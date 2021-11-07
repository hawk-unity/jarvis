from playsound import playsound
from gtts import gTTS
import speech_recognition as sr 
import time
from datetime import date, datetime
import random
from random import choice
from pydub import AudioSegment
import webbrowser
r = sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("anlamadım ya düzgün söyle")
        except sr.RequestError:
            print("sistem çalşşmıyor aga ")
        return voice

def response(voice):
    if "merhaba" in voice :
        speak("18 yaşında bir imam hatip mezunu bir yazılımcısın")
    if "selam" in voice :
        speak("aleykümselam kardeşim")
    if "saat kaç" in voice:
        selection = ["Saat şu an: ", "Hemen bakıyorum: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

    if "google'da ara" in voice:
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} içi Google'da bulabildiklerimi listeliyorum.".format(search))

def speak(string):
    tts=gTTS(text=string, lang="tr")
    file= "answer.mp3"
    tts.save(file)
    playsound(file)

speak("Sesli asistana hoşgeldin beni faruk yaptı , benim adım jarvis size nasıl yardımcı olabilirim ")
while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice)
        print(voice.capitalize())
        response(voice)
