#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import data

metaMap = {
    'whois': data.whois,
    'capital': data.capital
}

fieldsMap = {
    'whois': {
        'nom': 'wdt:P373',
        'age': 'wdt:P569',
        'nation': 'wdt:P27',
        'genre': 'wdt:P21',
        'metier': 'wdt:P106'
    },
    'capital':{
        'nom': 'wdt:P17',
        'capital': "wdt:P36"
    }
}
