# coding: utf-8

"""
Basic queries for prototype1 quepy.
"""

from refo import Group, Question, Plus
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate
from dsl import IsDefinedIn, IsLocatedIn, LabelOf, IsPlace, UTCof

class Thing(Particle):
    regex = Question(Pos("JJ")) + (Pos("NN") | Pos("NNP") | Pos("NNS")) |\
            Pos("VBN")

    def interpret(self, match):
        return HasKeyword(match.words.tokens)

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
    Questions du type "Where is smthg?"
    ex: "Where is the Big Ben?"
    """

    target = Group(Plus(Pos("NNP") | Pos("NNPS")), "target")
    regex = Lemma("where") + Lemma("be") + Question(Pos("DT")) + target + Question(Pos("."))
    #A modifier un peu pour éviter des problèmes comme avec "Where is Big Ben?"

    def interpret(self, match):
        target = HasKeyword(match.target.tokens)
        location = IsLocatedIn(target)
        definition = LabelOf(location)
        return definition

class WhatTime(QuestionTemplate):
    """
    Regex pour une question du type 'What time is it in ...'
    Ex : 'What time is it in Paris'
    """

    target = Question(Pos("DT")) + Group(Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS")), "target")
    regex = Lemma("what") + Lemma("time") + Lemma("be") + Question(Pos("PRP")) + Question(Pos("IN")) + target + Question(Pos("."))

    def interpret(self, match):
        place = HasKeyword(match.target.lemmas.title()) + IsPlace()
        utc_offset = UTCof(place)
        return utc_offset, "time"
