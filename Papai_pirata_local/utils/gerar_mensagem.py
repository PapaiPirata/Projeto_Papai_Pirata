import os
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Mapeamento de dias da semana em inglês para português
dias_semana = {
    "Monday": "segunda-feira",
    "Tuesday": "terça-feira",
    "Wednesday": "quarta-feira",
    "Thursday": "quinta-feira",
    "Friday": "sexta-feira",
    "Saturday": "sábado",
    "Sunday": "domingo"
}

def gerar_mensagem_dia():
    hoje = datetime.now()
    dia_semana_en = hoje.strftime("%A")         # Ex: "Monday"
    dia_semana_pt = dias_semana[dia_semana_en]  # "segunda-feira"
    data = hoje.strftime("%d/%m/%Y")

    prompt = (
        f"Hoje é {dia_semana_pt}, dia {data}. Crie uma mensagem motivacional "
        f"engraçada, no estilo de um pai pirata que está cuidando de seus filhos pequenos. "
        f"Use humor leve e inspiração. Apenas 1 parágrafo curto."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ou  "gpt-4"
        messages=[
            {"role": "system", "content": "Você é um pai pirata engraçado e inspirador."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    mensagem = response.choices[0].message.content.strip()
    return mensagem
