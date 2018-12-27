'''
Voice to text to poem to speech
Credits: Michel, Lauren, Thomas
'''

#https://pythonprogramminglanguage.com/text-to-speech/
## cmd 1::::  sudo pip install gTTS
## cmd 2::::  sudo pip install pyttsx
import sys
from gtts import gTTS           ## Packages for Text to voice
import os
import speech_recognition as sr ## Packages for voice recognizer
import tensorflow as tf
tf.enable_eager_execution()
from tensorflow.keras.layers import Embedding, GRU, Dense
import numpy as np
import re
from textblob import TextBlob
import random
from poem_generator import*
import time
##### KNOWN PARAMETERS
#######################################################
##sys.path
##sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python')
##sys.path.append('/Users/ShebMichel/Library/Python/2.7/lib/python/site-packages'
################################################################################
############ AUDIO CONVERSION TO TEST
t0=time.time()
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    tts = gTTS(text='HELLO! My Name is BIT-LIT. PLEASE SPEAK IN ABOUT 3 SECONDS.', lang='en')
    tts.save("BitLit.mp3")
    os.system("afplay BitLit.mp3")
#    ######
    
    print("SPEAK NOW-SPEAK NOW-SPEAK NOW:")
    audio = r.listen(source)   
    tts = gTTS(text='THANK YOU! GIVE ME A SECOND TO READ OUT YOUR POEM', lang='en')
    tts.save("BitLit.mp3")
    os.system("afplay BitLit.mp3")
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)
    AA0=r.recognize_google(audio)
    USER_INPUT=AA0
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))    
text_generated=poem(USER_INPUT)
#### END CODE
#########################################################
################# TEXT CONVERSION IN AUDIO
################# FEED POEM TO TRANSCRIBER
print('ML POEM is:', text_generated)
tts = gTTS(text=text_generated, lang='en')
tts.save("BitLit.mp3")
os.system("afplay BitLit.mp3")
#########################################################
####
print("BIT-LIT ENDING STATEMENT:")   
tts = gTTS(text='THANK YOU! CHECK ME OUT IN THE NEWS SOON.', lang='en')
tts.save("BitLit.mp3")
os.system("afplay BitLit.mp3")
######
t1   =time.time()
total=t1-t0
print 'Time spent is about:', np.round(total), 'seconds'
### USING JUPITER
# import IPython.display as ipd
# ipd.Audio(filename='path/to/file.mp3')
#tk.mainloop()
