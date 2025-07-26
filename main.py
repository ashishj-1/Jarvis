import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from datetime import datetime
from config import NEWS_API_KEY

# Speak using TTS
def speak(text):
    print(f"Jarvis: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Get audio input from user
def get_audio(timeout=5, phrase_time_limit=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""
        except Exception as e:
            print(f"Error during audio recognition: {e}")
            return ""

# Handle user commands
def process_command(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")

    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn.")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif command.startswith("play"):
        song = command.replace("play", "").strip().lower()
        if not song:
            speak("Please say the song name after 'play'.")
            return
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
            speak(f"Playing {song}.")
        else:
            speak(f"Couldn't find '{song}' in the music library. Searching on YouTube.")
            webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    elif "news" in command:
        speak("Fetching latest headlines.")
        try:
            response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}")
            if response.status_code == 200:
                articles = response.json().get("articles", [])[:5]
                for i, article in enumerate(articles, 1):
                    speak(f"News {i}: {article.get('title')}")
            else:
                speak("Sorry, I couldn't fetch the news right now.")
        except requests.exceptions.RequestException as e:
            print(e)
            speak("Network error while fetching the news.")

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}.")

    elif "exit" in command or "stop" in command:
        speak("Are you sure you want to exit?")
        confirmation = get_audio()
        if "yes" in confirmation.lower():
            speak("Goodbye!")
            exit()
        else:
            speak("Okay, continuing.")

    else:
        speak("Sorry, I didn't understand that command.")

# Main loop
if __name__ == "__main__":
    speak("Initializing Jarvis. Say 'Jarvis' to activate.")

    while True:
        try:
            print("Waiting for wake word...")
            wake = get_audio(timeout=10, phrase_time_limit=3)

            if "jarvis" in wake.lower():
                speak("Yes, how can I help you?")
                while True:
                    command = get_audio()
                    if command:
                        if "exit" in command.lower() or "stop" in command.lower():
                            process_command(command)
                            break  # Exit command mode
                        else:
                            process_command(command)
        except sr.WaitTimeoutError:
            continue
        except KeyboardInterrupt:
            speak("Shutting down.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            speak("Something went wrong.")