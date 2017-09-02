# coding: utf-8

"""
Basic queries for prototype1 quepy.
"""

from refo import Group, Question, Plus
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate
from dsl import IsDefinedIn, IsLocatedIn, LabelOf

class WhatIs(QuestionTemplate):
    """
    Questions du type "What is smthg?"
    ex: "What is an apple?"
    """

    target = Question(Pos("DT")) + Group(Plus(Pos("NN") | Pos("JJ")), "target")
    regex = Lemma("what") + Lemma("be") + target + Question(Pos("."))

    def interpret(self, match):
        target = HasKeyword(match.target.tokens)
        definition = IsDefinedIn(target)
        return definition

class WhereIs(QuestionTemplate):
    """
    Questions du type "Where is the Big Ben?"
    """

    target = Group(Plus(Pos("NNP") | Pos("NNPS")), "target")
    regex = Lemma("where") + Lemma("be") + Question(Pos("DT")) + target + Question(Pos("."))

    def interpret(self, match):
        target = HasKeyword(match.target.tokens)
        location = IsLocatedIn(target)
        definition = LabelOf(location)
        return definition
