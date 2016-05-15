#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clustering messages.
"""

import numpy as np

from pprint import pprint
import csv
import sys
import gensim
from gensim.corpora import Dictionary, HashDictionary, MmCorpus
from gensim.models import LdaMulticore, TfidfModel, HdpModel

import ipdb

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
             'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'] 

def tokenize(text):
    """Tokenize the text (using bi-grams)
    @returns:list[str]"""
    tokens = [token for token in text.lower().split() if token not in STOPWORDS and len(token) >= 3]
    return [" ".join(tokens[i:i+2]) for i in range(len(tokens)-1)]

def load_data(stream):
    """
    Return a list of tokens.
    """
    reader = csv.reader(stream, delimiter='\t')
    header = next(reader)
    assert header == ["id", "text"]

    return list(reader)

def to_corpus(documents):
    """
    Make into a corpus
    @documents:list[list[tuple[str,int]]] of bows
    @returns Dictionary, Corpus
    """
    d = Dictionary()
    corpus = [d.doc2bow(tokenize(doc), allow_update=True) for doc in documents]
    return d, corpus

def fit_model(dictionary, corpus, n_topics=2, savefile=None):
    """
    Fit a model using the corpus.
    @dictionary:Dictionary
    @corpus:Corpus
    @n_topics:int
    @returns Model
    """
    # Convertt the corpus into an in memory form to be faster to
    # access with LDA
    #MmCorpus.serialize(savefile, corpus)
    #mm = MmCorpus(savefile)

    # Choice of per-doc topic asymmetric prior and per-topic word
    # symmetric prior as per Wallach, Mimno and McCallum 2010.
    return LdaMulticore(corpus=corpus, id2word=dictionary, num_topics=n_topics, alpha='asymmetric', eta='symmetric')

def project_data(model, corpus):
    """Project documents onto the topic model.
    @model:Model - already trained
    @corpus:Corpus - ids for interfacing with the database.
    @returns:list[list[float]] - topic scores per document
    """
    X = np.zeros((len(corpus), model.num_topics))
    for i, doc in enumerate(corpus):
        for j, v in model[doc]:
            X[i,j] = v
    return X

def visualize_top_documents(model, P, documents, n_docs=10):
    assert P.shape[0] == len(documents)

    # For each topic, pick the top 5 documents
    for topic in range(P.shape[1]):
        print("Topic #{}".format(topic))
        pprint(model.show_topic(topic))
        for idx in reversed(P.T[topic].argsort()[-n_docs:]):
            print(documents[idx])
        print ("----\n")

def do_command(args):
    # Load data
    data = load_data(args.input)
    ids, documents = zip(*data)

    dictionary, corpus = to_corpus(documents)
    model = fit_model(dictionary, corpus, n_topics=args.topics)
    # project the data onto the corpus.
    P = project_data(model, corpus)
    
    visualize_top_documents(model, P, documents)

    # save output.

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser( description='' )
    parser.add_argument('--topics', type=int, default=2, help="")
    parser.add_argument('--savefile', type=str, default='test.mm', help="")
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="")
    parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="")
    parser.set_defaults(func=do_command)

    #subparsers = parser.add_subparsers()
    #command_parser = subparsers.add_parser('command', help='' )
    #command_parser.set_defaults(func=do_command)

    ARGS = parser.parse_args()
    ARGS.func(ARGS)
