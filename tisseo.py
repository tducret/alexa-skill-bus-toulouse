#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import environ
import json
import requests
from datetime import datetime
import pytz

_URL_TISSEO_API = "https://api.tisseo.fr/v1"
_TISSEO_API_KEY = environ['TISSEO_API_KEY']
if _TISSEO_API_KEY == "":
    raise KeyError("TISSEO_API_KEY environment variable must be set")

_DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
_TISSEO_TIMEZONE = 'Europe/Paris'
_AWS_LAMBDA_TIMEZONE = 'UTC'

# Load stop_areas JSON file (contains every stop areas with name and id)
with open("stop_areas.json") as f:
    full_dict = json.load(f)
    STOP_AREAS_DICT = full_dict.get("stopAreas").get("stopArea")


class Passage(object):
    def __init__(self, date, ligne, destination):
        self.date_str = date
        self.ligne = ligne
        self.destination = destination
        self.date_obj = _str_datetime_to_datetime_obj(self.date_str)
        self.timedelta = _get_timedelta(self.date_obj)
        self.timedelta_str = _timedelta_to_str(self.timedelta)

    def __str__(self):
        return "{} ({}) : {}".format(
            self.ligne, self.destination, self.date_str)


def _get(self, url, expected_status_code=200):
        ret = self.session.get(url=url, headers=self.headers)
        if (ret.status_code != expected_status_code):
            raise ConnectionError(
                'Status code {status} for url {url}\n{content}'.format(
                    status=ret.status_code, url=url, content=ret.text))


def get_stop_area_by_name(stop_area_name):
    stop_areas = []
    for stop_area in STOP_AREAS_DICT:
        if stop_area.get("name").lower() == stop_area_name.lower():
            stop_areas.append(stop_area)
    return stop_areas


def get_prochains_passages_for_stop_area_id(stop_area_id, limit=1,
                                            from_date=None):
    url = "{}/stops_schedules.json?stopAreaId={}&key={}&number={}".format(
        _URL_TISSEO_API, stop_area_id, _TISSEO_API_KEY, limit)
    if from_date is not None:
        url += "&datetime={}".format(from_date)

    ret = requests.get(url)

    if ret.status_code != 200:
        raise requests.ConnectionError("Status code {} for url {}".format(
            ret.status_code, url))

    j = json.loads(ret.text)
    return j.get("departures").get("departure")


def _str_datetime_to_datetime_obj(str_datetime,
                                  date_format=_DEFAULT_DATE_FORMAT):
    """ Check the expected format of the string date and returns a datetime
    object """
    try:
        datetime_obj = datetime.strptime(str_datetime, date_format)
    except:
        raise TypeError("date must match the format {}, received : {}".format(
            date_format, str_datetime))
    if datetime_obj.tzinfo is None:
        tz = pytz.timezone(_TISSEO_TIMEZONE)
        datetime_obj = tz.localize(datetime_obj)
    return datetime_obj


def _get_timedelta(date):
    now = datetime.now()
    if now.tzinfo is None:
        tz = pytz.timezone(_AWS_LAMBDA_TIMEZONE)
        now = tz.localize(now)
    return date - now


def _timedelta_to_str(time_delta):
    d = {"days": time_delta.days}
    d["hours"], rem = divmod(time_delta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    if d["days"] > 0:
        delta = "{} jours".format(d["days"])
    elif d["hours"] > 0:
        delta = "{} heures".format(d["hours"])
        if d["minutes"] > 0:
            delta += " et {} minutes".format(d["minutes"])
    elif d["minutes"] < 1:
        delta = "moins d'une minute"
    else:
        delta = "{} minutes".format(d["minutes"])
    return delta


def prochains_passages(stop_area_name):
    stop_areas = get_stop_area_by_name(stop_area_name)
    if len(stop_areas) < 1:
        raise KeyError("Arrêt {} inconnu".format(stop_area_name))
    elif len(stop_areas) > 1:
        print("Plusieurs arrêts trouvés pour {}".format(stop_area_name))

    stop_area_id = stop_areas[0].get("id")
    prochains_passages = get_prochains_passages_for_stop_area_id(stop_area_id)

    if len(prochains_passages) < 1:
        p = None
    else:
        prochain_passage = prochains_passages[0]
        date = prochain_passage.get("dateTime")
        ligne = prochain_passage.get("line").get("shortName")
        destination = prochain_passage.get("destination")[0].get("name")
        p = Passage(date=date, ligne=ligne, destination=destination)
    return p
