#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import csv
import numpy as np
from util import Index, to_ascii, ordc

def to_features(text):
    """
    Preprocesses the text of the tweet into a 150x70 array. The rows
    correspond to the length of the tweet (zero-padded). The features
    are one-hot corresponding to 96 valid character values corresponding
    to:
        - 10 for numbers
        - 33 for special characters [ !@#$%^&*()_+-=[]{}\|~`:;'",<.>/?]
        - 26 for lower-case characters
        - 26 for upper-case characters
        - 01 for unknown

    The encoding of characters corresponds to the ASCII table from 32 (' ') to 126 ('~').
    """
    assert len(text) <= 150
    features = np.zeros((150, 96))
    for i, c in enumerate(text):
        features[i][idx(c)] = 1
    return features

def int_(lbl):
    return int(lbl) if lbl != '' else 0

def prepare_data(istream):
    """
    Assumes that the input is a stream of a Tweet objects that contain
    the attributes:
        - text
        - label
    Labels are also returned as one-hot vectors.
    """
    #n_instances, labels = get_data_spec(istream)
    tweets = RowObjectFactory.from_stream(csv.reader(istream))
    #X_train, y_train = np.zeros((n_instances,150, 96)), np.zeros((n_instances, len(labels)))
    X_train, y_train = [], []

    for i, tweet in enumerate(tweets): 
        feats = to_features(to_ascii(tweet.text))
        labels = [int_(tweet.hc), int_(tweet.bs), int_(tweet.dt), int_(tweet.tc)]

        X_train.append(feats)
        y_train.append(labels)

    return np.array(X_train), np.array(y_train)

#def get_data_spec(istream):
#    """
#    Read input to get some properties from it. Resets the stream to the beginning when done.
#    """
#    n_instances, labels = 0, Index()
#    for obj in RowObjectFactory.from_stream(csv.reader(istream)):
#        n_instances += 1
#        labels[obj.label]
#    istream.seek(0)
#    return n_instances, labels

def do_command(args):
    X_train, y_train = prepare_data(args.input)
    np.savez(args.output, X_train = X_train, y_train = y_train)

if __name__ == "__main__":
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='Process a file with labels')
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="Input file")
    parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="Output file")
    parser.set_defaults(func=do_command)

    #subparsers = parser.add_subparsers()
    #command_parser = subparsers.add_parser('command', help='' )
    #command_parser.set_defaults(func=do_command)


    ARGS = parser.parse_args()
    ARGS.func(ARGS)

