# Code for using trade off analytics
# By Selene Baez

import json, os
from os.path import join, dirname
import numpy as np
import personalityInsight, tradeOff

def profileMaking(personal_data, questionnaire_answers, budget, time):
    """
    This method builts a profile according to personal data of the user and questionnaire answers

    Args:
        personal data: dictionary with "name", "gender", "age"
        questionnaire_answers: list of 10 answers (e.g [a a ... b])
        budget: float amount of money
        time: int number of days available for challenges

    Returns:
        profile: dictionary with
                personal-data: dictionary with "name", "gender", "age"
                tourist-type: dictionary with "culture-freak", "party-animal", "recreational-smoker"
                resources: dictionary with "budget", "time"
    """
    # Anwers are coded as: a for culture-freak, b for party-animal, c for recreational-smoker
    tourist_type = {"culture-freak": questionnaire_answers.count('a'), "party-animal": questionnaire_answers.count('b'), "recreational-smoker": questionnaire_answers.count('c')}

    # Gather fixed resources
    resources = {"budget": budget, "time": time}

    # Create profile
    profile = {"personal-data": personal_data, "tourist-type": tourist_type, "resources": resources}

    return profile

def profileUpdate(profile, personality):
    """
    This method updates a profile according to the personality of the user

    Args:
        profile: dictionary with
                personal-data: dictionary with "name", "gender", "age"
                tourist-type: dictionary with "culture-freak", "party-animal", "recreational-smoker"
                resources: dictionary with "budget", "time"
        personality: json with personality attributes

    Returns:
        profile: update values for tourist-type
    """
    #TODO: Algorithm for Tourist type

    return profile

def routeCreation(potential_challenges):
    """
    This method sorts the challenges by city to create a circular route

    Args:
        profile: profile: dictionary with
                personal-data: dictionary with "name", "gender", "age"
                tourist-type: dictionary with "culture-freak", "party-animal", "recreational-smoker"
                resources: dictionary with "budget", "time"
        potential_challenges: list of challenges

    Returns:
        profile: dictionary with "culture-freak", "party-animal", "recreational-smoker"
    """
    #TODO: sort by circular route
    challenge_route = potential_challenges

    return challenge_route

#################################### INPUTS ####################################
#TODO get inputs through command line?
personal_data = {"Name": "Sofia Ramos", "Gender": "Female", "Age": 23}
questionnaire_answers = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c']
budget = 800.0
time = 7

################################### PIPELINE ###################################
# Create profile based on user report
profile = profileMaking(personal_data, questionnaire_answers, budget, time)

#TODO: Get personality through Watson Personality Insights
# give Twitter credentials, get json with personality description
personality = {}

# Update profile based on cognitive module
profile = profileUpdate(profile, personality)

#TODO: Get challenges based on Watson Tradeoff Analytics
potential_challenges = tradeOff.analyze(profile)

# Create circular route
challenge_route = routeCreation(potential_challenges)

# Maybe save into file? 

print("We did it! Yay!")
