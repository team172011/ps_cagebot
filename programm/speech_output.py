"""
module for the speech output
@autor: wimmer, simon-justus
"""

from gtts import gTTS
import os
from threading import Thread
import subprocess
import pyttsx

class Speaker:
    def __init__(self):
        pass
    
    def say_in_thread(self, msg):
        say_thread = Thread(target=self.say, args=(msg,))
        say_thread.start()

    def say(self, msg):
        engine = pyttsx.init()
        engine.setProperty("rate", 120)
        engine.say(msg)
        engine.runAndWait()
        
    def say_gtts(self, msg):
        tts = gTTS(msg, lang='de')
        tts.save('temp.mp3')
        devnull = open(os.devnull, 'wb')
        subprocess.call('C:\Users\ITM2\Surrogate\ps_cagebot\programm\playmp3.cmd temp.mp3', shell=False,
        stdout=subprocess.PIPE, stderr=devnull)
