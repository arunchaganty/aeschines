#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import csv
import sys

class tuple_(tuple):
    def __init__(self, *elems):
        super(tuple_, self).__init__(elems)

    def __add__(self, other):
        return tuple_(e1 + e2 for e1, e2 in zip(self, other))

    def __sub__(self, other):
        return tuple_(e1 - e2 for e1, e2 in zip(self, other))

    def __mul__(self, other):
        return tuple_(e1 * other for e1 in self)

    def __div__(self, other):
        return tuple_(e1 / other for e1 in self)

def load_lexicon(fstream):
    reader = csv.reader(fstream)
    header = next(reader)
    #assert (header[1], header[2], header[5], header[8]) == "word",
    return {r[1] : tuple_(map(lambda f: (f-5.)/5., map(float, (r[2], r[5], r[8])))) for r in reader}

def do_command(args):
    reader = csv.reader(args.input, delimiter='\t')
    writer = csv.writer(args.output, delimiter='\t')
    lexicon = load_lexicon(args.lexicon)

    writer.writerow(["line", "valence", "arousal", "dominance"])

    header = next(reader)
    for line in reader:
        line, = line
        count = sum(1 for word in line.lower().split() if word in lexicon)
        valence, arousal, dominance = sum((lexicon.get(word, tuple_([0,0,0])) for word in line.lower().split()), tuple_([0,0,0]))/count if count > 0 else (0,0,0)
        if abs(valence) < 0.1 and abs(arousal) < 0.1 and abs(dominance) < 0.1:
            continue

        writer.writerow([line, valence, arousal, dominance])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="")
    parser.add_argument('--lexicon', type=argparse.FileType('r'), default='../data/Ratings_Warriner_et_al.csv', help="")
    parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="")
    parser.set_defaults(func=do_command)

    #subparsers = parser.add_subparsers()
    #command_parser = subparsers.add_parser('command', help='' )
    #command_parser.set_defaults(func=do_command)

    ARGS = parser.parse_args()
    ARGS.func(ARGS)
