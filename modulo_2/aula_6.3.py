numeros = [54, 89, 46, 1, 33, 90, 47]

impares = []
for numero in numeros:
    if numero % 2 == 1:
        impares.append(numero)

pares = [numero for numero in numeros if numero % 2 == 0]

quadrado = []
for numero in numeros:
    quadrado.append(numero**2)

cubo = [numero**3 for numero in numeros]
