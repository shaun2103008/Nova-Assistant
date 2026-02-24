Nova – Offline Voice Assistant (Python)

Nova is a lightweight, offline desktop voice assistant built using Python. It focuses on accurate command recognition, fast execution, and zero cloud dependency. The system is designed to run efficiently on low-spec machines while maintaining user privacy.

This project was developed as a practical implementation of speech recognition, system automation, and command processing in a fully offline environment.

Features

Offline speech recognition using Vosk

Text-to-speech responses using pyttsx3

Open commonly used websites (YouTube, WhatsApp Web, Gmail)

Launch system applications (Notepad, Calculator)

Provide real-time date and time

Capture screenshots

Fuzzy command matching to handle minor mispronunciations

Fully offline execution (no cloud APIs required)

Optimized for systems with 8GB RAM or lower

Design Philosophy

Most voice assistants rely heavily on cloud APIs and large language models, which introduce latency, privacy concerns, and unpredictable behavior.

Nova is designed with a different approach:

Fully offline architecture

Deterministic command handling

Lightweight execution

Modular and easily extensible structure

The system prioritizes reliability and responsiveness over complex conversational capabilities.

Tech Stack

Python 3.9+

Vosk (offline speech recognition)

sounddevice (microphone input handling)

pyttsx3 (text-to-speech engine)

pyautogui (automation and screenshots)
