#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Extrait la liste des destinations (ou terminus)
pour configurer le slot_type liste_destinations """

import json

with open("lines.json") as f:
    full_dict = json.load(f)
    LINES_DICT = full_dict.get("lines").get("line")

liste_lignes = []
for line in LINES_DICT:
    liste_lignes.append(line.get("shortName"))

# Remove duplicates
liste_lignes = list(set(liste_lignes))

for ligne in liste_lignes:
    print("{},".format(ligne))
