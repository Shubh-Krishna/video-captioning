import os
from moviepy.editor import VideoFileClip
import whisper
import srt
from datetime import timedelta
from deep_translator import GoogleTranslator

def translate_text(text, target_language):
    try:
        # Translate the text to the target language
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Return the original text in case of error

# Function to save uploaded video file
def save_uploaded_file(uploaded_file, upload_dir):
    file_path = os.path.join(upload_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

# Function to extract audio from video
def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = video_path.rsplit(".", 1)[0] + ".wav"
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')
    return audio_path

# Function to transcribe audio to SRT using Whisper
def transcribe_audio_to_srt(audio_path, srt_path, target_language=None):
    # Load Whisper model
    model = whisper.load_model("base")
    
    # Transcribe audio
    transcription = model.transcribe(audio_path)
    segments = transcription["segments"]
    
    # Convert transcription to SRT format
    srt_entries = []
    for segment in segments:
        start = timedelta(seconds=segment["start"])
        end = timedelta(seconds=segment["end"])
        content = segment["text"]
        
        # Translate if target language is provided
        if target_language:
            content = translate_text(content, target_language)
        
        srt_entries.append(srt.Subtitle(index=len(srt_entries) + 1, start=start, end=end, content=content))
    
    # Write SRT file with UTF-8 encoding
    with open(srt_path, "w", encoding='utf-8') as f:
        f.write(srt.compose(srt_entries))
