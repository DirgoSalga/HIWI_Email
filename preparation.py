# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:36:37 2017

@author:Dirgo
"""


def table_template(perfect_scores, keylist):
    """
    Creates a table that can be formatted to the results of each students.
    :param perfect_scores: <pandas series> containing all perfect scores.
    :param keylist: <list> of strings containing column names.
    :return: <str> formatable table.
    """
    table_str = ""
    for key in keylist:
        table_str += "{key}: {{{key}}} / {score}\n\n".format(key=key, score=perfect_scores[key])
    return table_str.strip()
