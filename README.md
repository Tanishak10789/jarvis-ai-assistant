# Jarvis — Voice-Controlled AI Assistant

A Python desktop voice assistant inspired by Iron Man's Jarvis. Activates on the wake word "Jarvis," takes voice commands, and responds using a locally-running Llama 2 model via Ollama.

## Features
- Wake-word activation using Google's Speech Recognition API
- Conversational AI powered by Llama 2 (locally via Ollama)
- Voice responses using gTTS + Pygame
- Quick-launch sites (Google, YouTube, LinkedIn, Facebook)
- Live news headlines via NewsAPI

## Tech Stack
Python · Ollama (Llama 2) · SpeechRecognition · gTTS · Pygame · NewsAPI

## Setup
```bash
pip install -r requirements.txt
ollama pull llama2
python main.py
```
