#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

def who_is(data):
    if data.has_key("age"):
        data["age"] = data["age"].replace("T00:00:00Z","")
        data["age"] = datetime.strptime(data["age"], '%Y-%m-%d').strftime('%d/%m/%y')
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
