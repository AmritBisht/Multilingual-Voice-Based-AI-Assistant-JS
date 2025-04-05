# 🌍 Multilingual Voice-Based AI Assistant

A **voice-enabled AI chatbot** that supports **multiple languages**. Speak into your mic, and get intelligent responses from Google Gemini — with voice feedback!

Built using:
- 🎤 Web Audio API + JS (frontend, Vercel)
- ⚙️ FastAPI backend (Render)
- 🧠 Google Gemini AI
- 🗣️ Google Speech Recognition API

---

## 🚀 Live Demo

🔗 Try the live demo here : [ Click ](https://multilingual-voice-based-ai-git-4983bc-amrits-projects-1a6211f2.vercel.app)

🔗 Frontend (Vercel): [https://your-vercel-app-url](https://multilingual-voice-based-ai-git-4983bc-amrits-projects-1a6211f2.vercel.app)

🌐 Backend (Render): [https://your-render-app-url](https://dashboard.render.com/web/srv-cvo2vs49c44c73bhteo0/deploys/dep-cvoaid6mcj7s7380h9cg)

---

## 📸 Features

✅ Voice recording (manual + auto-stop after 20s)  
✅ Translates speech to text in multiple languages  
✅ AI-powered responses via **Google Gemini**  
✅ Text-to-speech voice feedback  
✅ User-friendly, responsive UI  
✅ Status feedback (Listening / Processing...)

---

## 🧠 Tech Stack

| Layer         | Tech                                      |
|---------------|-------------------------------------------|
| Frontend      | HTML, CSS, JavaScript (Vercel)            |
| Backend       | FastAPI (Render)                          |
| Speech-to-Text| Google Speech Recognition                 |
| AI Model      | Google Gemini (via Generative AI SDK)     |
| Voice Output  | Web Speech API (SpeechSynthesis)          |

---

## 📁 Project Structure

```
multilingual-voice-ai-assistant/
├── backend/
│   ├── main.py               # FastAPI backend
│   └── .env                  # Contains GOOGLE_API_KEY
├── frontend/
│   └── index.html            # Web app with JS logic
└── README.md
```

---

## 🔑 Environment Variables (Backend)

On **Render Dashboard**, add this in the "Environment" section:

```bash
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> ⚠️ Ensure your `.env` is **not committed to Git**. FastAPI will use this to authenticate with Google Generative AI.

---

## 🧪 How It Works

1. User clicks **Start** → App records voice  
2. Audio is sent to backend → Transcribed using Google STT  
3. Transcribed text is sent to Gemini → AI generates response  
4. Response is returned → Spoken out loud using Text-to-Speech  

---

## 🌐 Supported Languages

- English 🇺🇸 (`en-US`)
- Hindi 🇮🇳 (`hi-IN`)
- French 🇫🇷 (`fr-FR`)
- Spanish 🇪🇸 (`es-ES`)

> You can add more languages by editing the `<select>` dropdown in `index.html`.

---

## ✨ User Feedback UX

- 🎙️ **Listening...** appears during recording  
- 🧠 **Processing...** while waiting for AI response  
- 💬 Shows user + AI messages in styled chat bubbles  
- 🔊 AI speaks reply using your selected language

---

## 🛠️ To Run Locally

### 1. Clone Repo

```bash
git clone https://github.com/your-username/multilingual-voice-ai-assistant.git
cd multilingual-voice-ai-assistant
```

### ⚙️ 2. Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt

# Create .env file
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# Start backend
uvicorn main:app --reload
```

### 🌐 3. Frontend (HTML + JS)

You can run this locally by just opening the file:

```bash
cd ../frontend
open index.html
```

Or, to deploy:

### 🧾 3. Frontend Deployment (Vercel)

Go to [https://vercel.com](https://vercel.com)

1. Create a new project.
2. Upload your `index.html`.
3. Inside `index.html`, replace the backend URL in the `fetch()` call:

```javascript
const response = await fetch("https://your-backend-url.onrender.com/process_audio/", { ... });
```

4. Deploy and done 🎉

---

## 🌍 Supported Languages

- English 🇺🇸 (`en-US`)
- Hindi 🇮🇳 (`hi-IN`)
- French 🇫🇷 (`fr-FR`)
- Spanish 🇪🇸 (`es-ES`)

> You can add more in the `<select>` dropdown inside `index.html`.

---

## 💬 UX Feedback

| Event                | UI Feedback           |
|----------------------|-----------------------|
| Recording Start      | "🎙️ Listening..."    |
| Recording End        | "🤖 Processing..."    |
| AI Reply             | Voice + Text Bubble   |

---

## 🧠 How It Works

1. User clicks record (manual start).
2. Audio is recorded for up to 20 seconds or until the user stops.
3. Sent to FastAPI → converted from `.webm` to `.wav`.
4. Transcribed using Google Speech Recognition.
5. Sent to Google Gemini → response generated.
6. AI response returned + spoken aloud via TTS.

---

## 💡 Future Plans

- Persistent chat history (memory)
- Translate Gemini response back into the user's language
- More language support
- UI animation + avatars
- Mobile PWA support

---

## 🙌 Credits

- FastAPI
- Google Generative AI
- Pydub
- Web Speech API
- Render
- Vercel

