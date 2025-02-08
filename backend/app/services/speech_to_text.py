import whisper
model = whisper.load_model("small")

def transcribe_audio(audio_data):
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_data)
    result = model.transcribe("temp_audio.wav")
    return result["text"]