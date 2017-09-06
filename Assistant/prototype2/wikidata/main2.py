#!/usr/bin/python3
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
from sparql_query import SPARQLQuery

def get_arguments(argparse):
    parser = argparse.ArgumentParser(description='Quepy prototype number 1')

    parser.add_argument("question", help='Question à poser sous la forme "question"')
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = get_arguments(argparse)

    query = SPARQLQuery.get_query(args.question)

    print(SPARQLQuery.execute_query(query))

    query = """SELECT DISTINCT ?x0Label WHERE{wd:Q37079 wdt:P106 ?x0.SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr". }}"""

    print(SPARQLQuery.execute_query(query))
