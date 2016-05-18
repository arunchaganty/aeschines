# -*- coding: utf-8 -*-
"""
Various utilities for interfacing with Twitter
"""

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
