# coding: utf-8

"""
Main script for prototype1 quepy.
"""

import quepy
prototype1 = quepy.install("prototype1")
target, query, metadata = prototype1.get_query("where is the Big Ben?")
print query
