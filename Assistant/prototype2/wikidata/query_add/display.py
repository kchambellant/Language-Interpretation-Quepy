#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

def who_is(data):
    if data.has_key("age"):
        mois_label={
            1: 'Janvier',
            2: 'Fevrier',
            3: 'Mars',
            4: 'Avril',
            5: 'Mai',
            6: 'Juin',
            7: 'Juillet',
            8: 'Aout',
            9: 'Septembre',
            10: 'Octobre',
            11: 'Novembre',
            12: 'Decembre'
            }
        data["age"] = data["age"].replace("T00:00:00Z","")
        annee = data["age"][:4]
        mois = data["age"][5:7]
        jour = data["age"][8:10]
        data["age"] = jour + " " +mois_label[int(mois)] + " " + annee
    str = ""
    if data.has_key("metier"):
        if type(data["metier"]) == list:
            data["metier"] = ", ".join(data["metier"][:3])
            str_metier = "exerce les professions:"
        else:
            str_metier = "exerce la profession:"
    else:
        str_metier = ""
        data["metier"] = ""
    if data.has_key("genre"):
        if data["genre"] == "masculin":
            str = u"%s %s %s. Il est n\xe9 le %s dans le pays: %s" %(data["nom"], str_metier, data["metier"], data["age"], data["nation"])
        elif "feminin":
            str = u"%s %s %s. Elle est n\xe9e le %s dans le pays: %s" %(data["nom"], str_metier, data["metier"], data["age"], data["nation"])
    return str

def capital(data):
    if data.has_key("nom"):
        if type(data["nom"]) == list:
            data["nom"] = data["nom"][0]
    str="La capital de %s est %s" %(data["nom"], data["capital"])
    return str
