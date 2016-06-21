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
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers.core import Dense, Dropout, Activation, Reshape, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D

from util import tokenize, Index, to_ascii, ordc, RowObjectFactory, log, WordVectorModel

def float_(lbl):
    return float(lbl) if lbl != '' else 0.

def process_input(tweet):
    tokens = tokenize(to_ascii(tweet.text))
    labels = [float_(tweet.hc), float_(tweet.bs), float_(tweet.dt), float_(tweet.tc)]
    return tokens, labels

def load_data_raw(istream, dev_split):
    """
    Load training data from a stream of input.
    Input is a TSV with fields (id, text, label).
    Returns a set of words, and input.
    """
    log("Loading training data...")
    data = list(map(process_input, RowObjectFactory.from_stream(csv.reader(istream, delimiter="\t"))))
    np.random.shuffle(data)

    # Make splits of train and validation data.
    n_train, n_val = len(data) - int(len(data) * dev_split), int(len(data) * dev_split)
    X_train, y_train = zip(*data[:n_train])
    X_val, y_val = zip(*data[n_train:])

    log("Done. Loaded {} train {} val instances", n_train, n_val)

    return X_train, y_train, X_val, y_val

def save_model(model, model_output, weights_output):
    """
    Save model architecture and weights.
    """
    model_output.write(model.to_json())
    model.save_weights(weights_output)

def load_model(model, model_input, weights_input):
    """
    Load model architecture and weights.
    """
    model = model_from_json(model_input)
    model.load_weights(weights_input)
    return model

def build_model(args, input_shape):
    model = Sequential()

    N, D = input_shape

    # 2D Convolution - 200 filters, with a filter size of LxD

    # Max pooling layer

    # droput
    # Dense to k = 200
    # dropout
    # Softmax to 4.

    # Input layer.
    model.add(Reshape((N*D,), input_shape=input_shape))
    model.add(Dense(
        4,
        activation='linear'))

    model.compile(
        optimizer='rmsprop',
        loss='mse',
        metrics=['accuracy'])

    return model

def do_train(args):
    """
    Train the model using the provided arguments.
    """

    X_train, y_train, X_val, y_val = load_data_raw(args.input, args.dev_split)
    wvecs = WordVectorModel.from_file(args.wvecs, False, '*UNKNOWN*')

    N, D = args.n_words, wvecs.dim

    # Build model
    model = build_model(args, input_shape=(N,D))

    # Load data.
    X_train, y_train, X_val, y_val = wvecs.embed_sentences(X_train), array(y_train), wvecs.embed_sentences(X_val), array(y_val)

    # Train the model.
    for _ in range(args.training_epochs):
        log("=== Training the model.")
        model.fit(X_train, y_train, nb_epoch=5, batch_size=32)

        score = model.evaluate(X_val, y_val, batch_size=32)
        log("=== validiation error: loss: {}, acc: {}", *score)

    ## Save the model
    #save_model(model, args.model, args.weights)

def do_run(args):
    """
    Run the neural net to predict on new data.
    """
    # Load the model and weights
    # For each input example, predict the output
    raise NotImplementedError()

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
    command_parser.add_argument('--training_epochs', type=int, default=10, help="Number of epochs (full passes of the data) to train the model on.")
    command_parser.add_argument('--weights', type=str, help="Where to save the model weights")
    command_parser.add_argument('--n_words', type=int, default=50, help="Number of words to use.")
    command_parser.set_defaults(func=do_train)

    command_parser = subparsers.add_parser('run', help='Runs the distant supervision model on individual models')
    command_parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="Input tweets")
    command_parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="Output labels on the tweets")
    command_parser.set_defaults(func=do_run)

    ARGS = parser.parse_args()

    np.random.seed(ARGS.seed)

    ARGS.func(ARGS)

