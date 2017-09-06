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

if __name__ == "__main__":
    args = get_arguments(argparse)

    translator = Translator()
    question_trans = translator.translate(args.question)
    data, metadata = SPARQLQuery.get_data_from_question(question_trans.text)
    uri_id = utils.get_id_of_uri(data)

    result = data_settings.metaMap[metadata](uri_id, metadata)

    print(result)
