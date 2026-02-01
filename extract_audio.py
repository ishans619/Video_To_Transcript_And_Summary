import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio(video_path, audio_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    video = VideoFileClip(video_path)

    if video.audio is None:
        video.close()
        raise ValueError("No audio track found in the video")

    video.audio.write_audiofile(audio_path, codec="mp3")
    video.close()
