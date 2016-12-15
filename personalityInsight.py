# Code for using personality insights
# By Selene Baez

import json, os
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    username='0bf8ad43-d450-485d-b3ef-8bbaae557eea',
    password='qGyVxGBapbPb')

def analyze(profile):
    with open(os.path.join(os.path.dirname(__file__), './resources/personality-v3.json')) as data_json:
        analysis = personality_insights.profile(data_json.read(), content_type='application/json', raw_scores=True, consumption_preferences=True)

    print(json.dumps(profile, indent=2))

    personality = {}

    return personality

x = analyze(1)
