# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

"""
Domain specific language for DBpedia quepy.
"""

from quepy.dsl import FixedType, HasKeyword, FixedRelation, FixedDataRelation

# Setup the Keywords for this application
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
