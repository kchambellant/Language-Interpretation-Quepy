# coding: utf-8

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

def print_define(results, target, metadata=None):
    for result in results["results"]["bindings"]:
        print result[target]["value"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Quepy prototype number 1')

    parser.add_argument("question", help='Question à poser sous la forme "question"')
    args = parser.parse_args()


    prototype1 = quepy.install("wikidata")
    target, query, metadata = prototype1.get_query(args.question)

    query = query.replace(target, "?x0", 1).replace("?x0 ToGenerate ?x1.", "", 1)
    target = "?x0"
    query = query[:-2]+'SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr". }'+"\n}\n"
    print query
    sparql = SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql")
    if target.startswith("?"):
        target = target[1:]
        if query:
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            #print(sparql.query().info())
            results = sparql.query().convert()

    print("print_define :")
    print_define(results, target, metadata)
