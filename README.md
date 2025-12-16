# 🤖 Nova – Offline Voice Assistant (Python)

Nova is a **lightweight, offline desktop voice assistant** built using Python. It focuses on **accurate command recognition**, fast responses, and zero cloud dependency — making it perfect for low‑spec laptops and privacy‑friendly usage.

This project was built as a **resume‑ready, GitHub‑worthy project** with clean structure and practical features.

---

## ✨ Features

* 🎙️ **Offline Speech Recognition** (Vosk)
* 🗣️ **Text‑to‑Speech responses** (pyttsx3)
* 🌐 Open websites like:

  * YouTube
  * WhatsApp Web
  * Gmail
* 🖥️ Open system apps:

  * Notepad
  * Calculator
* ⏰ Tell **time & date**
* 📸 Take **screenshots**
* 🧠 **Fuzzy command matching** (understands mispronunciations like *"war sap" → WhatsApp*)
* 🔒 **No APIs, no internet required for speech**
* ⚡ Optimized for **8GB RAM / low‑end CPUs**

---

## 🧠 Why Nova?

Most voice assistants rely on cloud APIs and struggle with accents or low hardware.

Nova is different:

* Runs **completely offline**
* Uses **keyword + fuzzy matching** instead of unreliable LLM guesses
* Designed to **do exactly what the user says** — not hallucinate
* Easy to extend with new commands

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Vosk** – Offline speech recognition
* **sounddevice** – Microphone audio input
* **pyttsx3** – Text‑to‑speech
* **pyautogui** – Screenshots & automation

---

## 📂 Project Structure

```
Nova_Assistant/
│── nova.py
│── model/              # Vosk speech model (NOT pushed to GitHub)
│── requirements.txt
│── .gitignore
│── README.md
```

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Nova-Assistant.git
cd Nova-Assistant
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download Vosk model

Download a Vosk English model and extract it as:

```
Nova_Assistant/model/
```

(Models are intentionally excluded from GitHub to keep the repo clean.)

---

## ▶️ Run Nova

```bash
python nova.py
```

Say **"hello"** to wake Nova, then try commands like:

* "Open YouTube"
* "Open war sap"
* "What time is it"
* "Open calci"
* "Take screenshot"

---

## 🚫 What Nova Does NOT Do (By Design)

* ❌ No cloud APIs
* ❌ No ChatGPT / LLM hallucinations
* ❌ No background spying

This keeps Nova **fast, predictable, and beginner‑friendly**.

---

## 🚀 Future Improvements (Optional)

* Volume control
* Music playback
* App launching via Start Menu
* GUI interface

---

## 👨‍💻 Author

**Shaun Banis**
Second‑year AI/ML student
Built to learn real‑world voice systems and system automation

---

⭐ If you like this project, consider starring the repository!
