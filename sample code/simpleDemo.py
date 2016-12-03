# Code for simple Watson demo (nlc and tts) 
# Selene Baez .

import sys

########################## Main ##########################
# first argument: phrase
# second argument: who responds
    # Nao as default

import speech_to_text_app as stt
import text_to_speech as tts
import nlc

voice = sys.argv[1]

#TODO: if no phrase given, start detecting speech
phrase = sys.argv[2]

global HILTON_CLASSIFIER = "341781x90-nlc-7639"


# ask watson what type of phrase is this
topClass = nlc.find_class(HILTON_CLASSIFIER, phrase)

# Make the robot say the phrase
tts.set_voice(voice)
tts.say(phrase)

# say the veredict
veredict = 'The class is. ' + str(topClass['class_name']) + '. With confidence of. ' + str(topClass['confidence'])
tts.say(veredict)

