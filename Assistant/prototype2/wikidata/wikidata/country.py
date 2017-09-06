#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Country related regex
"""

from refo import Plus, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dsl import DefinitionOf, CategoryOf, ToGenerate


class Country(Particle):
    regex = Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS") | Pos("DT"))

    def interpret(self, match):
        name = match.words.tokens
        return CategoryOf(name) + DefinitionOf(u"wd:Q6256")


class CapitalOf(QuestionTemplate):
    """
    Ex: "What is the capital of France?"
    """

    regex = Lemma("what") + Lemma("be") + Pos("DT") + Lemma("capital") + Pos("IN") + Country() + Question(Pos("."))

    def interpret(self, match):
        definition = ToGenerate(match.country)
        return definition, "capital"
