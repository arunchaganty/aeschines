#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Annotate tweets using CoreNLP
"""

import csv
import sys
from tqdm import tqdm
from collections import namedtuple
from stanza.nlp.corenlp import CoreNLPClient
from stanza.util.postgres import to_psql_array

def do_command(args):
    reader = csv.reader(args.input, delimiter="\t")
    header = next(reader)
    assert all(field in header for field in ("id", "text"))

    Tweet = namedtuple("Tweet", header)
    client = CoreNLPClient()
    annotators = "tokenize ssplit lemma pos".split()

    writer = csv.writer(args.output, delimiter="\t")
    writer.writerow(["id", "tokens", "lemmas", "pos_tags"])

    for tweet in tqdm(Tweet(*row) for row in reader):
        doc = client.annotate(tweet.text, annotators)
        tokens, lemmas, pos_tags = [], [], []
        for sentence in doc:
            tokens += sentence.words
            lemmas += sentence.lemmas
            pos_tags += sentence.pos_tags
        writer.writerow([tweet.id, to_psql_array(tokens), to_psql_array(lemmas), to_psql_array(pos_tags)])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser( description='' )
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="")
    parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout, help="")
    parser.set_defaults(func=do_command)

    #subparsers = parser.add_subparsers()
    #command_parser = subparsers.add_parser('command', help='' )
    #command_parser.set_defaults(func=do_command)

    ARGS = parser.parse_args()
    ARGS.func(ARGS)
