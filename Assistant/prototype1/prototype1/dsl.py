# coding: utf-8

"""
Domain specific language for prototype1 quepy.
"""

from quepy.dsl import FixedRelation

class IsDefinedIn(FixedRelation):
    relation = "rdfs:comment"
    reverse = True
