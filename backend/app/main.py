from fastapi import FastAPI, WebSocket
from app.services.speech_to_text import transcribe_audio
from app.services.translation import translate_text
from app.services.summarization import generate_summary

app = FastAPI()
clients = []
conversation_log = ""

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global conversation_log
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            audio_data = await websocket.receive_bytes()
            text = transcribe_audio(audio_data)
            conversation_log += text + " "
            translated_text = translate_text(text)
            for client in clients:
                await client.send_text(translated_text)
    except:
        clients.remove(websocket)

@app.get("/summary")
def get_summary():
    global conversation_log
    summary = generate_summary(conversation_log)
    conversation_log = ""
    return {"summary": summary}