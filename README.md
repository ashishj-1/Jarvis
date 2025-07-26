# 🤖 Jarvis – Voice-Controlled Desktop Assistant (No AI)

Jarvis is a lightweight, voice-activated assistant built in Python that helps you perform everyday tasks like opening websites,
playing songs, checking the time, or fetching news headlines — all without using expensive AI services.

💡 No GPT or cloud AI used — works offline (except for APIs like news and YouTube).

📂 Project Structure

```JARVIS/
├── __pycache__/            # Compiled cache
├── .venv/                  # Python virtual environment
├── config.py               # Stores API keys/configurations
├── main.py                 # Core logic for voice commands
├── musicLibrary.py         # Dictionary of music track names and URLs
├── requirements.txt        # Python dependencies
├── .env                    # API key storage (not tracked by Git)
└── .gitignore              # Excludes .env, __pycache__, etc.
```

# 🎯 Features

* 🎤 Voice command detection using microphone
* 🌐 Open popular websites via voice (Google, Facebook, YouTube, etc.)
* 🎵 Play songs from a custom music library or search YouTube
* 📰 Get top 5 Indian news headlines using News API
* 🕒 Check current time
* 🗣️ Offline text-to-speech responses
* 🔁 Wake word detection ("Jarvis")
 
# 🔧 Technologies Used

* `speech_recognition` – for voice input
* `pyttsx3` – for offline text-to-speech
* `webbrowser` – to open links
* `requests` – to fetch news data
* `datetime` – for time handling
* `Python 3.10+`

# 🚀 Getting Started
1. Clone the Repository

```bash
git clone https://github.com/yourusername/jarvis.git
cd jarvis
```

2. Setup Virtual Environment
   
```bash
python -m venv .venv
source .venv/Scripts/activate   # On Windows
# or
source .venv/bin/activate       # On Linux/macOS
```

3. Install Dependencies

`bash
pip install -r requirements.txt`

4. Add API Key

Create a `.env` file in the root directory and add your News API key:
env
NEWS_API_KEY=your_news_api_key_here
> Get your free News API key from [https://newsapi.org](https://newsapi.org)

# ▶️ Run Jarvis

bash
python main.py

Jarvis will listen for the wake word **"Jarvis"** and then await your commands.
🧪 Sample Commands

* “Jarvis, open Google”
* “Play Night Changes” *(must be in musicLibrary.py)*
* “What’s the time?”
* “Tell me the news”
* “Stop” or “Exit” to quit

# 📜 License

MIT License — free to use, modify, and share.

# 🙏 Acknowledgments

* Open-source Python libraries
* News API
* Community contributors
* You — for checking out this project!
