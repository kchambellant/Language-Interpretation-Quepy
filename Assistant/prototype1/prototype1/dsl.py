# coding: utf-8

"""
Domain specific language for prototype1 quepy.
"""

from quepy.dsl import FixedRelation

class IsDefinedIn(FixedRelation):
    relation = "rdfs:comment"
    reverse = True

class IsLocatedIn(FixedRelation):
    relation = "rdfs:location"
    reverse = True

class LabelOf(FixedRelation):
    relation = "rdfs:label"
    reverse = True
