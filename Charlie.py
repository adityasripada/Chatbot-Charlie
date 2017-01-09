import aiml
import os
import speech_recognition as sr
from gtts import gTTS

kernel = aiml.Kernel()
path = "/home/warr/Desktop/ai/aiml-en-us-foundation-alice/"

for lalu in os.listdir(path):
	if lalu != ".hg" and lalu != "test.mp3" and lalu!= "Charlie.py":	
		kernel.learn(lalu)
# Create the kernel and learn AIML files


if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

kernel.respond("load aiml b")

while True:
	r = sr.Recognizer()
	raw_input(">Press")  
	with sr.Microphone() as source:
    		r.adjust_for_ambient_noise(source)
    		print("Say something!")
    		audio = r.listen(source)
	try:
		message = r.recognize_bing(audio,key = "ed3acfea3f3d45bcad3bb7c04a2591f4")
		#message = r.recognize_google(audio)
		#message = r.recognize_bing(audio)
		print message
	except:
		ts = gTTS(text = "Can you please repeat?", lang = 'en')
		ts.save("test.mp3")
		os.system("mpg123 test.mp3")
		continue
	if 'brands' in message.lower() and 'wat' in message.lower():
		answer = "120+ brands across sectors which includes 20+ global clients."
	elif 'first office' in message.lower():
		answer = The first office of WATConsult was in Colaba, Mumbai
	elif 'first employee' in message.lower():
		answer = Gautam Bhatia. School friend of Rajiv Dingra.
	elif 'philosophy' in message.lower():
		answer = "1. do more with less. 2. make big of nothing. 3. something out of nothing 4.punch above your weight"	
	elif 'superheroes' in message.lower():
		answer = "Conviction in self. Do the impossible. "
	elif 'delhi' in message.lower() and 'bangalore' in message.lower() and 'team' in message.lower():
		answer = "WATConsult has 50+ employees in Delhi and 25+ in Bangalore. And 1000s of potential employees in CV form in our inboxes."	
	elif 'wat' in message.lower() and 'rank' in message.lower():
		answer = "WAT is by far the biggest social media agency in India and soon to be the one of the topmost digital agencies in the country."
	elif 'recent' in message.lower() and 'achievements'in message.lower():
		answer = "Drivers of Digital (DOD) Agency of the year 2016, Entered the roster of Hindustan Unilever (HUL), successful creative campaign for the international player Emirates NBD"
	elif message.lower() == "quit":
		answer = "See you Later!!" 		
		exit()	
	elif message.lower() == "initiate shadow mode":
		answer = "Initiating shadow Modde!!!!"
	elif message.lower() == "save":
		kernel.saveBrain("bot_brain.brn")
	else:	
		answer =  kernel.respond(message)
		print answer
	ts = gTTS(text = answer, lang = 'en')
	ts.save("test.mp3")
	os.system("mpg123 test.mp3")
	
