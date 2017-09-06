#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import data_settings
from sparql_query import SPARQLQuery
import display

def whois(uri_id, metadata):
    data = {}

    fieldsMap = data_settings.fieldsMap[metadata]

    for field in fieldsMap:
        data[field] = SPARQLQuery.create_query(uri_id, fieldsMap[field])

    return display.who_is(data)

def capital(uri_id, metadata):
    data = {}

    fieldsMap = data_settings.fieldsMap[metadata]

    for field in fieldsMap:
        data[field] = SPARQLQuery.create_query(uri_id, fieldsMap[field])

    return display.capital(data)

def howoldis(uri_id, metadata):
    data = {}

    fieldsMap = data_settings.fieldsMap[metadata]

    for field in fieldsMap:
        data[field] = SPARQLQuery.create_query(uri_id, fieldsMap[field])

    return display.howoldis(data)
