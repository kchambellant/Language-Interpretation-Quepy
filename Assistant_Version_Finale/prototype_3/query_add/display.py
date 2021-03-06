#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import date

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
        annee, mois, jour = data["age"].split('-')

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

def how_old_is(data):
    if data['death'][0] is None:
        data['death'] = date.today().isoformat()
        str= "%s a "%data['nom']
    else:
        data["death"] = data["death"].replace("T00:00:00Z","")
        str= "%s est mort lorsqu'il avait  "%data['nom']
    data["birth"] = data["birth"].replace("T00:00:00Z","")
    annee_birth, mois_birth, jour_birth = data["birth"].split('-')
    annee_death, mois_death, jour_death = data["death"].split('-')
    age=int(annee_death) - int(annee_birth) - ((int(mois_death), int(jour_death))<(int(mois_birth), int(jour_birth)))
    str += "%s ans"%age
    return str

def population_of_question(data):
    def intWithCommas(x):
        if type(x) not in [type(0), type(0L)]:
            raise TypeError("Parameter must be an integer.")
        if x < 0:
            return '-' + intWithCommas(-x)
        result = ''
        while x >= 1000:
            x, r = divmod(x, 1000)
            result = ",%03d%s" % (r, result)
        return "%d%s" % (x, result)

    population = intWithCommas(int(data['population']))

    str = '%s personnes vivent dans le pays %s' % (population, data['nom'])

    return str

def president_of_question(data):
    str_res = "Le chef d'état du pays %s est %s." % (str(data['nom']), str(data['president']))

    return str_res

def language_of_question(data):
    str_res = 'Le pays %s a comme ' % str(data['nom'])

    if type(data['language']) is list:
        languages = ', '.join(data['language'])

        str_res += 'langues officielles : %s.' % languages
    else:
        str_res += 'langue officielle : %s.' % data['language']

    return str_res
