tipos = ("string", "inteiro", "float",)

letras = tuple("Vinicius")

pares = tuple([0, 2, 4, 6, 8])

cidade = ("Jundiaí",)

print(tipos[0])
print(tipos[2])
print(tipos[-1])
print(tipos[-3])

matriz = (
    [15, "B", 32],
    ["Y", 45, 95],
    [31, 89, "H"],
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

nome = ("V", "i", "n", "i",)
print(nome[2:])
print(nome[:2])
print(nome[1:3])
print(nome[0:3:2])
print(nome[::])
print(nome[::-1])

jogos = ("xadrez", "jogo da velha", "dominó",)
for jogo in jogos:
    print(jogo)

for indice, jogo in enumerate(jogos):
    print(f"{indice+1}º: {jogo}")

# COUNT: Conta quantas vezes um item aparece na tupla
objetos = ("lápis", "livro", "sapato", "sapato",)
print(objetos.count("lápis"))
print(objetos.count("sapato"))
print(objetos.count("livro"))

# INDEX: Informa o primeiro índice de determinado item na tupla
print(objetos.index("livro"))
print(objetos.index("sapato"))

# LEN: Retorna o tamanho da tupla
print(len(objetos))
