import speech_recognition as sr
import pyaudio

def capture_voice_input(recognizer):
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source,None,10)
    return audio

def convert_voice_to_text(audio,recognizer):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text


