senha = set([1, 7, 2, 8, 3, 9])
print(senha)

letras = set("melancia")
print(letras)

cores = set(("vermelho", "roxo", "preto", "vermelho"))
print(cores)

formas = {"círculo", "quadrado", "círculo"}
print(formas)

simbolos = {"!", "@", "#", "$"}
simbolos = list(simbolos)
print(simbolos[0])

for simbolo in simbolos:
    print(simbolo)

for indice, simbolo in simbolos:
    print(f"{indice+1}º: {simbolo}")
