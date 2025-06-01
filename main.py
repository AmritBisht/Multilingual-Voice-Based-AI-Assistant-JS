from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile
from dotenv import load_dotenv
from pydub import AudioSegment
import speech_recognition as sr
import google.generativeai as genai


genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process_audio/")
async def process_audio(file: UploadFile = File(...), language: str = Form("en-US")):
    # Save uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp:
        temp.write(await file.read())
        temp_path = temp.name

    # Convert webm to wav
    audio = AudioSegment.from_file(temp_path, format="webm")
    wav_path = temp_path.replace(".webm", ".wav")
    audio.export(wav_path, format="wav")

    # Transcribe using Google Speech Recognition
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language=language)
        except sr.UnknownValueError:
            return {"response": "Sorry, I couldn't understand.", "transcription": ""}
        except sr.RequestError as e:
            return {"response": f"Speech Recognition error: {e}", "transcription": ""}

    # Generate response using Gemini
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(text)

    return {
        "transcription": text,
        "response": response.text
    }
@app.get("/")
def root():
    return {"status": "Voice chatbot backend is live"}
