import requests
import os

def gerar_narracao(texto, output_path):
    url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"
    headers = {
        "xi-api-key": os.getenv("ELEVENLABS_API_KEY"),
        "Content-Type": "application/json"
    }
    data = {
        "text": texto,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.7
        }
    }
    response = requests.post(url, json=data, headers=headers)
    with open(output_path, "wb") as f:
        f.write(response.content)
