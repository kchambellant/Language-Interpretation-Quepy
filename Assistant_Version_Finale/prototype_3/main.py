#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Main script for prototype1 quepy.
"""

import quepy
import argparse
import sys
import time
import random
import datetime

from SPARQLWrapper import SPARQLWrapper, JSON, XML
from query_add.sparql_query import SPARQLQuery
import query_add.utils as utils
import query_add.data_settings as data_settings
import query_add.data as data
from googletrans import Translator

def get_arguments(argparse):
    parser = argparse.ArgumentParser(description='Quepy prototype number 1')

    parser.add_argument("question", help='Question à poser sous la forme "question"')
    args = parser.parse_args()

    return args

def translate_question(question):
    translator = Translator()
    question = translator.translate(question)

    return question.text

def handle_questions():
    question = ''

    while question != 'bye':
        question = raw_input("Quelle est votre requête ? (Si vous voulez quitter, tapez 'bye'.)\n")

        question = translate_question(question)

        if question != 'bye':
            print("-----------------\n")
            data_res, metadata = SPARQLQuery.get_data_from_question(question)

            if not data_res:
                print(metadata % question)
                continue

            uri_id = utils.get_id_of_uri(data_res)

            result = data.get_data_for_uri(uri_id, metadata)

            print(result)
            print("-----------------\n")

if __name__ == "__main__":
    handle_questions()
