#!/usr/bin/python
# -*- coding: utf-8 -*-

def who_is(data):
    str = ""
    if data.has_key("metier"):
        if type(data["metier"]) == list:
            data["metier"] = ", ".join(data["metier"])
            str_metier = "exerce les professions:"
        else:
            str_metier = "exerce la profession:"
    else:
        str_metier = ""
        data["metier"] = ""
    if data.has_key("genre"):
        if data["genre"] == "masculin":
            str = "%s %s %s. Il est ne le %s dans le pays: %s" %(data["nom"], str_metier, data["metier"], data["age"], data["nation"])
        elif "feminin":
            str = "%s %s %s. Elle est nee le %s dans le pays: %s" %(data["nom"], str_metier, data["metier"], data["age"], data["nation"])
    return str
