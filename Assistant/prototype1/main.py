#!/usr/bin/env python
# coding: utf-8

import sys
import time
import random
import datetime
import argparse

import quepy
from SPARQLWrapper import SPARQLWrapper, JSON

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Quepy prototype number 1')

    parser.add_argument("question", help='Question à poser sous la forme "question"')
    args = parser.parse_args()


    prototype1 = quepy.install("dbpedia")
    target, query, metadata = prototype1.get_query(args.question)
    print query
