import subprocess
import os

def extract_audio(video_path, audio_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-vn",
        "-acodec", "mp3",
        audio_path
    ]

    subprocess.run(command, check=True)
