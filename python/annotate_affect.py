#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Annotate affect.
"""

import csv
import sys
from tqdm import tqdm
from collections import namedtuple
from stanza.util.postgres import parse_psql_array
from numpy import array

def load_affect_dict(fstream):
    """
    Loads a dictionary with affect from input.
    """
    reader = csv.reader(fstream, delimiter=",")
    header = next(reader)
    legend = {
        'Word' : 1,
        'V.Mean.Sum' : 2,
        'A.Mean.Sum' : 5,
        'D.Mean.Sum' : 8,
        }
    assert all(header[v] == k for k,v in legend.items()), "Input file had invalid header"

    affect_dict = {}
    for row in reader:
        lemma, valence, arousal, dominance = row[legend['Word']], row[legend['V.Mean.Sum']], row[legend['A.Mean.Sum']], row[legend['D.Mean.Sum']]
        affect_dict[lemma] = array([float(valence), float(arousal), float(dominance)])

    return affect_dict

def do_command(args):
    affect_dict = load_affect_dict(args.affect_dict)

    reader = csv.reader(args.input, delimiter="\t")
    header = next(reader)
    assert all(field in header for field in ("id", "lemmas"))

    Tweet = namedtuple("Tweet", header)

    writer = csv.writer(args.output, delimiter="\t")
    writer.writerow(["id", "valence", "arousal", "dominance"])

    for tweet in tqdm(Tweet(*row) for row in reader):
        # Get the lemmas from the tweet
        lemmas = map(str.lower, parse_psql_array(tweet.lemmas))
        # Filter lemmas.
        lemmas = [affect_dict[lemma] for lemma in lemmas if lemma in affect_dict]

        # If there are any lemmas, then take their average and return as
        # mean arousal.
        if len(lemmas) > 0:
            valence, arousal, dominance = sum(lemmas)/len(lemmas)
            writer.writerow([tweet.id, valence, arousal, dominance])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser( description='' )
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="")
    parser.add_argument('--affect_dict', type=argparse.FileType('r'), default='data/Ratings_Warriner_et_al.csv', help="The Warriner et al affect lexicon")
    parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="")
    parser.set_defaults(func=do_command)

    ARGS = parser.parse_args()
    ARGS.func(ARGS)
