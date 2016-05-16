#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clustering messages.
"""

import numpy as np

from collections import Counter
from pprint import pprint
import csv
import sys
import gensim
from gensim.corpora import Dictionary, HashDictionary, MmCorpus
from gensim.models import LdaMulticore, TfidfModel, HdpModel
from gensim.models.doc2vec import TaggedDocument, Doc2Vec

from happyfuntokenizing import Tokenizer
from KMeansClustering import KMeansClusterer

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
             'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now',
             '.', ',', '@', '!', '#', '$', '%', '^', '&', '*', ':', ";", '"', "'", "?",
             ] 

TOKENIZER = Tokenizer()

def tokenize(text):
    """Tokenize the text (using bi-grams)
    @returns:list[str]"""
    return [tok for tok in TOKENIZER.tokenize(text) if tok not in STOPWORDS]

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
    corpus = [d.doc2bow(doc, allow_update=True) for doc in documents]
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
    """
    Use the projection of documents onto topics to select documents that are most representative of each topic category.
    """
    assert P.shape[0] == len(documents)

    # For each topic, pick the top 5 documents
    for topic in range(P.shape[1]):
        print("Topic #{}".format(topic))
        pprint(model.show_topic(topic))
        for idx in reversed(P.T[topic].argsort()[-n_docs:]):
            print(documents[idx] + "\t" + str(P[idx]))
        print ("----\n")

def embed_documents(documents, size=100):
    """Use Doc2Vec to embed documents in a d-dimensional space.
    @documents:list[list[str]] - tokenized documents
    @returns:numpy.array - of (num_docs) x (dimension)
    """
    documents = [TaggedDocument(words=words, tags=[i]) for (i,words) in enumerate(documents)]
    model = Doc2Vec(documents, size=size, window=8, min_count=5, workers=4)
    return model

def cluster_kmeans(X, K = 2):
    """Cluster documents in X using a k-means model.
    @X:numpy.array - A (documents x vector representation) of the documents.
    @returns list[int], M - list of cluster assignments and cluster centroids
    """
    # Initialize k means (using kmeans++)
    N, D = X.shape
    algo = KMeansClusterer(K, D)
    _, Z, M = algo.run(X)

    return Z, M

def explain_clusters(M, X, documents):
    """
    Pick examples that are close to each cluster center.
    """
    _, D = X.shape
    K, D_ = M.shape
    assert D == D_

    for k in range(K):
        print("Topic #{}".format(k))
        D = ((X - M[k])**2).sum(1)
        for idx in D.argsort()[:10]:
            print(documents[idx])
        print("---\n")

def load_evaluation(path):
    import csv
    with open(path) as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader)
        assert header == ["text", "stance", "sentiment"]
        return [(t, int(s1), int(s2)) for t, s1, s2 in reader]

def evaluate_clustering(model, M):
    dataset = load_evaluation('data/labelled_tweets.tsv')
    # Load labelled tweets
    counter = Counter()
    K, _ = M.shape

    for tweet, stance, sentiment in dataset:
        v = model.infer_vector(tokenize(tweet))
        # Which mean is it closest to?
        cluster = ((M - v)**2).sum(1).argmin()
        counter[(cluster, "stance", stance)] += 1
        counter[(cluster, "sentiment", sentiment)] += 1

    for cluster in range(K):
        print("Cluster #{}".format(cluster))
        sentiment = [
                counter[cluster, "sentiment", -1],
                counter[cluster, "sentiment", 0],
                counter[cluster, "sentiment", 1],1]
        stance = [
                counter[cluster, "stance", -1],
                counter[cluster, "stance", 0],
                counter[cluster, "stance", 1],1]
        print("sentiment: {} ({}) {} ({}) {} ({}) = {}".format( 
                sentiment[0], sentiment[0] / sum(sentiment), 
                sentiment[1], sentiment[1] / sum(sentiment), 
                sentiment[2], sentiment[2] / sum(sentiment), 
                sum(sentiment)))
        print("stance: {} ({}) {} ({}) {} ({}) = {}".format( 
                stance[0], stance[0] / sum(stance), 
                stance[1], stance[1] / sum(stance), 
                stance[2], stance[2] / sum(stance), 
                sum(stance)))
    return counter

def do_command(args):
    # Load data
    data = load_data(args.input)
    ids, documents = zip(*data)
    tokenized = [tokenize(doc) for doc in documents]

    model = embed_documents(tokenized)
    X = np.vstack(model.docvecs)

    Z, M = cluster_kmeans(X, K = args.topics) 
    explain_clusters(M, X, documents)
    evaluate_clustering(model, M)

    #dictionary, corpus = to_corpus(tokenized)
    #model = fit_model(dictionary, corpus, n_topics=args.topics)
    ## project the data onto the corpus.
    #P = project_data(model, corpus)
    #
    #visualize_top_documents(model, P, documents)

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
