from youtube_transcript_api import YouTubeTranscriptApi
import re
from flask import jsonify, request

def get_youtube_video_id(url):
    # Extrait l'ID de la vidéo à partir de l'URL
    video_id = re.search(r"(?<=v=)[^&]+", url)
    if not video_id:
        video_id = re.search(r"(?<=be/)[^?&]+", url)
    return video_id.group(0) if video_id else None

def get_transcription(video_url):
    # Récupère l'ID de la vidéo
    video_id = get_youtube_video_id(video_url)
    if not video_id:
        return "Invalid YouTube video URL."
    
    try:
        # Récupère la liste des sous-titres disponibles
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Sélectionne le premier transcript disponible
        transcript = transcript_list.find_transcript(['en', 'fr', 'de', 'es'])  # essaie plusieurs langues
        transcription = " ".join([item['text'] for item in transcript.fetch()])
        return transcription
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Exemple : l'URL sera fournie par le module RSS
video_url = "https://www.youtube.com/watch?v=-mMH3_5o1h4"
transcription = get_transcription(video_url)

print(transcription)