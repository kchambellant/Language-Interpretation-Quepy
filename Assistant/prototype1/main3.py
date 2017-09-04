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

from SPARQLWrapper import SPARQLWrapper, JSON

def print_define(results, target, metadata=None):
    for result in results["results"]["bindings"]:
        if result[target]["xml:lang"] == "en":
            print result[target]["value"]
            print

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Quepy prototype number 1')

    prototype1 = quepy.install("dbpedia")
    question = ""
    while question != "bye" :
        question = raw_input("Quelle est votre requête ? (Si vous voulez quitter, tapez 'bye'.)\n")
        if question != "bye" :
            target, query, metadata = prototype1.get_query(question)
            print query

            sparql = SPARQLWrapper("http://dbpedia.org/sparql")
            if target.startswith("?"):
                target = target[1:]
                if query:
                    sparql.setQuery(query)
                    sparql.setReturnFormat(JSON)
                    results = sparql.query().convert()

            print("print_define :")
            print_define(results, target, metadata)
    
