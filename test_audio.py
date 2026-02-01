from extract_audio import extract_audio

video_path = "C:/HCL_space/Video-To-Summary/videos/Kafka in 100 Seconds - Fireship (480p, h264, youtube).mp4"
audio_path = "audio/test.mp3"

extract_audio(video_path, audio_path)
print("Audio extracted successfully!")
