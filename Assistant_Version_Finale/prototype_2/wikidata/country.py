#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Country related regex
"""

from refo import Plus, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate, Token, Particle
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

class PopulationOfQuestion(QuestionTemplate):
    """
    Regex for questions about the population of a country.
    Ex: "What is the population of China?"
        "How many people live in China?"
    """

    openings = (Pos("WP") + Token("is") + Pos("DT") +
                Lemma("population") + Pos("IN")) | \
               (Pos("WRB") + Lemma("many") + Lemma("people") +
                Token("live") + Pos("IN"))
    regex = openings + Question(Pos("DT")) + Country() + Question(Pos("."))

    def interpret(self, match):
        definition = ToGenerate(match.country)
        return definition, "populationofquestion"

class PresidentOfQuestion(QuestionTemplate):
    """
    Regex for questions about the president of a country.
    Ex: "Who is the president of Argentina?"
    """

    regex = Pos("WP") + Token("is") + Question(Pos("DT")) + \
        Lemma("president") + Pos("IN") + Country() + Question(Pos("."))

    def interpret(self, match):
        definition = ToGenerate(match.country)
        return definition, "presidentofquestion"

class LanguageOfQuestion(QuestionTemplate):
    """
    Regex for questions about the language spoken in a country.
    Ex: "What is the language of Argentina?"
        "what language is spoken in Argentina?"
    """

    openings = (Lemma("what") + Token("is") + Pos("DT") +
                Question(Lemma("official")) + Lemma("language")) | \
               (Lemma("what") + Lemma("language") + Token("is") +
                Lemma("speak"))

    regex = openings + Pos("IN") + Question(Pos("DT")) + Country() + \
        Question(Pos("."))

    def interpret(self, match):
        definition = ToGenerate(match.country)
        return definition, "languageofquestion"
