from utils.gerar_mensagem import gerar_mensagem_dia

print("inicio main")

def main():
    print("Def main")
    mensagem = gerar_mensagem_dia()
    print("retorno Def main")
    print("Mensagem gerada:", mensagem)

#    imagem_path = gerar_imagem(mensagem)
#    print("Imagem salva em:", imagem_path)

#    audio_path = gerar_audio(mensagem)
#    print("Áudio salvo em:", audio_path)

if __name__ == "__main__":
    main()
