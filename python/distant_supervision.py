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

import sys
import csv

import numpy as np
from keras import backend as K
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Reshape
from keras.layers.convolutional import Convolution2D, MaxPooling2D

def do_command(args):
    tweets = RowObjectFactory.from_stream(csv.reader(args.input))
    for row in reader:
        writer.writerow(row)

if __name__ == "__main__":
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="Input file")
    parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="Output file")
    parser.set_defaults(func=do_command)

    #subparsers = parser.add_subparsers()
    #command_parser = subparsers.add_parser('command', help='' )
    #command_parser.set_defaults(func=do_command)


    ARGS = parser.parse_args()
    ARGS.func(ARGS)

