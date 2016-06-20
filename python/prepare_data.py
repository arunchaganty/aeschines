#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import csv
import numpy as np
from scipy.sparse import csc_matrix
from util import Index, to_ascii, ordc, RowObjectFactory
from tqdm import tqdm

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
    text = text[:150]
    assert len(text) <= 150, "Tweet is too long."

    row, col, data = zip(*((i, ordc(c), 1) for i, c in enumerate(text)))
    return csc_matrix((data, (row, col)), shape=(150, 96))

def float_(lbl):
    return float(lbl) if lbl != '' else 0

def prepare_data(tweets):
    """
    Assumes that the input is a stream of a Tweet objects that contain
    the attributes:
        - text
        - label
    Labels are also returned as one-hot vectors.
    """
    X_train, y_train = [], []

    for tweet in tqdm(tweets):
        feats = to_features(to_ascii(tweet.text))
        labels = [float_(tweet.hc), float_(tweet.bs), float_(tweet.dt), float_(tweet.tc)]

        X_train.append(feats)
        y_train.append(labels)

    return np.array(X_train), np.array(y_train)

def do_command(args):
    tweets = RowObjectFactory.from_stream(csv.reader(args.input, delimiter="\t"))
    X_train, y_train = prepare_data(tweets)
    np.savez(args.output, X_train = X_train, y_train = y_train)

if __name__ == "__main__":
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='Process a file with labels')
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="Input file")
    parser.add_argument('--output', type=argparse.FileType('wb'), default=sys.stdout, help="Output file")
    parser.set_defaults(func=do_command)

    ARGS = parser.parse_args()
    ARGS.func(ARGS)

