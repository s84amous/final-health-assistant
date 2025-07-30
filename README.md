# 🧠 Multimodal AI Health Assistant Agent

A modular, multi-agent LLM system that dynamically routes user queries to specialized AI agents and provides personalized health & lifestyle advice.

---

## 🚀 Features

- 🌤️ **Weather Agent** - Real-time weather information and recommendations
- 🏃 **Fitness Agent** - Personalized workout plans and exercise advice
- 🥗 **Nutrition Agent** - Recipe suggestions and dietary recommendations
- 🧘 **Wellbeing Agent** - Mental health and wellness support
- ⏰ **Reminders Agent** – Health-related reminders and notifications
- 🌐 **Web Search Fallback** – Web search fallback for general queries
- 🧠 **Selector Agent** – Intelligently routes queries to appropriate specialized agents

---

## 📋 Prerequisites

- **Python 3.8+** (tested with Python 3.11.7)
- **Ollama** installed and running
- **Git** for cloning the repository

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/final-health-assistant.git
cd final-health-assistant
```

### 2. Create Virtual Environment

Create virtual environment

```bash
python -m venv .venv
```

Activate on macOS/Linux

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the OLLAMA server

### 1. Pull the ollama server

```bash
ollama pull qwen2.5-coder:3b
```

### 2. Start ollama server

```bash
ollama serve
```

---

## 🚀 Running the Application

When all the above requirements have been fulfilled and the virtual environment is running.

```bash
python main.py
```

---

## 🧪 Example input

```
"I am feeling energetic today, I want to do a good workout that includes going to the swimming pool due to it being very hot today,
also add to my training biking and tell me a good place to do it. I need to eat to boost my protein intake and remind me to drink water in 1 hour"
```

## 👨‍💻 Contributors

- Amr Moustafa
- Muhammad Zakria
- Mohammad Erfan Hosseini
- Mohammad Mehdi Deylamipour

University of Bonn – Dialogue Systems – SS 2025

---

## 📝 License

This project is intended for educational and academic use only.
