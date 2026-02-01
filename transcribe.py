import whisper

def transcribe_audio(audio_path, output_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)

    text = result["text"]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return text
