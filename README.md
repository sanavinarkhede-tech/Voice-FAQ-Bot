# 🎤 Voice FAQ Bot

An AI-powered College FAQ Assistant that uses Google's Gemini API to answer student questions from a predefined FAQ knowledge base.

## 🚀 Features

- 💬 Ask questions using text
- 🤖 Gemini-powered AI responses
- 📚 FAQ-based knowledge system
- 🔒 Answers are restricted to available FAQ information
- ⚡ FastAPI backend
- 🌐 Simple web interface
- 🔊 Voice support planned as the next feature

## 🏗️ Architecture

User Question
       ↓
Web Interface
       ↓
FastAPI Backend
       ↓
FAQ Knowledge Base
       ↓
Google Gemini API
       ↓
AI Answer
       ↓
Web Interface

## 🛠️ Tech Stack

- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- JavaScript
- Uvicorn
- python-dotenv

## 📁 Project Structure

```text
voice-faq-bot/
│
├── app/
│   ├── main.py
│   ├── services/
│   │   ├── openai_client.py
│   │   └── voice_pipeline.py
│   └── static/
│       ├── index.html
│       ├── app.js
│       └── style.css
│
├── data/
│   └── faqs.json
│
├── .gitignore
├── README.md
└── requirements.txt
