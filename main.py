from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.services.voice_pipeline import process_text, process_voice

app = FastAPI(title="Voice FAQ Bot")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def home():
    return FileResponse("app/static/index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/text")
async def text_question(question: str):
    try:
        result = process_text(question)
        return result
    except Exception as e:
        print("ERROR:", repr(e))
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/api/voice")
async def voice_question(file: UploadFile = File(...)):
    try:
        audio_data = await file.read()
        result = process_voice(audio_data, file.filename)
        return result
    except Exception as e:
        print("ERROR:", repr(e))
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/api/audio/{filename}")
def get_audio(filename: str):
    return FileResponse(
        f"data/audio/{filename}",
        media_type="audio/mpeg"
    )
