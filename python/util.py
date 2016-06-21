#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Useful utilities
"""

import sys
import numpy as np
from numpy import array, zeros
import csv
from happyfuntokenizing import Tokenizer
TOKENIZER = Tokenizer(preserve_case=True)

from happyfuntokenizing import Tokenizer
TOKENIZER = Tokenizer(preserve_case=True)
import itertools


BLUE = '\033[34;1m'
CLOSE = '\033[0m'

def log(msg, *args):
    sys.stderr.write(BLUE + str(msg).format(*args) + CLOSE + "\n")

class Index(object):
    """
    A lazy feature index, which maps string input to an integer label.
    """
    def __init__(self, max_labels = None):
        self.index = {}
        self.max_labels = max_labels

    def __getitem__(self, key):
        if key not in self.index:
            assert self.max_labels is None or len(self.index) < self.max_labels, "Too many unique labels"
            self.index[key] = len(self.index)
        return self.index[key]

UNICODE_EMOJI_TO_ASCII_TABLE = [
        ('o/'    , '👋'),
        ('</3'   , '💔'),
        ('<3'    , '💗'),
        ('=D'    , '😁'),
        (r":\')"  , '😂'),
        (':)'    , '😄'),
        ('0:)'   , '😇'),
        ('3:)'   , '😈'),
        ('*)'    , '😉'),
        (':|'    , '😐'),
        (':('    , '😒'),
        ('%)'    , '😖'),
        (':P'    , '😜'),
        (':@'    , '😠'),
        (':/'    , '😡'),
        (r":\'("  , '😢'),
        ('^5'    , '😤'),
        ('|-O'   , '😫'),
        (':###..', '😰'),
        ('D:'    , '😱'),
        (':O'    , '😲'),
        (':$'    , '😳'),
        ('#-)'   , '😵'),
        (':#'    , '😶'),
        (':-J'   , '😼'),
        (':*'    , '😽'),
    ]

def to_ascii(text):
    # Convert from ascii
    for asci, unicod in UNICODE_EMOJI_TO_ASCII_TABLE:
        text = text.replace(unicod, asci)
    text = text.encode('ascii', errors='ignore').decode('ascii', errors='ignore')
    return text

def tokenize(text):
    """
    Call the tokenizer
    """
    return TOKENIZER.tokenize(text)

def ordc(c):
    """
    Compressed version of ord that returns indices between 0 and 95.
    """
    c = ord(c)
    if c < 32 or c > 126: return 95
    else: return c - 32

class RowObject(object):
    """
    Is an empty object that can be modified by the factory to have the required fields.
    """
    pass

class RowObjectFactory(object):
    """
    Creates a row object using the specified schema.
    """
    def __init__(self, header):
        self.header = header

    def build(self, row):
        """
        Build a row using the specified schema.
        """
        obj = RowObject()
        for key, value in zip(self.header, row):
            setattr(obj, key, value)
        return obj

    @staticmethod
    def from_stream(stream):
        """
        Creates a stream of RowObjects from input stream.
        """

        header = next(stream)
        factory = RowObjectFactory(header)
        return map(factory.build, stream)

def make_one_hot(vec, n_classes):
    mat = np.zeros((len(vec), n_classes))
    for i, j in enumerate(vec):
        mat[i,j] = 1
    return mat

class WordVectorModel(dict):
    """
    A wrapper around a word vector model.
    """

    def __init__(self, wvecs, dim, preserve_case=False, unknown='*UNKNOWN*'):
        dict.__init__(self, wvecs)
        self.dim = dim
        self.preserve_case = preserve_case
        self.unknown = unknown

    def __getitem__(self, key):
        if not self.preserve_case:
            key = str.lower(key)
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return dict.__getitem__(self, self.unknown)

    def __setitem__(self, key, val):
        if not self.preserve_case:
            key = str.lower(key)
        return dict.__setitem__(self, key, val)

    @staticmethod
    def from_file(f, preserve_case, unknown):
        """
        Construct a word vector map from a file
        """
        log("Reading word vectors")
        wvecs = {}
        dim = None
        for line in f:
            parts = line.split()
            tok = parts[0]
            vec = array([float(x) for x in parts[1:]])
            if dim is None:
                dim = len(vec)
            assert dim == len(vec), "Incorrectly sized vector"
            wvecs[tok] = vec
        assert unknown in wvecs, "Unknown token not defined in word vectors"
        log("Done. Loaded {} vectors.", len(wvecs))
        return WordVectorModel(wvecs, dim, preserve_case, unknown)

    @staticmethod
    def from_filename(fname, preserve_case, unknown):
        """
        Construct a word vector map from a file
        """
        with open(fname) as f:
            return WordVectorModel.from_file(f, preserve_case, unknown)

    def embed_sentence(self, toks, max_length=50):
        """
        Return the list of tokens embedded as a matrix.
        """
        X = zeros((max_length, self.dim))
        for i, w in enumerate(toks[:max_length]):
            X[i, :] = self[w]
        return X

    def embed_sentences(self, sentences, max_length=50):
        """
        Return the list of tokens embedded as a matrix.
        """
        return array([[self.embed_sentence(toks, max_length)] for toks in sentences])


def test_wvec_model():
    """
    Test that the WordVectorModel handles case and unknowns correctly.
    """
    import os
    from numpy import allclose
    assert os.path.exists('./glove.6B.50d.txt'), "Can't find word vector file at"
    undiplomatically = array([-0.44594,-1.1723,0.058833,-0.99806,0.065609,0.059089,0.60732,1.2965,-0.32984,-0.045185,-0.30061,0.33055,-0.18897,0.82746,-0.28756,-0.31784,-0.091562,-0.42301,1.173,-0.65538,0.027537,0.1238,0.26689,0.39363,0.62385,0.847,1.0387,0.82124,-0.064256,0.043767,-0.97034,-0.4336,1.1662,0.24741,0.54262,0.58686,0.51069,0.67763,-0.78139,-0.21806,0.029529,0.11175,-0.43608,0.41791,-0.34094,-1.0393,0.64999,0.2285,-0.033636,0.23816])
    unk = array([-0.1292,-0.2887,-0.01225,-0.05677,-0.2021,-0.08389,0.3336,0.1605,0.03867,0.1783,0.04697,-0.002858,0.291,0.04614,-0.2092,-0.06613,-0.06822,0.07666,0.3134,0.1785,-0.1226,-0.09917,-0.07496,0.06413,0.1444,0.6089,0.1746,0.05335,-0.01274,0.03474,-0.8124,-0.04689,0.2019,0.2031,-0.03936,0.06968,-0.01554,-0.03405,-0.06528,0.1225,0.1399,-0.1745,-0.08012,0.08495,-0.01042,-0.137,0.2013,0.1007,0.00653,0.01685])

    model = WordVectorModel.from_file('./glove.6B.50d.txt', False, '*UNKNOWN*')
    assert allclose(undiplomatically, model['undiplomatically']), "Vectors are not equal!"
    assert allclose(undiplomatically, model['UndIplomAtically']), "Vectors are not equal!"
    assert allclose(unk, model['undiplomaticallyy']), "Vectors are not equal!"


def grouper(n, iterable):
    """
    grouper(3, 'ABCDEFG') --> 'ABC', 'DEF', 'G'
    """
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk

