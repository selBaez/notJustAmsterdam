# Code for using trade off analytics
# By Selene Baez

import json, os
from os.path import join, dirname

def profileMaking(personality):
    """
    This method builts a Tourist profile according to the personality of the user

    Args:
        personality: json with personality attributes

    Returns:
        profile: dictionary with "culture-freak", "party-animal", "recreational-smoker"
    """
    #TODO: Algorithm for Tourist type

    profile = {"culture-freak": 0.3, "party-animal": 0.3, "recreational-smoker": 0.4}

    return profile

#TODO: call personality insights
# give Twitter credentials, get json with personality description
personality = {}

# Create profile based on personality
profile = profileMaking(personality)

print("yay!")
