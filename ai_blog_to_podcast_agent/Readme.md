# 📰 ➡️ 🎙️ Blog to Podcast Agent

A Streamlit-based application that converts any blog post into a podcast episode. The app uses **OpenAI's GPT-4** for summarization, **Firecrawl** for scraping blog content, and **ElevenLabs** for generating natural-sounding audio.

Simply input a blog URL, and the app generates a podcast episode you can listen to or download!

## ✨ Features

- **Blog Scraping** — Scrapes the full content of any public blog URL using Firecrawl API.
- **Summary Generation** — Creates an engaging, concise summary (max 2000 characters) using OpenAI GPT-4.
- **Podcast Generation** — Converts the summary into audio using ElevenLabs text-to-speech API.
- **Secure API Key Input** — API keys are entered via the sidebar (never hardcoded).
- **Download Support** — Listen to the podcast in-browser or download it as an MP3.

## 🔑 API Keys Required

| API | Sign Up Link | Description |
|-----|-------------|-------------|
| **OpenAI** | [platform.openai.com](https://platform.openai.com/api-keys) | Powers blog summarization (GPT-4) |
| **ElevenLabs** | [elevenlabs.io](https://elevenlabs.io) | Converts text to natural speech |
| **Firecrawl** | [firecrawl.dev](https://www.firecrawl.dev) | Scrapes blog content from URLs |

## 🛠️ Setup

### Prerequisites

- Python 3.8 or higher
- API keys for OpenAI, ElevenLabs, and Firecrawl

### Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/fathimapa/ai_blog_to_podcast_agent.git
   cd ai_blog_to_podcast_agent
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the App

```bash
streamlit run blog_to_podcast_agent.py
```

The app will open in your browser at `http://localhost:8501`.

### How to Use

1. Enter your **OpenAI**, **ElevenLabs**, and **Firecrawl** API keys in the sidebar.
2. Paste a **blog URL** in the input field.
3. Click **"🎙️ Generate Podcast"**.
4. Listen to the generated podcast or click **"Download Podcast"** to save it.

## 📁 Project Structure

```
ai_blog_to_podcast_agent/
├── blog_to_podcast_agent.py   # Main Streamlit application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore rules
```

## 📦 Dependencies

```
agno
openai
elevenlabs
firecrawl-py
streamlit
```

## 📸 App Screenshot

```
┌─────────────────────────────────────────────────────┐
│  SIDEBAR               │  MAIN AREA                 │
│                        │                             │
│  🔑 API Keys           │  📰 ➡️ 🎙️ Blog to Podcast │
│  ┌──────────────────┐  │                             │
│  │ OpenAI API Key    │  │  Enter Blog URL:           │
│  └──────────────────┘  │  ┌───────────────────────┐ │
│  ┌──────────────────┐  │  │ https://example.com   │ │
│  │ ElevenLabs Key    │  │  └───────────────────────┘ │
│  └──────────────────┘  │                             │
│  ┌──────────────────┐  │  [🎙️ Generate Podcast]     │
│  │ Firecrawl Key     │  │                             │
│  └──────────────────┘  │  🎧 Audio Player            │
│                        │  [Download Podcast]         │
└─────────────────────────────────────────────────────┘
```


## ⚠️ Notes

- Blog URLs must be **publicly accessible** (not behind a login or paywall).
- OpenAI API uses **pay-as-you-go** pricing. Use `gpt-4o-mini` for lower costs.
- ElevenLabs free tier has **limited characters** per month.
- **Python 3.12** is recommended. Python 3.14 may show compatibility warnings.
