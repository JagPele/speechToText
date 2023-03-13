# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
import time

def onNow():
	print("listening.....")
	r = sr.Recognizer()
	with sr.Microphone() as mic:
		audio_data = r.listen(mic)
		print("Recognizing your text.............")
		text = r.recognize_google(audio_data)
		print(text)

def callback(recognizer, audio):
	print("callback")
	# received audio data, now we'll recognize it using Google Speech Recognition
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		text = recognizer.recognize_google(audio)
		print("Google Speech Recognition thinks you said " + text)
		if text.lower() == "bitch":
			print("you said bitch......\n")
			listen(audio, recognizer)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
# def SpeakText(command):
	
# 	# Initialize the engine
# 	engine = pyttsx3.init()
# 	engine.say(command)
# 	engine.runAndWait()
	
	
# Loop infinitely for user to
# speak
# Exception handling to handle
# exceptions at the runtime
# try:
	
	# use the microphone as source for input.
with sr.Microphone() as mic:
	r.adjust_for_ambient_noise(mic)

	while True:
		r = sr.Recognizer()
		try:
			audio_data = r.listen(mic)
			text = r.recognize_google(audio_data)

			if text.lower() == "hello":
				onNow()
		except sr.UnknownValueError:
			print("ERROR")
			continue

	
#print("Noise adjusted")
	
# start listening in the background (note that we don't have to do this inside a `with` statement)
# stop_listening = r.listen_in_background(mic, callback)
# print("listening")
# # `stop_listening` is now a function that, when called, stops background listening

# init_words = r.listen_in_background(mic, callback)

# print("SLEEP TIME")
# 	# if init_words.lower() == "bitch":
# 	# 	print("you said bitch......\n")
# 	# 	listen(mic, r)
# time.sleep(2)

# print("SLEPT")

# init_words(wait_for_stop=False)

# print("STOPPED LISTENING")


# while(1):
# 	time.sleep(5)
# 	print("WHILE")

		
# 		# Using google to recognize audio
# 		# text = r.recognize_google(audio)
# 		# text = text.lower()

# 		# print(text)
# 		#SpeakText(MyText)
		
# # except sr.UnknownValueError:
# 	# print("ERROR")
