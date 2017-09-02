# coding: utf-8

"""
Main script for prototype1 quepy.
"""

import quepy
import argparse
parser = argparse.ArgumentParser(description='Quepy prototype number 1')

parser.add_argument("question", help='Question à poser sous la forme "question"')
args = parser.parse_args()


prototype1 = quepy.install("prototype1")
target, query, metadata = prototype1.get_query(args.question)
print query
