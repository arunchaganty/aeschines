#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Useful utilities
"""

import csv

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
        ('8-D'   , '😁'),
        ('8D'    , '😁'),
        (':-D'   , '😁'),
        ('=-3'   , '😁'),
        ('=-D'   , '😁'),
        ('=3'    , '😁'),
        ('=D'    , '😁'),
        ('B^D'   , '😁'),
        ('X-D'   , '😁'),
        ('XD'    , '😁'),
        ('x-D'   , '😁'),
        ('xD'    , '😁'),
        (':\')'  , '😂'),
        (':\'-)' , '😂'),
        (':-))'  , '😃'),
        ('8)'    , '😄'),
        (':)'    , '😄'),
        (':-)'   , '😄'),
        (':3'    , '😄'),
        (':D'    , '😄'),
        (':]'    , '😄'),
        (':^)'   , '😄'),
        (':c)'   , '😄'),
        (':o)'   , '😄'),
        (':}'    , '😄'),
        (':っ)'  , '😄)',
        ('=)'    , '😄'),
        ('=]'    , '😄'),
        ('0:)'   , '😇'),
        ('0:-)'  , '😇'),
        ('0:-3'  , '😇'),
        ('0:3'   , '😇'),
        ('0;^)'  , '😇'),
        ('O:-)'  , '😇'),
        ('3:)'   , '😈'),
        ('3:-)'  , '😈'),
        ('}:)'   , '😈'),
        ('}:-)'  , '😈'),
        ('*)'    , '😉'),
        ('*-)'   , '😉'),
        (':-,'   , '😉'),
        (';)'    , '😉'),
        (';-)'   , '😉'),
        (';-]'   , '😉'),
        (';D'    , '😉'),
        (';]'    , '😉'),
        (';^)'   , '😉'),
        (':-|'   , '😐'),
        (':|'    , '😐'),
        (':('    , '😒'),
        (':-('   , '😒'),
        (':-<'   , '😒'),
        (':-['   , '😒'),
        (':-c'   , '😒'),
        (':<'    , '😒'),
        (':['    , '😒'),
        (':c'    , '😒'),
        (':{'    , '😒'),
        (':っC'  , '😒)',
        ('%)'    , '😖'),
        ('%-)'   , '😖'),
        (':-P'   , '😜'),
        (':-b'   , '😜'),
        (':-p'   , '😜'),
        (':-Þ'   , '😜'),
        (':-þ'   , '😜'),
        (':P'    , '😜'),
        (':b'    , '😜'),
        (':p'    , '😜'),
        (':Þ'    , '😜'),
        (':þ'    , '😜'),
        (';('    , '😜'),
        ('=p'    , '😜'),
        ('X-P'   , '😜'),
        ('XP'    , '😜'),
        ('d:'    , '😜'),
        ('x-p'   , '😜'),
        ('xp'    , '😜'),
        (':-||'  , '😠'),
        (':@'    , '😠'),
        (':-.'   , '😡'),
        (':-/'   , '😡'),
        (':/'    , '😡'),
        (':L'    , '😡'),
        (':S'    , '😡'),
        (':\\'   , '😡'),
        ('=/'    , '😡'),
        ('=L'    , '😡'),
        ('=\\'   , '😡'),
        (':\'('  , '😢'),
        (':\'-(' , '😢'),
        ('^5'    , '😤'),
        ('^<_<'  , '😤'),
        ('o/\\o' , '😤'),
        ('|-O'   , '😫'),
        ('|;-)'  , '😫'),
        (':###..', '😰'),
        (':-###.., '😰'),
        ('D-\':' , '😱'),
        ('D8'    , '😱'),
        ('D:'    , '😱'),
        ('D:<'   , '😱'),
        ('D;'    , '😱'),
        ('D='    , '😱'),
        ('DX'    , '😱'),
        ('v.v'   , '😱'),
        ('8-0'   , '😲'),
        (':-O'   , '😲'),
        (':-o'   , '😲'),
        (':O'    , '😲'),
        (':o'    , '😲'),
        ('O-O'   , '😲'),
        ('O_O'   , '😲'),
        ('O_o'   , '😲'),
        ('o-o'   , '😲'),
        ('o_O'   , '😲'),
        ('o_o'   , '😲'),
        (':$'    , '😳'),
        ('#-)'   , '😵'),
        (':#'    , '😶'),
        (':&'    , '😶'),
        (':-#'   , '😶'),
        (':-&'   , '😶'),
        (':-X'   , '😶'),
        (':X'    , '😶'),
        (':-J'   , '😼'),
        (':*'    , '😽'),
        (':^*'   , '😽'),
        ('ಠ_ಠ'   , '🙅'),
        ('*\\0/*', '🙆'),
        ('\\o/'  , '🙆'),
        (':>'    , '😄'),
        ('>.<'   , '😡'),
        ('>:('   , '😠'),
        ('>:)'   , '😈'),
        ('>:-)'  , '😈'),
        ('>:/'   , '😡'),
        ('>:O'   , '😲'),
        ('>:P'   , '😜'),
        ('>:['   , '😒'),
        ('>:\\'  , '😡'),
        ('>;)'   , '😈'),
        ('>_>^'  , '😤'),
    ]

def to_ascii(text):
    # Convert from ascii
    for asci, unicod in UNICODE_EMOJI_TO_ASCII_TABLE:
        text = text.replace(unicod, asci)
    return text.decode('ascii', errors='ignore').encode('ascii', errors='ignore')


def ordc(c):
    """
    Compressed version of ord that returns indices between -1 and 95.
    """
    c = ord(c)
    if c < 32 or c > 126: return -1
    else return c - 32

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

