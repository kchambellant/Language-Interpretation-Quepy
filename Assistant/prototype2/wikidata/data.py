#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import data_settings
from sparql_query import SPARQLQuery

def whois(uri_id, metadata):
    data = {}

    fieldsMap = data_settings.fieldsMap[metadata]

    for field in fieldsMap:
        data[field] = SPARQLQuery.create_query(uri_id, fieldsMap[field])

    display.whois(data)
