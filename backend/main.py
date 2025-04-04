from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile
from dotenv import load_dotenv
from pydub import AudioSegment
import speech_recognition as sr
import google.generativeai as genai

# Load .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process_audio/")
async def process_audio(file: UploadFile = File(...)):
    # Save uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
        temp.write(await file.read())
        temp_path = temp.name

    # Convert MP3 to WAV
    audio = AudioSegment.from_file(temp_path)
    wav_path = temp_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")

    # Transcribe audio
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return {"response": "Sorry, I couldn't understand."}
        except sr.RequestError as e:
            return {"response": f"Speech Recognition error: {e}"}

    # Generate response with Gemini
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(text)

    return {"response": response.text}
