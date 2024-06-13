#Name of the assistant is Jarvis
import speech_recognition as sr
import win32com.client
import pyfirmata
import datetime

comport='COM3'
board=pyfirmata.Arduino(comport)
out_1 = board.get_pin('d:2:o')
out_2 = board.get_pin('d:3:o')
out_3 = board.get_pin('d:4:o')
out_4 = board.get_pin('d:5:o')

spk = win32com.client.Dispatch("SAPI.SpVoice")

def voice_input():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold=0.5
    with sr.Microphone() as source:
        aud = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(aud, language="en-US")
            print(query)
            return query
        except sr.UnknownValueError:
            return "Sorry, didn't get that!"
        except Exception as e:
            return " "
def recognize():
    while True:
        query = voice_input()
        if query.lower() == "turn on led 1":
            spk.speak("Okay, Turning led 1 ON")
            out_1.write(1)
        elif query.lower() == "turn off led 1":
            spk.speak("Okay, Turning led 1 OFF")
            out_1.write(0)
        
        if query.lower() == "turn on led 2":
            spk.speak("Okay, Turning led 2 ON")
            out_2.write(1)
        elif query.lower() == "turn off led 2":
            spk.speak("Okay, Turning led 2 OFF")
            out_2.write(0)
        
        if query.lower() == "turn on led 3":
            spk.speak("Okay, Turning led 3 ON")
            out_3.write(1)
        elif query.lower() == "turn off led 3":
            spk.speak("Okay, Turning led 3 OFF")
            out_3.write(0)
        
        if query.lower() == "turn on led 4":
            spk.speak("Okay, Turning led 4 ON")
            out_4.write(1)
        elif query.lower() == "turn off led 4":
            spk.speak("Okay, Turning led 4 OFF")
            out_4.write(0)

        elif query.lower() == "turn on all leds":
            spk.speak("Okay, Turning all leds ON")
            out_1.write(1)
            out_2.write(1)
            out_3.write(1)
            out_4.write(1)    
        elif query.lower() == "turn off all leds":
            spk.speak("Okay, Turning all leds OFF")
            out_1.write(0)
            out_2.write(0)
            out_3.write(0)
            out_4.write(0)

        elif query.lower() == "what's the time":
            x=datetime.datetime.now()
            spk.speak(f"The time is {x.strftime("%I %M %p")}")
        elif query.lower() == "what's the date today":
            x=datetime.datetime.now()
            spk.speak(f"Today is {x.strftime("%B")},{x.day}")

        elif query.lower() == "bye":
            spk.speak("Goodbye")
            break

while True:
    query = voice_input()
    if query.lower() == "hey jarvis":
        spk.speak(f"Hi there, How can I assist you today?")
        recognize()
