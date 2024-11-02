# main.py

from fastapi import FastAPI, HTTPException, Query
from youtube_video_transcript_api import get_transcription

app = FastAPI()

@app.get("/transcribe")
async def transcribe_video(video_url: str = Query(..., description="URL de la vidéo YouTube à transcrire")):
    """
    Endpoint qui transcrit une vidéo YouTube à partir de son lien.
    """
    transcription = get_transcription(video_url)
    if "Invalid" in transcription or "error" in transcription:
        raise HTTPException(status_code=400, detail=transcription)
    
    return {"transcription": transcription}
