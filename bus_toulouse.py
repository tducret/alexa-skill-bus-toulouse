#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard
from os import environ
from tisseo import prochains_passages

from six import PY2
try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser


################################################

class SSMLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.full_str_list = []
        if not PY2:
            self.strict = False
            self.convert_charrefs = True

    def handle_data(self, d):
        self.full_str_list.append(d)

    def get_data(self):
        return ''.join(self.full_str_list)

################################################

_TISSEO_API_KEY = environ['TISSEO_API_KEY']
if _TISSEO_API_KEY == "":
    raise KeyError("TISSEO_API_KEY environment variable must be set")

skill_name = "Bus Toulouse"
help_text = ("Vous pouvez demander : "
             "Quand passe le prochain bus à l'arrêt Moulin Armand ?")

arret_bus_slot = "arret_bus"

sb = SkillBuilder()


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    # Handler for Skill Launch
    speech = "Bienvenue dans la skill des bus de Toulouse."

    handler_input.response_builder.speak(
        speech + " " + help_text).ask(help_text)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    # Handler for Help Intent
    handler_input.response_builder.speak(help_text).ask(help_text)
    return handler_input.response_builder.response


@sb.request_handler(
    can_handle_func=lambda input:
        is_intent_name("AMAZON.CancelIntent")(input) or
        is_intent_name("AMAZON.StopIntent")(input))
def cancel_and_stop_intent_handler(handler_input):
    # Single handler for Cancel and Stop Intent
    speech_text = "Au revoir!"

    return handler_input.response_builder.speak(speech_text).response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    # Handler for Session End
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name(
    "demande_des_prochains_passages_a_un_arret"))
def demande_des_prochains_passages_a_un_arret(handler_input):
    slots = handler_input.request_envelope.request.intent.slots

    if arret_bus_slot in slots:
        arret_bus_demande = slots[arret_bus_slot].value
        liste_p = prochains_passages(arret_bus_demande)

        speech = "A l'arrêt {}, ".format(arret_bus_demande)
        for p in liste_p:
            if p is None:
                speech = "Dans les prochaines heures, \
aucun passage prévu à l'arrêt {}.".format(arret_bus_demande)
            else:
                if p.ligne == "A":
                    speech += "Le métro ligne {},".format(p.ligne)
                if p.ligne == "B":
                    speech += "Le métro ligne {}".format(p.ligne)
                    # No comma here because it is pronounced "Bi" and not "Bé"
                elif p.ligne in ["T1", "T2"]:
                    speech += "Le tramway {},".format(p.ligne)
                else:
                    speech += "Le bus {},".format(p.ligne)

                speech += " à destination de {}, passera dans {}. ".format(
                    p.destination, p.timedelta_str)
    else:
        speech = "Je ne suis pas sûr de comprendre le nom de l'arrêt de bus."

    handler_input.response_builder.speak(speech)
    return handler_input.response_builder.response


def convert_speech_to_text(ssml_speech):
    # convert ssml speech to text, by removing html tags
    s = SSMLStripper()
    s.feed(ssml_speech)
    return s.get_data()


@sb.global_response_interceptor()
def add_card(handler_input, response):
    # Add a card by translating ssml text to card content
    response.card = SimpleCard(
        title=skill_name,
        content=convert_speech_to_text(response.output_speech.ssml))


@sb.global_response_interceptor()
def log_response(handler_input, response):
    # Log response from alexa service
    print("Alexa Response: {}\n".format(response))


@sb.global_request_interceptor()
def log_request(handler_input):
    # Log request to alexa service
    print("Alexa Request: {}\n".format(handler_input.request_envelope.request))


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    # Catch all exception handler, log exception and
    # respond with custom message
    print("Encountered following exception: {}".format(exception))

    speech = "Désolé, je n'ai pas compris. \
Dite aide pour obtenir des exemples d'utilisation."
    handler_input.response_builder.speak(speech).ask(speech)

    return handler_input.response_builder.response


# Handler to be provided in lambda console.
handler = sb.lambda_handler()
