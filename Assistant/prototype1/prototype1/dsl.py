# coding: utf-8

"""
Domain specific language for prototype1 quepy.
"""

from quepy.dsl import FixedRelation, FixedType

class IsDefinedIn(FixedRelation):
    relation = "rdfs:comment"
    reverse = True

class IsLocatedIn(FixedRelation):
    relation = "rdfs:location"
    reverse = True

class LabelOf(FixedRelation):
    relation = "rdfs:label"
    reverse = True

class IsPlace(FixedType):
    fixedtype = "dbpedia:Place"

class UTCof(FixedRelation):
    relation = "rdfs:utc"
    reverse = True
