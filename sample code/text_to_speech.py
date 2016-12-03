# Code for switching between Watson and Nao voices 
# Selene Baez modified from Dhaval R Sonawane et al.

from naoqi import ALProxy
import json, time, unicodedata, logging
from os.path import join, dirname, abspath
from watson_developer_cloud import TextToSpeechV1

# Usage:
# import text_to_speech as tts
# tts.say("This text will be played on the robot.")
# tts.set_voice(tts.MICHAEL_VOICE)
# tts.say("This will be played in the Michael voice.")

NAO_VOICE = "nao"
MICHAEL_VOICE = "michael" # English - US
SOFIA_VOICE = "sofia" # Spanish - Latinamerica
RENEE_VOICE = "renee" # French - France
ISABELA_VOICE = "isabela" # Portuguese - Brazil

class TextToSpeech():
	def __init__(self):
		print ("Starting text to speech")

		self.voice = NAO_VOICE
		self.nao_tts = ALProxy("ALTextToSpeech", "localhost", 9559)
		self.watson_tts = TextToSpeechV1(
				username="47ab5412-296a-4213-9cb2-6a40cf67480c",
				password="CjidJ7klhtjj")
	
	def say(self, text):
		if self.voice == NAO_VOICE:
			self.nao_tts.say(text)
		elif self.voice == MICHAEL_VOICE:
			output_path = join(dirname(__file__), "output.wav")
			with open(output_path, "wb") as audio_file:
				audio_file.write(self.watson_tts.synthesize(text, voice="en-US_MichaelVoice", accept="audio/wav"))

			audioplayer = ALProxy("ALAudioPlayer", "localhost", 9559)
			abs_output_path = abspath(output_path)
			audioplayer.playFile(abs_output_path)
		elif self.voice == SOFIA_VOICE:
			output_path = join(dirname(__file__), "output.wav")
			with open(output_path, "wb") as audio_file:
				audio_file.write(self.watson_tts.synthesize(text, voice="es-US_SofiaVoice", accept="audio/wav"))

			audioplayer = ALProxy("ALAudioPlayer", "localhost", 9559)
			abs_output_path = abspath(output_path)
			audioplayer.playFile(abs_output_path)
		elif self.voice == RENEE_VOICE:
			output_path = join(dirname(__file__), "output.wav")
			with open(output_path, "wb") as audio_file:
				audio_file.write(self.watson_tts.synthesize(text, voice="fr-FR_ReneeVoice", accept="audio/wav"))

			audioplayer = ALProxy("ALAudioPlayer", "localhost", 9559)
			abs_output_path = abspath(output_path)
			audioplayer.playFile(abs_output_path)
		elif self.voice == ISABELA_VOICE:
			output_path = join(dirname(__file__), "output.wav")
			with open(output_path, "wb") as audio_file:
				audio_file.write(self.watson_tts.synthesize(text, voice="pt-BR_IsabelaVoice", accept="audio/wav"))

			audioplayer = ALProxy("ALAudioPlayer", "localhost", 9559)
			abs_output_path = abspath(output_path)
			audioplayer.playFile(abs_output_path)
	
	def set_voice(self, voice):
		self.voice = voice

tts = TextToSpeech() 

def set_voice(new_voice):
	print ("Set voice to %s" % new_voice)
	tts.voice = new_voice

def say(text):
	print ("Saying %s" % text)
	tts.say(text)
