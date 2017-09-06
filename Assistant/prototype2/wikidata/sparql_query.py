#!/usr/bin/python3
# -*- coding: utf-8 -*-

import quepy
from SPARQLWrapper import SPARQLWrapper, JSON

class SPARQLQuery(object):
    _quepy_query = quepy.install("wikidata")
    _sparql = SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql")

    @staticmethod
    def query_change(query, target):
        query = query.replace(target, "?x0", 1).replace("?x0 ToGenerate ?x1.", "", 1)
        target = "?x0"

        return query, target

    @classmethod
    def get_query(cls, question):
        target, query, metadata = cls._quepy_query.get_query(question)

        query, target = cls.query_change(query, target)

        return query

    @classmethod
    def execute_query(cls, query):
        cls._sparql.setQuery(query)
        cls._sparql.setReturnFormat(JSON)

        results = cls._sparql.query().convert()

        data = cls.get_data(results)

        return data

    @staticmethod
    def get_data(results):
        data = []

        head = results['head']['vars']

        for result in results['results']['bindings']:
            dataDict = {}

            for key in head:
                dataDict[key] = result[key]['value']

            data.append(dataDict)

        return data
