matriz = [
    [15, "B", 32],
    ["Y", 45, 95],
    [31, 89, "H"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

nome = ["V", "i", "n", "i"]
print(nome[2:])
print(nome[:2])
print(nome[1:3])
print(nome[0:3:2])
print(nome[::])
print(nome[::-1])

for letra in nome:
    print(letra)

for indice, letra in enumerate(nome):
    print(f"{indice+1}ª letra: {letra}")