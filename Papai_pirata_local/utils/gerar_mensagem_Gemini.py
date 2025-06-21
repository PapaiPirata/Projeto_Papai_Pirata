import os
import webbrowser
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import quote

# Carrega as variáveis de ambiente
load_dotenv()

# Configura a API Key da Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Mapeamento para dias da semana em português
dias_semana = {
    "Monday": "segunda-feira",
    "Tuesday": "terça-feira",
    "Wednesday": "quarta-feira",
    "Thursday": "quinta-feira",
    "Friday": "sexta-feira",
    "Saturday": "sábado",
    "Sunday": "domingo"
}

print("Passo 1 - Início")

def gerar_mensagem_gemini():
    try:
        print("Passo 2 - Obtendo data")
        hoje = datetime.now()
        dia_semana_en = hoje.strftime("%A")
        dia_semana_pt = dias_semana.get(dia_semana_en, dia_semana_en)
        data = hoje.strftime("%d/%m/%Y")

        print("Passo 3 - Criando prompt")
        prompt = f"""
        Hoje é {dia_semana_pt}, {data}. Crie uma mensagem curta, motivacional e com humor de pai pirata.
        Fale de forma animada como um pirata alegre que quer inspirar os filhos e que caiba num video de 8 segundos.
        """

        print("Passo 4 - Inicializando modelo Gemini")
        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

        print("Passo 5 - Gerando mensagem")
        response = model.generate_content(prompt)

        print("Passo 6 - Mensagem gerada")
        return response.text.strip()
    
    except Exception as e:
        print(f"ERRO: {str(e)}")
        return "Arrr! Nem o mar bravo impede o Papai Pirata de motivar a tripulação hoje! 🌊🏴‍☠️"

# Executa
print("Iniciando geração da mensagem...")
mensagem = gerar_mensagem_gemini()
print("\n=== MENSAGEM GERADA ===")
print(mensagem)
print("=======================")

agora = datetime.now()
formato_data_hora = agora.strftime("%Y-%m-%d_%H-%M-%S")
# Nome base do seu arquivo
nome_base  = "texto_gemini"
# Montar o nome completo do arquivo
nome_arquivo  = f"{nome_base}_{formato_data_hora}.txt"
# Salvar o arquivo
try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write("Gerar uma Animação 2D em estilo de conto de fadas, em português do brasil, com traços suaves e arredondados, cores vibrantes e saturadas, o pirata deve ser careca com barba grande. Crie com base no texto: " + mensagem)
        print(f"O arquivo '{nome_arquivo}' foi salvo com sucesso!")
except IOError as e:
    print(f"Erro ao salvar o arquivo '{nome_arquivo}': {e}")        

print(f"O nome do arquivo gerado será: {nome_arquivo}")

print("Vídeo via Gemini App (Manual):")
print("1. Abra seu navegador em: https://gemini.google.com/chat/new")
print("2. Copie o seguinte prompt e cole no chat para gerar seu vídeo:")
print("------------------------------------------------------------------")
print("Gerar uma Animação 2D em estilo de conto de fadas, com traços suaves e arredondados, cores vibrantes e saturadas com base no texto: ", mensagem)
print("------------------------------------------------------------------")
webbrowser.open("https://gemini.google.com/app/c045e7e23b1c016d") # Abre a aba para o usuário