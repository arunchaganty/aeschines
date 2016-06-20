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

import numpy as np
from keras import backend as K
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers.core import Dense, Dropout, Activation, Reshape
from keras.layers.convolutional import Convolution2D, MaxPooling2D

def load_data(npz, dev_split):
    """
    Load training data from numpy.
    """
    data = np.load(npz)
    X_train, y_train = data['X_train'], data['y_train']
    n_train, n_val = len(X_train) - int(len(X_train) * dev_split), int(len(X_train) * dev_split)
    X_train, X_val = X_train[:n_train], X_train[n_train:]
    y_train, y_val = y_train[:n_train], y_train[n_train:]

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

def build_model(args):
    model = Sequential()

    # Input layer.
    # data.

    # 1d convolution

    return model

def do_train(args):
    """
    Train the model using the provided arguments.
    """
    # Build model
    model = build_model(args)

    # Load data.
    X_train, y_train, X_val, y_val = load_data(args.input, args.dev_split)

    # Train the model.
    for _ in range(args.training_epochs):
        print("=== Training the model.")
        model.fit(X_train, y_train, nb_epoch=5, batch_size=32)

        print("=== validiation error")
        model.evaluate(X_val, y_val, batch_size=32)

    # Save the model
    save_model(model, args.model, args.weights)

def do_run(args):
    """
    Run the neural net to predict on new data.
    """
    # Load the model and weights
    # For each input example, predict the output
    raise NotImplementedError()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Distant supervision')

    subparsers = parser.add_subparsers()
    command_parser = subparsers.add_parser('train', help='Trains the distant supervision model')
    command_parser.add_argument('--input', type=argparse.FileType('r'), help="Input tweets represented as a 150x70 matrix (each)")
    command_parser.add_argument('--model', type=argparse.FileType('w'), help="Where to save the model")
    command_parser.add_argument('--dev_split', type=float, default=0.1, help="How much of the data to save for dev.")
    command_parser.add_argument('--training_epochs', type=int, default=10, help="Number of epochs (full passes of the data) to train the model on.")
    command_parser.add_argument('--weights', type=str, help="Where to save the model weights")
    command_parser.set_defaults(func=do_train)

    command_parser = subparsers.add_parser('run', help='Runs the distant supervision model on individual models')
    command_parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="Input tweets")
    command_parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="Output labels on the tweets")
    command_parser.set_defaults(func=do_run)


    ARGS = parser.parse_args()
    ARGS.func(ARGS)

