#Name of the assistant is Jarvis
import speech_recognition as sr
import win32com.client
import serial
import time

ser=serial.Serial('com3',9600)
time.sleep(0.5)

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
        except Exception as e:
            return " "
def recognize():
    while True:
        query = voice_input()
        if query.lower() == "turn on led 1":
            spk.speak("Okay, Turning led 1 ON")
            ser.write(b'1')
        elif query.lower() == "turn off led 1":
            spk.speak("Okay, Turning led 1 OFF")
            ser.write(b'2')
        
        if query.lower() == "turn on led 2":
            spk.speak("Okay, Turning led 2 ON")
            ser.write(b'3')
        elif query.lower() == "turn off led 2":
            spk.speak("Okay, Turning led 2 OFF")
            ser.write(b'4')
        
        if query.lower() == "turn on led 3":
            spk.speak("Okay, Turning led 3 ON")
            ser.write(b'5')
        elif query.lower() == "turn off led 3":
            spk.speak("Okay, Turning led 3 OFF")
            ser.write(b'6')
        
        if query.lower() == "turn on led 4":
            spk.speak("Okay, Turning led 4 ON")
            ser.write(b'7')
        elif query.lower() == "turn off led 4":
            spk.speak("Okay, Turning led 4 OFF")
            ser.write(b'8')
        elif query.lower() == "turn off all leds":
            spk.speak("Okay, Turning all leds OFF")
            ser.write(b'9')

        if query == "exit":
            time.sleep(2)
            spk.speak("Goodbye")
            break

while True:
    query = voice_input()
    if query.lower() == "hey jarvis":
        spk.speak("Hi there, How can I assist you today?")
        recognize()
    if query == "exit":
        time.sleep(2)
        spk.speak("Goodbye")
        break
