from extract_audio import extract_audio
from transcribe import transcribe_audio
from summarize import summarize_text
import os

VIDEO_FILE = "C:/HCL_space/Video-To-Summary/videos/Kafka in 100 Seconds - Fireship (480p, h264, youtube).mp4"
AUDIO_FILE = "temp/audio.mp3"
TRANSCRIPT_FILE = "output/transcript.txt"
SUMMARY_FILE = "output/summary.txt"

os.makedirs("output", exist_ok=True)

extract_audio(VIDEO_FILE, AUDIO_FILE)

text = transcribe_audio(AUDIO_FILE, TRANSCRIPT_FILE)

summarize_text(text, SUMMARY_FILE)

print("✅ Transcript and summary created successfully!")
