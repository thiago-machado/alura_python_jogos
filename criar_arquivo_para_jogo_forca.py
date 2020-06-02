'''
Para abrir um arquivo, o Python possui a função built-in open().
Ela recebe dois parâmetros: o primeiro é o nome do arquivo a ser aberto,
e o segundo parâmetro é o modo que queremos trabalhar com esse arquivo, se queremos ler,
escrever ou fazer append.
O modo é passado através de uma string: "w" para escrita, "r" para leitura ou "a" para append.

Vale lembrar que o w sobrescreve o arquivo, se o mesmo existir. Se só quisermos adicionar conteúdo ao
arquivo, utilizamos o a.

Podemos também passar o encoding desejado.

Além do r, w e a existe o modificador b que devemos utilizar quando queremos trabalhar
no modo binário. Para abrir uma imagem devemos usar:
imagem = open("foto.jpg", "rb")

'''

def criar_arquivo():
    arquivo = open("palavras.txt", "w", encoding="utf-8")
    arquivo.write("banana\n")   # escrevendo no arquivo
    arquivo.write("maçã\n")
    arquivo.write("laranja\n")
    arquivo.write("kiwi\n")
    arquivo.write("tamarindo\n")
    arquivo.write("uva\n")
    arquivo.write("pêra\n")
    arquivo.write("acabaxi\n")
    arquivo.close()     # sempre fechar o aquivo

if (__name__ == "__main__"):
    criar_arquivo()
