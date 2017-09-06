#!/usr/bin/python2.7
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
    def get_data_from_question(cls, question):
        target, query, metadata = cls._quepy_query.get_query(question)

        if not query:
            return None, "Il n'est pas possible de traiter la question suivante : '%s'."

        query, target = cls.query_change(query, target)

        return cls.execute_query(query, metadata)

    @classmethod
    def execute_query(cls, query, metadata=False):
        cls._sparql.setQuery(query)
        cls._sparql.setReturnFormat(JSON)

        results = cls._sparql.query().convert()

        data = cls.get_data(results)

        if not data:
            return None, "Aucun résultat n'a été trouvé pour la question suivante : '%s'."

        if not metadata:
            return data
        else:
            return data, metadata

    @staticmethod
    def create_query(uri_id, field):
        query = "SELECT DISTINCT ?x0Label WHERE{\n wd:"+uri_id+" "+field+" ?x0\n"+ 'SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr". }'+"\n}\n"

        data = SPARQLQuery.execute_query(query)

        return data

    @staticmethod
    def get_data(results):
        data = []

        head = results['head']['vars']

        for result in results['results']['bindings']:
            if len(head) == 1:
                temp = result[head[0]]['value']
            else:
                temp = {}

                for key in head:
                    temp[key] = result[key]['value']

            data.append(temp)

        if len(data) == 1:
            return data[0]

        return data
