
# Requisitos: instale as bibliotecas com:
# pip install openai requests moviepy

import openai
import requests
from moviepy.editor import *
import os

# Configurações de API
OPENAI_API_KEY = 'SUA_CHAVE_OPENAI'
ELEVENLABS_API_KEY = 'SUA_CHAVE_ELEVENLABS'

# Passo 1 - Gerar texto com ChatGPT
def gerar_texto():
    openai.api_key = OPENAI_API_KEY
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Crie uma mensagem motivacional com humor para pais no estilo Papai Pirata, com até 100 palavras."}
        ]
    )
    return resposta['choices'][0]['message']['content']

# Passo 2 - Gerar narração com ElevenLabs
def gerar_audio(texto, filename="audio.mp3"):
    url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"  # voice ID padrão
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": texto,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.4, "similarity_boost": 0.8}
    }
    response = requests.post(url, headers=headers, json=data)
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename

# Passo 3 - Usar imagem local (ou já gerada por IA)
def montar_video(imagem_path, audio_path, output_path="video_final.mp4"):
    imagem = ImageClip(imagem_path).set_duration(10).resize(height=1080)
    audio = AudioFileClip(audio_path)
    imagem = imagem.set_audio(audio)
    imagem.write_videofile(output_path, fps=24)

if __name__ == "__main__":
    texto = gerar_texto()
    print("Mensagem gerada:", texto)
    gerar_audio(texto)
    montar_video("imagem_base.jpg", "audio.mp3")  # Substitua imagem_base.jpg pela imagem desejada
