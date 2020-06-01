import random

# Em Python, quando queremos criar uma função, precisamos defini-la através da palavra chave def
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # Quase todas as funções utilizadas aqui são built-in:
    # https://docs.python.org/3/library/functions.html

    tentativas = 0
    numero_secreto = random.randrange(1, 101) # Gerando um número aleatório entre 1 e 100
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    # while funciona da mesma maneira que no Java. Apenas se atentar ao ":" no final da condição
    while (rodada <= tentativas):

        # print("Tentativa ", rodada, "de", tentativas)

        # Outra forma de exibir a mesma saída acima
        # No local de {} entrará os valores inseridos em format()
        print("Tentativa {} de {} tentativas".format(rodada, tentativas))

        # input() vai exigir do usuário uma entrada de dados
        # int() vai converter o que o usuário digitar em um inteiro
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou: ", chute)

        if(chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100!!!")
            continue    # Mesma função do continue no Java

        # Condição if e else exige um ":" após a condição
        # Respeitar a identação! Tudo o que estiver identado o código vai entender que
        # faz parte da condição if/else
        if (numero_secreto == chute):
            print("Acertou! Você fez {} pontos.".format(pontos))
            print("Parabéns")
            break
        else:
            if (chute > numero_secreto):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (chute < numero_secreto):  # elif é similar ao else if no Java
                print("Você errou! O seu chute foi menor que o número secreto.")
            if (rodada == tentativas):
                print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
        rodada = rodada + 1
        pontos_perdidos = abs(numero_secreto - chute)   # função abs() retorna o número absoluto
        pontos = pontos - pontos_perdidos


    # "for" exige uma variável que receberá o valor dos itens que serão iterados. No nosso caso, será o "index".
    # range() conterá os itens que serão iterados. No caso, começaremos da posição 1 até "tentativas + 1"
    # Igual ao laço while, se atentar a identação e aos ":" na declaração do for.
    print("***TESTANDO LAÇO FOR***")
    for index in range(1, tentativas + 1):
        print("Iteração posição {}".format(index))

    # Essa mensagem está FORA do while. Se atentar a identação.
    print("Fim")

if (__name__ == "__main__"):
    jogar()
