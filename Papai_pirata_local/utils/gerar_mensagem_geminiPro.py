import webbrowser
from urllib.parse import quote

mensagem_gerada = "Arrr! A sorte favorece os bravos marinheiros!"
prompt_video = f"Crie um vídeo curto de um pai pirata motivacional com a mensagem: '{mensagem_gerada}'"

# A URL exata para preencher o chat pode não ser pública ou estável.
# Muitas ferramentas web não permitem preencher o campo de input via URL para segurança.
# Esta é uma tentativa e pode não funcionar perfeitamente com gemini.google.com.
# Uma alternativa mais confiável seria o usuário copiar e colar.

# Tentativa 1: Abrir Gemini para o usuário digitar.
# webbrowser.open("https://gemini.google.com/chat/new")

# Tentativa 2: Preencher algo na URL (geralmente não funciona para o campo de input de chat dinâmico)
# prompt_encoded = quote(prompt_video)
# url = f"https://gemini.google.com/chat?q={prompt_encoded}" # Isso é mais comum para pesquisa, não chat input
# webbrowser.open(url)

# A melhor abordagem para "abrir e preencher" é abrir e instruir o usuário a colar.
# Ou, usar a API diretamente (Solução 1).

# Para sua aplicação local, você poderia:
print("Vídeo via Gemini App (Manual):")
print("1. Abra seu navegador em: https://gemini.google.com/chat/new")
print("2. Copie o seguinte prompt e cole no chat para gerar seu vídeo:")
print("------------------------------------------------------------------")
print(prompt_video)
print("------------------------------------------------------------------")
webbrowser.open("https://gemini.google.com/chat/new") # Abre a aba para o usuário