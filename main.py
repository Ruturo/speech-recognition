from captureAudio import *
from processor import *

recognizer = sr.Recognizer()

def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input(recognizer)
        text = convert_voice_to_text(audio,recognizer)
        print(text)

main()