
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import ollama
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()  
newsapi = "73a2f119c41c47b9959141d31c3873b4"  # Replace with your NewsAPI key if needed

def speak(text):
    """Convert text to speech using gTTS and play it."""
    tts = gTTS(text)
    tts.save('temp.mp3') 

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    """Process user input with Llama 2 via Ollama."""
    response = ollama.chat(
        model="llama2",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
            {"role": "user", "content": command}
        ]
    )
    return response['message']['content']
  # Fix: Correct retrieval of AI response

def processCommand(c):
    """Perform actions based on user command."""
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:3]:  # Speak only top 3 news articles
                speak(article['title'])
    else:
        output = aiProcess(c)  # Get AI response
        speak(output) 

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        print("Waiting for wake word 'Jarvis'...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio).lower()

            if "jarvis" in word:  # More flexible wake-word detection
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
