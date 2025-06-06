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
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp:
            content = await file.read()
            temp.write(content)
            temp_path = temp.name

        print(f"[DEBUG] File saved to: {temp_path}, size: {len(content)} bytes")

        # Convert to wav
        audio = AudioSegment.from_file(temp_path, format="webm")
        wav_path = temp_path.replace(".webm", ".wav")
        audio.export(wav_path, format="wav")
        print(f"[DEBUG] Converted to WAV: {wav_path}")

        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language=language)

        print(f"[DEBUG] Transcription: {text}")

        # Send to LLM
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(text)

        return {
            "transcription": text,
            "response": response.text
        }

    except sr.UnknownValueError:
        print("[ERROR] Could not understand audio.")
        return {"response": "Sorry, I couldn't understand.", "transcription": ""}

    except sr.RequestError as e:
        print(f"[ERROR] Speech recognition service error: {e}")
        return {"response": f"Speech Recognition error: {e}", "transcription": ""}

    except Exception as e:
        print(f"[ERROR] General error: {e}")
        return {"response": f"Server error: {e}", "transcription": ""}

@app.get("/")
def root():
    return {"status": "Voice chatbot backend is live"}


@app.get("/test_llm/")
def test_llm():
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content("Say hello in three different languages.")
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}

