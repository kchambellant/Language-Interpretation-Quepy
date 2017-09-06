#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def get_id_of_uri(uri):
    id_uri = uri.replace("http://www.wikidata.org/entity/","")

    return id_uri
