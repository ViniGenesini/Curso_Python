texto = ""
VOGAIS = "AEIOU"


# ITERÁVEL
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()


# FUNÇÃO BUILT-IN range()
for numero in range(0, 51, 5):
    print(numero, end=" ")
