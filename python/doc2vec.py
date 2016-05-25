#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Label documents with doc2vec.
"""

import numpy as np

import os
from collections import Counter
from pprint import pprint
import csv
import sys
import gensim
from gensim.corpora import Dictionary, HashDictionary, MmCorpus
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from sklearn.neighbors import NearestNeighbors

from happyfuntokenizing import Tokenizer

import ipdb

norm = np.linalg.norm

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
             'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
             'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
             'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
             'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
             'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
             'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
             'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
             'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
             'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
             'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
             'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now',
             '.', ',', '@', '!', '#', '$', '%', '^', '&', '*', ':', ";", '"', "'", "?",
             ] 

TOKENIZER = Tokenizer()

def tokenize(text):
    """Tokenize the text (using bi-grams)
    @returns:list[str]"""
    return [tok for tok in TOKENIZER.tokenize(text)]
    return #[tok for tok in TOKENIZER.tokenize(text) if tok not in STOPWORDS]

def load_data(stream):
    """
    Return a list of tokens.
    """
    reader = csv.reader(stream, delimiter='\t')
    header = next(reader)
    assert header == ["id", "text"]

    return reader

def embed_documents(documents, size=100):
    """Use Doc2Vec to embed documents in a d-dimensional space.
    @documents:list[list[str]] - tokenized documents
    @returns:numpy.array - of (num_docs) x (dimension)
    """
    documents = (TaggedDocument(words=words, tags=[id]) for (id,words) in documents)
    model = Doc2Vec(documents, size=size, window=8, min_count=5, workers=4)
    return model

#def find_nearest_neighbors(vecs):
#    nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(vecs)
#    distances, indices = nbrs.kneighbors(vecs)
#    return [(i, j, distance) for i in range(len(vecs)) for j, distance in nbrs.kneighbors(vecs[i])]

#def find_nearest_neighbors(vecs):
#    for i, v in enumerate(vecs):
#        distances = norm(vecs - v, axis = 1)
#        neighbors = distances.argsort()[1:11]
#        for j in neighbors:
#            yield (i, j, np.exp(-distances[j]))

def find_nearest_neighbors(X):
    # Normalize the vectors
    X = (X.T / norm(X, axis=1)).T
    for i, x in enumerate(X):
        # compute inner product.
        distances = X.dot(x)
        neighbors = distances.argsort()[1:11]
        for j in neighbors:
            yield (i, j, distances[j])

def do_command(args):
    # Load data
    data = load_data(args.input)
    #ids, documents = zip(*data)
    data = [(id, tokenize(doc)) for id, doc in data]
    ids = [id for id, _ in data]

    if not os.path.exists(args.modelfile):
        model = embed_documents(data)
        # Save model
        model.save(args.modelfile)
    else:
        model = Doc2Vec.load(args.modelfile)
        #map(model.infer_tokens, tokenized)
    print("Loaded model.")
    # Do k-nearest neighbors search.

    writer = csv.writer(args.output, delimiter='\t')
    writer.writerow(["id1", "id2", "score"])
    count = int(args.count) if args.count > 0 else len(model.docvecs)
    vectors = np.array([model.docvecs[i] for i in range(count)])
    del model # clear up memory

    for i, j, score in find_nearest_neighbors(vectors):
        id1, id2 = ids[i], ids[j]
        writer.writerow([id1, id2, score])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser( description='' )
    parser.add_argument('--modelfile', type=str, default='doc2vec.model', help="Model file")
    parser.add_argument('--nneighbors', type=str, default='doc2vec.neighbors', help="Neighbors")
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="Input file")
    parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="Output vectors.")
    parser.add_argument('--count', type=float, default=1e5, help="number of vectors to use.")
    parser.set_defaults(func=do_command)

    #subparsers = parser.add_subparsers()
    #command_parser = subparsers.add_parser('command', help='' )
    #command_parser.set_defaults(func=do_command)

    ARGS = parser.parse_args()
    ARGS.func(ARGS)
