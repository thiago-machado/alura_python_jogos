import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        forca.jogar()   # Chamando método jogar() da forca
    elif (jogo == 2):
        adivinhacao.jogar() # Chamando método jogar() da adivinhacao

# A variável __name__ somente estará preenchida se o arquivo jogos.py for executado diretamente.
# Arquivos como adivinhacao.py e forca.py também possuem esse if. Contudo, eles somente
# executarão a função jogar() caso esses arquivos forem executados diretamente.
# Caso eles sejam importados, como é o caso nesse arquivo jogos.py, eles não serão executados.
# Em resumo, apenas entrará nesse bloco if se o arquivo for executado diretamente
if (__name__ == "__main__"):
    escolhe_jogo()

