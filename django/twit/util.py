# -*- coding: utf-8 -*-
"""
Various utilities for interfacing with Twitter
"""

import os
import csv
import gc
import re
from collections import Counter

def identify_issues(text):
    """
    Identify any issues mentioned in a span of text according to a simple lexicon.

    @text:str
    @returns:Counter - containing counts of how many issues occur in each tweet.
    """
    issues = {
        "Free Trade": "free trade|trade",
        "Energy & Oil": "energy|oil",
        "Jobs": "jobs",
        "Environment": "environment",
        "Corporations": "corporations",
        "Tax Reform": "tax|taxes|tax reform",
        "Government Reform": "government reform",
        "Infrastructure & Technology": "infrastructure|technology",
        "Education": "education",
        "Health Care": "health care|healthcare|obamacare",
        "Civil Rights": "civil rights|equal rights",
        "Families & Children": "families|children",
        "Religion": "religion",
        "Criminal Justice": "criminal justice",
        "Gun Control": "gun control|gun|guns",
        "Welfare & Poverty": "welfare|poverty",
        "Crime": "crime",
        "Drugs": "drugs",
        "Immigration": "immigration|border patrol|border",
        "Foreign policy": "foreign policy",
        "War & Peace": "war|peace",
        "Homeland Security": "homeland security|dhs",
    }

    counts = Counter()
    for issue, regex in issues.items():
        if re.search(regex, text) is not None:
            counts[issue] += 1
    return counts

def identify_stance(text):
    """
    Identify stance using keywords
    """
    score = Counter()
    total = 0
    for keyword, candidate, stance in STANCE_KEYWORDS:
        if keyword.lower() in text.lower():
            total = 0
            score[candidate] += float(stance)
    if total > 0:
        for key in score:
            score[key] /= total

    return score

def __init_stance(fname=os.path.join(os.path.dirname(__file__),'data','stance_seeds.txt')):
    """
    Initialize the stance keyword list
    """
    with open(fname) as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ["keyword", "candidate", "stance"]
        return list(reader)

STANCE_KEYWORDS = __init_stance()


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

def queryset_iterator(queryset, chunksize=1000):
    '''''
    Iterate over a Django Queryset ordered by the primary key

    This method loads a maximum of chunksize (default: 1000) rows in it's
    memory at the same time while django normally would load all rows in it's
    memory. Using the iterator() method only causes it to not preload all the
    classes.

    Note that the implementation of the iterator does not support ordered query sets.
    '''
    pk = 0
    last_pk = queryset.order_by('-pk')[0].pk
    queryset = queryset.order_by('pk')
    while pk < last_pk:
        for row in queryset.filter(pk__gt=pk)[:chunksize]:
            pk = row.pk
            yield row
        gc.collect()
