import whisper

def load_whisper_model():
    return whisper.load_model("small")