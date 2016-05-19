#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Convert CoNLL output produced by Tweebo to standoff.

@author Arun Tejasvi Chaganty <chaganty@cs.stanford.edu>
"""

import os
import csv
import sys

def handle_sentence(sentence):
    """
    Parses @sentence, a dependency graph encoded in CoNLL, and produces output @txt and @ann in standoff format.
    For reference, this is the CoNLL format used by Tweebo
1   ID  Token counter, starting at 1 for each new sentence.
2   FORM    Word form or punctuation symbol.
3   LEMMA   Lemma or stem (depending on particular data set) of word form, or an underscore if not available.
4   CPOSTAG     Coarse-grained part-of-speech tag, where tagset depends on the language.
5   POSTAG  Fine-grained part-of-speech tag, where the tagset depends on the language, or identical to the coarse-grained part-of-speech tag if not available.
6   FEATS   Unordered set of syntactic and/or morphological features (depending on the particular language), separated by a vertical bar (|), or an underscore if not available.
7   HEAD    Head of the current token, which is either a value of ID or zero ('0'). Note that depending on the original treebank annotation, there may be multiple tokens with an ID of zero.
8   DEPREL  Dependency relation to the HEAD. The set of dependency relations depends on the particular language. Note that depending on the original treebank annotation, the dependency relation may be meaningfull or simply 'ROOT'.

    @sentence: an iterable over tuples of 8 elements (described above).
    @returns: str, str: the text and annotation in standoff format.
    """ 

    # These tags are defined in the annotation guidelines specified
    # here: http://www.cs.cmu.edu/~ark/TweetNLP/annot_guidelines.pdf
    # Translating the tags because brat does not like using punctuation
    # for its tags.
    TAG = {
        "N":       "NN",
        "O":       "PRP",
        "^":       "NNP",
        "S":       "NNS",
        "Z":       "NNPOS",
        "V":       "VB",
        "A":       "ADJ",
        "R":       "RB",
        "!":       "UH",
        "D":       "DET",
        "P":       "IN",
        "&":       "CC",
        "T":       "RP",
        "X":       "EX",
        ",":       "PDT ",
        "#":       "HASH",
        "@":       "AT",
        "~":       "DIS",
        "U":       "URL",
        "E":       "EMOT",
        "$":       "NUM",
        "G":       "ABBV",
        "L":       "NOMV",
        "M":       "NNPV",
        "Y":       "EXV",
        }

    txt, ann = "", ""

    start = 0
    for idx, token, _, _, tag, _, head, _ in sentence:
        idx = int(idx)
        head = int(head)
        end = start + len(token)
        if tag == ',' and head == -1:
            pass
        else:
            ann += "T{}\t{} {} {}\t{}\n".format(
                idx, # Trigger id
                TAG[tag], start, end,
                token)
        if tag == ",":
            start = end
        else:
            start = end + 1
        if tag == ",":
            txt += token
        elif idx == 1:
            txt += token
        else:
            txt += " " + token


    for idx, _, _, _, _, _, head, rel in sentence:
        idx = int(idx)
        head = int(head)
        if head != -1 and head != 0:
            ann += "R{}\t{} Arg1:T{} Arg2:T{}\n".format(
                idx,
                rel, idx, head)

    return txt, ann

def save(root, i, txt, ann):
    """
    Save the text and annotation in separate files as required by the standoff format.
    """
    txt_fn = os.path.join(root, '%02d.txt'%i)
    ann_fn = os.path.join(root, '%02d.ann'%i)
    with open(txt_fn, 'w') as txt_f, open(ann_fn, 'w') as ann_f:
        txt_f.write(txt)
        ann_f.write(ann)

def do_command(args):
    assert os.path.isdir(args.output_dir)

    # NOTE: ignoring quoting because CoNLL doesn't do quoting and the
    # case where you have a single token '"' destroys the CSV reader.
    reader = csv.reader(args.input, delimiter="\t", quoting = csv.QUOTE_NONE, quotechar="")

    i, sentence = 0, []
    # Parse the input in the file.
    for row in reader:
        # There is an empty new line between each sentence
        if len(row) == 0:
            # Process sentence just read
            txt, ann = handle_sentence(sentence)
            save(args.output_dir, i, txt, ann)
            i, sentence = i+1, []
        else:
            # Append to existing sentence
            sentence.append(row)
    # Edge case processing
    if len(sentence) != 0:
        txt, ann = handle_sentence(sentence)
        save(args.output_dir, i, txt, ann)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser( description='This script reads output produced in CoNLL format by the TweeboParser and produces output in standoff format' )
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin, help="input in CoNLL format.")
    parser.add_argument('--output-dir', type=str, default='.', help="Directory to save text and annotation files required by the standoff format.")
    parser.set_defaults(func=do_command)

    ARGS = parser.parse_args()
    ARGS.func(ARGS)
