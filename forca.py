import random


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    imprime_log_apresentacao()

    # Todas as formas abaixo funcionam, já que os parâmetros são opcionais
    # carrega_palavra_secreta(nome_arquivo="frutas.txt", primeira_linha_valida=0)
    # carrega_palavra_secreta("frutas.txt", 0)
    # carrega_palavra_secreta("frutas.txt")
    # carrega_palavra_secreta(nome_arquivo="frutas.txt")
    # carrega_palavra_secreta(primeira_linha_valida=0)
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)


    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # Enquanto "acertou" E "enforcou" sejam FALSE, executa o while
    while (not acertou and not enforcou):
        chute = pede_chute()

        if(chute in palavra_secreta):   # Verifica se a letra "chuatada" existe na palavra
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas   # acertou será True caso não conste mais "_" em "letras_acertadas"
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_log_apresentacao():
    print("*********************************")
    print("****Bem vindo ao jogo da Forca***")
    print("*********************************")


# Define um nome de arquivo que seria o padrão usado quando não fosse especificado algum arquivo.
# Ou seja, se passar algum parâmetro para carrega_palavra_secreta(...), esse parâmetro será o nome do arquivo.
# Caso não passe nada, ou seja, caso chame carrega_palavra_secreta() sem parâmetros, o valor padrão será "palavras.txt"
# Isso só é possível porque no Python temos como definir um valor padrão para os parâmetros e assim permitindo os parâmetros opcionais.
def carrega_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=0):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    index = random.randrange(primeira_linha_valida, len(palavras))

    return palavras[index]


def inicializa_letras_acertadas(palavra):

    # Estamos inicializando nosso array com um "_" para cada letra da palavra secreta.
    # Resumidamente, é como se iteracemos cada letra da palavra_secreta dentro dos [] e
    # desejássemos que para cada letra iterada, o conteúdo na lista seja um "_".
    # Essa funcionalidade do Python se chama List Comprehension, em português, Compreensão de lista.
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra deseja chutar?")
    return chute.strip().upper()  # Equivalente ao trim()


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:  # Iterando a palavra secreta, caractere por caractere
        if (chute == letra):  # upper deixa a palavra/letra em maiúsculo
            letras_acertadas[index] = chute
        index += 1

if (__name__ == "__main__"):
    jogar()
