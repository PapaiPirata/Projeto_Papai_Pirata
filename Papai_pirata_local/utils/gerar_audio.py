import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def gerar_audio(mensagem):
    API_KEY = os.getenv("ELEVENLABS_API_KEY")
    VOICE_ID = "Rachel"  # Você pode trocar por outro ID disponível

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": mensagem,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    pasta = datetime.now().strftime("saida/%Y-%m-%d")
    os.makedirs(pasta, exist_ok=True)
    caminho = f"{pasta}/audio.mp3"

    with open(caminho, "wb") as f:
        f.write(response.content)

    return caminho
