# coding: utf-8

"""
Basic queries for prototype1 quepy.
"""

from refo import Group, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate
from dsl import IsDefinedIn

class WhatIs(QuestionTemplate):
    """"""

    target = Question(Pos("DT")) + Group(Pos("NN"), "target")
    regex = Lemma("what") + Lemma("be") + target + Question(Pos("."))

    def interpret(self, match):
        target = HasKeyword(match.target.tokens)
        definition = IsDefinedIn(target)
        return definition
