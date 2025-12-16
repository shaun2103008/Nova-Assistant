import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3
import webbrowser
import datetime
import os
import sys
import pyautogui
import subprocess
from difflib import get_close_matches

# --------------------
# TEXT TO SPEECH
# --------------------
def speak(text):
    print(f"Nova: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

# --------------------
# LOAD VOSK MODEL
# --------------------
MODEL_PATH = "model"

if not os.path.exists(MODEL_PATH):
    print("Model folder missing.")
    sys.exit()

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()

# --------------------
# AUDIO CALLBACK
# --------------------
def callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))

# --------------------
# LISTENING FUNCTION
# --------------------
def listen():
    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1,
        callback=callback
    ):
        print("🎙️ Listening...")
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                text = json.loads(recognizer.Result()).get("text", "")
                if text.strip():
                    print("User:", text)
                    return text.lower()

# --------------------
# COMMAND KEYWORDS
# --------------------
COMMAND_KEYWORDS = {
    "youtube": ["youtube", "you tube", "u tube", "you do", "you dub", "yt", "utub", "your deal"],
    "whatsapp": ["whatsapp", "what sap", "what's app", "watsap", "war sap", "whatsup"],
    "gmail": ["gmail", "g mail", "mail", "email", "e mail"],
    "notepad": ["notepad", "note pad", "note bad", "notes"],
    "calculator": ["calculator", "calci", "cal si", "calc", "calculate"],
    "time": ["time", "tym", "clock"],
    "date": ["date", "day", "today"],
    "screenshot": ["screenshot", "screen shot", "snap", "capture", "big screen short"],
}

EXIT_WORDS = ["bye", "bi", "bai", "by", "buy", "goodbye", "exit", "quit"]

# --------------------
# FUZZY COMMAND MATCHING
# --------------------
def detect_command(text):

    for w in EXIT_WORDS:
        if w in text:
            return "exit"

    for cmd, variants in COMMAND_KEYWORDS.items():
        for v in variants:
            if v in text:
                return cmd

        if get_close_matches(text, variants, n=1, cutoff=0.55):
            return cmd

    return None

# --------------------
# EXECUTE COMMAND
# --------------------
def execute(cmd):

    if cmd == "youtube":
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    elif cmd == "whatsapp":
        speak("Opening WhatsApp Web.")
        webbrowser.open("https://web.whatsapp.com")

    elif cmd == "gmail":
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com")

    elif cmd == "notepad":
        speak("Opening Notepad.")
        subprocess.Popen("notepad")

    elif cmd == "calculator":
        speak("Opening Calculator.")
        subprocess.Popen("calc")

    elif cmd == "time":
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif cmd == "date":
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif cmd == "screenshot":
        speak("Taking screenshot.")
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        speak("Screenshot saved.")

    elif cmd == "exit":
        speak("Goodbye Shaun.")
        sys.exit()

    else:
        speak("I did not understand that.")

# --------------------
# MAIN PROGRAM
# --------------------
def main():
    speak("Welcome back Shaun. Nova online. How can I assist you?")

    awake = False

    while True:
        text = listen()

        if not awake:
            if "hello" in text:
                awake = True
                speak("Yes Shaun, I'm listening.")
            continue

        cmd = detect_command(text)
        if cmd:
            execute(cmd)
        else:
            pass  # stay silent instead of annoying replies

if __name__ == "__main__":
    main()
