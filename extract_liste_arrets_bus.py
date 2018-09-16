#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Extrait la liste des arrêts de bus
pour configurer le slot_type liste_arrets_bus """

import json

# Load stop_areas JSON file (contains every stop areas with name and id)
with open("stop_areas.json") as f:
    full_dict = json.load(f)
    STOP_AREAS_DICT = full_dict.get("stopAreas").get("stopArea")

liste_stop_areas = []
for stop_area in STOP_AREAS_DICT:
    liste_stop_areas.append(stop_area.get("name").lower())

# Remove duplicates
liste_stop_areas = list(set(liste_stop_areas))

for stop_area in liste_stop_areas:
    print("{},".format(stop_area))
