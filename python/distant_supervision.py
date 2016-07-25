#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A neural distant supervision model based on Vijayaraghavan, P.,
Vosoughi, S., & Roy, D. (2016). Automatic Detection and Categorization
of Election-Related Tweets. Computation and Language; Information
Theory; Information Theory. Retrieved from
http://arxiv.org/abs/1605.05150.
"""
from __future__ import print_function

import csv

import ipdb

import numpy as np
from numpy import zeros, array
from keras import backend as K
from keras.models import Sequential, Model
from keras.models import model_from_json
from keras.layers import Dense, Dropout, Activation, Reshape, Flatten, Merge, Input, Convolution2D, MaxPooling2D, merge

from util import tokenize, Index, to_ascii, ordc, RowObjectFactory, log, WordVectorModel, grouper
from tqdm import tqdm

def float_(lbl):
    """
    Safe float for reading input.
    """
    return float(lbl) if lbl != '' else 0.

def process_input(tweet):
    """
    Process input data to tokenize and make labels.
    """
    tokens = tokenize(to_ascii(tweet.text))
    labels = [float_(tweet.hc), float_(tweet.bs), float_(tweet.dt), float_(tweet.tc)]
    return tweet.id, tokens, labels

def split_data(X, y, dev_split):
    """
    Split training data into train and dev.
    """
    # Make splits of train and validation data.
    n_train, n_val = len(X) - int(len(X) * dev_split), int(len(X) * dev_split)
    X_train, y_train = X[:n_train], y[:n_train]
    X_val, y_val = X[n_train:], y[n_train:]

    return X_train, y_train, X_val, y_val

def load_data_raw(istream):
    """
    Load training data from a stream of input.
    Input is a TSV with fields (id, text, label).
    Returns a set of words, and input.
    """
    log("Loading training data...")
    data = list(map(process_input, RowObjectFactory.from_stream(csv.reader(istream, delimiter="\t"))))
    np.random.shuffle(data)
    ids, X, y = zip(*data)

    log("Done. Loaded {} instances", len(data))

    return ids, X, y

def save_model(model, model_output, weights_output):
    """
    Save model architecture and weights.
    """
    model_output.write(model.to_json())
    model.save_weights(weights_output)

def load_model(model_input, weights_input):
    """
    Load model architecture and weights.
    """
    json = model_input.read()
    model = model_from_json(json)
    model.load_weights(weights_input)
    return model

def build_model(args, input_shape, output_shape, output_type='tanh'):
    """
    Build a model.
    """
    N_FILTERS = 200
    WINDOWS = [2,3,4]

    _, N, D = input_shape

    x = Input(shape=input_shape)

    # Max pooling layer
    window_models = {}
    for window in WINDOWS:
        # 2D Convolution - 200 filters, with a filter size of LxD
        y = Convolution2D(N_FILTERS, window, D, activation='relu')(x)
        y = MaxPooling2D(pool_size=(N - window + 1, 1))(y)
        window_models[window] = y

    # droput
    z = merge(list(window_models.values()), mode='concat')
    z = Dropout(0.5)(z)
    z = Flatten()(z)

    # Dense to k = 200
    z = Dense(128, activation='relu')(z)
    # dropout
    z = Dropout(0.5)(z)
    # Softmax to 4.
    z = Dense(output_shape, activation=output_type)(z)

    model = Model(input=[x], output=[z])

    model.compile(
        optimizer='rmsprop',
        loss='mse',
        metrics=['accuracy'])

    return model

class Scorer(object):
    def __init__(self, model):
        self.metrics = model.metrics_names
        self.score = [0. for _ in self.metrics]
        self.n = 0

    def update(self, score, n_items):
        self.n += n_items
        for i in range(len(score)):
            self.score[i] += (n_items * score[i] - self.score[i])/self.n

    def __str__(self):
        return "\t".join(str(name) + " " + str(score) for name, score in zip(self.metrics, self.score))

    def keys(self):
        return self.metrics

    def values(self):
        return "\t".join(str(score) for score in self.score)



def do_train(args):
    """
    Train the model using the provided arguments.
    """

    # Assumption: it is cheap to store all the data in text form in
    # memory (it's only about 144mb)
    _, X, y = load_data_raw(args.input)
    X_train, y_train, X_val, y_val = split_data(X, y, args.dev_split)

    # Assumption: word vector model will also easily fit in memory.
    wvecs = WordVectorModel.from_file(args.wvecs, False, '*UNKNOWN*')

    # Typical values are 50, 50
    input_shape = (1,args.n_words, wvecs.dim)
    output_shape = len(y[0])

    # Build model
    model = build_model(args, input_shape=input_shape, output_shape=output_shape, output_type=args.output_type)

    # Training data on the other hand will not. Each input instance is
    # 50x50 matrix with 8bytes per value: that's about 20kb.
    # Assuming we want to store only about 500mb in memory at a time,
    # that means we want at most 25k items in a batch.
    # Typically minibatches of 32-128 are probably ok. Let's keep it
    # that way?
    for epoch in range(args.n_epochs):
        log("== Training model, epoch {}", epoch)

        scorer = Scorer(model)
        for xy in tqdm(grouper(args.batch_size, zip(X_train, y_train))):
            X_batch, y_batch = zip(*xy)
            X_batch, y_batch = wvecs.embed_sentences(X_batch), array(y_batch)
            score = model.train_on_batch(X_batch, y_batch)
            scorer.update(score, len(X_batch))
        log("=== train error: {}", scorer)

        scorer = Scorer(model)
        for xy in tqdm(grouper(args.batch_size, zip(X_val, y_val))):
            X_batch, y_batch = zip(*xy)
            X_batch, y_batch = wvecs.embed_sentences(X_batch), array(y_batch)
            score = model.test_on_batch(X_batch, y_batch)
            scorer.update(score, len(X_batch))
        log("=== val error: {}", scorer)

    ## Save the model
    save_model(model, args.model, args.weights)

    #ys_ = model.predict(X_train_)
    #run_model(X_train, y_train, ys_)

def run_model(X, ys, ys_):
    print("i\ttext\tactual\tpredicted")
    for i, (x, y, y_) in enumerate(zip(X, ys, ys_)):
        print("{}\t{}\t{}\t{}".format(i, " ".join(x), y, y_))

def do_run(args):
    """
    Run the neural net to predict on new data.
    """
    # Load the model and weights
    model = load_model(args.model, args.weights)
    wvecs = WordVectorModel.from_file(args.wvecs, False, '*UNKNOWN*')

    data = map(lambda tweet: (tweet.id, tokenize(to_ascii(tweet.text))), RowObjectFactory.from_stream(csv.reader(args.input, delimiter="\t")))
    writer = csv.writer(args.output, delimiter='\t')

    for ix in tqdm(grouper(args.batch_size, data)):
        ids_batch, X_batch = zip(*ix)
        X_batch = wvecs.embed_sentences(X_batch)
        labels = model.predict_on_batch(X_batch)
        for id, label in zip(ids_batch, labels):
            writer.writerow([id,] + [float(l) for l in label])

if __name__ == "__main__":
    import sys, argparse
    parser = argparse.ArgumentParser(description='Distant supervision')
    parser.add_argument('--seed', default=42, help="Random seed to use")

    subparsers = parser.add_subparsers()
    command_parser = subparsers.add_parser('train', help='Trains the distant supervision model')
    command_parser.add_argument('--input', type=argparse.FileType('r'), help="Input tweets represented as a TSV with fields id, text, label")
    command_parser.add_argument('--wvecs', type=argparse.FileType('r'), help="Input word vector embeddings")
    command_parser.add_argument('--model', type=argparse.FileType('w'), help="Where to save the model")
    command_parser.add_argument('--dev_split', type=float, default=0.1, help="How much of the data to save for dev.")
    command_parser.add_argument('--n_epochs', type=int, default=10, help="Number of epochs (full passes of the data) to train the model on.")
    command_parser.add_argument('--batch_size', type=int, default=32, help="Number of item to train with in a batch.")
    command_parser.add_argument('--output_type', choices=["tanh", "sigmoid"], default="tanh", help="Number of item to train with in a batch.")
    command_parser.add_argument('--weights', type=str, required=True, help="Where to save the model weights")
    command_parser.add_argument('--n_words', type=int, default=50, help="Number of words to use.")
    command_parser.set_defaults(func=do_train)

    command_parser = subparsers.add_parser('run', help='Runs the distant supervision model on individual models')
    command_parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="Input tweets")
    command_parser.add_argument('--model', type=argparse.FileType('r'), help="Where to save the model")
    command_parser.add_argument('--weights', type=str, required=True, help="Where to save the model weights")
    command_parser.add_argument('--batch_size', type=int, default=32, help="Number of item to train with in a batch.")
    command_parser.add_argument('--wvecs', type=argparse.FileType('r'), help="Input word vector embeddings")
    command_parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="Output labels on the tweets")
    command_parser.set_defaults(func=do_run)

    ARGS = parser.parse_args()

    np.random.seed(ARGS.seed)

    ARGS.func(ARGS)

