# -*- coding: utf-8 -*-
"""
Various utilities for interfacing with Twitter
"""

import os
import csv
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
        if keyword in text:
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

