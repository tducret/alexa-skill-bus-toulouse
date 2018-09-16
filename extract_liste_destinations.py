#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Extrait la liste des destinations (ou terminus)
pour configurer le slot_type liste_destinations """

import json

with open("lines.json") as f:
    full_dict = json.load(f)
    LINES_DICT = full_dict.get("lines").get("line")

liste_destinations = []
for line in LINES_DICT:
    if line.get("terminus") is not None:
        for terminus in line.get("terminus"):
            liste_destinations.append(terminus.get("name").lower())

# Remove duplicates
liste_destinations = list(set(liste_destinations))

for destination in liste_destinations:
    print("{},".format(destination))
