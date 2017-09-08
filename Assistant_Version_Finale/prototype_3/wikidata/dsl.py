#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Domain specific language.
"""

from quepy.dsl import FixedType, HasKeyword, FixedRelation, FixedDataRelation

HasKeyword.relation = "rdfs:label"
HasKeyword.language = "en"

class CategoryOf(FixedDataRelation):
    relation = "wdt:P373"
    reverse = True

class DefinitionOf(FixedDataRelation):
    relation = "wdt:P31"
    reverse = True

class ToGenerate(FixedRelation):
    relation = "ToGenerate"
    reverse = True
