# coding: utf-8

"""
Main script for prototype1 quepy.
"""

import quepy
import argparse
from SPARQLWrapper import SPARQLWrapper, JSON

parser = argparse.ArgumentParser(description='Quepy prototype number 1')

parser.add_argument("question", help='Question à poser sous la forme "question"')
args = parser.parse_args()


prototype1 = quepy.install("prototype1")
target, query, metadata = prototype1.get_query(args.question)
print query

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery(str(query))
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["label"]["value"])
