# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from terms import Terms


class TermsAndDefinitions(Action):

    def name(self) -> Text:
        return "action_term_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        term = tracker.latest_message['text']
        definition = str(Terms(term))
        if definition:
            dispatcher.utter_template("utter_definition", tracker, term = term, definition = definition)
        else:
            dispatcher.utter_template("utter_no_term", tracker, term = term)

        return []

