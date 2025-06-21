from openai import OpenAI
import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_imagem(mensagem):
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Cartoon illustration of a pirate dad with two babies, inspired by: '{mensagem}'. Colorful, warm, cartoon style.",
        n=1,
        size="1024x1024"
    )

    image_url = response.data[0].url

    pasta = datetime.now().strftime("saida/%Y-%m-%d")
    os.makedirs(pasta, exist_ok=True)
    caminho = f"{pasta}/imagem.png"

    with open(caminho, "wb") as f:
        f.write(requests.get(image_url).content)

    return caminho
