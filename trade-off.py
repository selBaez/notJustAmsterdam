# Code for using trade off analytics
# By Selene Baez

import json, os
from os.path import join, dirname
from watson_developer_cloud import TradeoffAnalyticsV1

tradeoff_analytics = TradeoffAnalyticsV1(
    username='56b3ccff-47df-4717-80cd-dcd290633175',
    password='xiA6ByCxCtxD')

with open(os.path.join(os.path.dirname(__file__), './resources/challenges.json')) as challenges:
    dilemma = tradeoff_analytics.dilemmas(json.load(challenges), generate_visualization=True)

print(json.dumps(dilemma, indent=2))
