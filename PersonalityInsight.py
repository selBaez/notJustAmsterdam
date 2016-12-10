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
    with open(os.path.join(os.path.dirname(__file__), './resources/challenges.json')) as challenges:
        dilemma = tradeoff_analytics.dilemmas(json.load(challenges), generate_visualization=True)

    #print(json.dumps(dilemma, indent=2))

    potential_challenges = {}

    return potential_challenges
