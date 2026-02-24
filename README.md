*Nova – Offline Voice Assistant (Python)*

Nova is a lightweight, offline desktop voice assistant built using Python. It focuses on accurate command recognition, fast execution, and zero cloud dependency. The system is designed to run efficiently on low-spec machines while maintaining privacy and predictable behavior.
This project demonstrates practical implementation of speech recognition, command parsing, and desktop automation in a fully offline environment.

*Overview*
Nova enables users to interact with their system using voice commands without relying on cloud APIs or external AI services. The assistant is optimized for low hardware usage and prioritizes reliability over conversational complexity.

*Features*
Offline speech recognition using Vosk
Text-to-speech responses using pyttsx3
Open commonly used websites:
YouTube
WhatsApp Web
Gmail
Launch system applications:
Notepad
Calculator
Provide real-time date and time
Capture screenshots
Fuzzy command matching to handle minor mispronunciations
Fully offline execution (no internet required for speech processing)
Optimized for systems with 8GB RAM or lower

*Design Approach*
Unlike most modern assistants that depend on cloud APIs and large language models, Nova is designed with a deterministic and modular architecture.
Key principles:
Fully offline processing
Keyword-based and fuzzy-matched command recognition
Lightweight execution
Clear command-response mapping
Easy extensibility for adding new commands
The system executes exactly what is requested without generating unpredictable outputs.

Tech Stack

*Python 3.9+*
Vosk – Offline speech recognition
sounddevice – Microphone audio input
pyttsx3 – Text-to-speech engine
pyautogui – Automation and screenshot functionality

Project Structure
Nova_Assistant/
│── nova.py
│── model/              # Vosk speech model (excluded from GitHub)
│── requirements.txt
│── .gitignore
│── README.md

Example commands:
"Open YouTube"
"Open WhatsApp"
"What time is it"
"Open calculator"
"Take screenshot"

Future Improvements:
System volume control
Music playback integration
Start Menu application indexing
Optional graphical user interface

*Author*
Shaun Banis
Second-year AI/ML student
Built to explore real-world speech systems, system automation, and offline assistant design.
