#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import display

displayMap = {
    'whois': display.who_is,
    'capital': display.capital,
    'howoldis': display.how_old_is,
    'populationofquestion': display.population_of_question,
    'presidentofquestion': display.president_of_question,
    'languageofquestion': display.language_of_question
}

fieldsMap = {
    'whois': {
        'nom': 'wdt:P373',
        'age': 'wdt:P569',
        'nation': 'wdt:P27',
        'genre': 'wdt:P21',
        'metier': 'wdt:P106'
    },
    'capital': {
        'nom': 'wdt:P17',
        'capital': 'wdt:P36'
    },
    'howoldis': {
        'nom': 'wdt:P373',
        'birth': 'wdt:P569',
        'death': 'wdt:P570'
    },
    'populationofquestion': {
        'nom': 'wdt:P17',
        'population': 'wdt:P1082'
    },
    'presidentofquestion': {
        'nom': 'wdt:P17',
        'president': 'wdt:P35'
    },
    'languageofquestion': {
        'nom': 'wdt:P17',
        'language': 'wdt:P37'
    }
}
