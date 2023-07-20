# UNION: Une os valores de dois sets em um só
america_do_sul = {"Brasil", "Argentina"}
america_do_norte = {"EUA", "Canadá"}
americas = america_do_sul.union(america_do_norte)
print(americas)

# INTERSECTION: Retorna os valores em comum entre dois sets
europa = {"França", "Inglaterra", "Escócia"}
reino_unido = {"Inglaterra", "Escócia", "Gales"}
paises = europa.intersection(reino_unido)
print(paises)

# DIFFERENCE: Retorna os valores do set 2 que não estão no set 1
contagem = {56, 23, 95}
total = {54, 23, 95}

diferenca_1 = contagem.difference(total)
diferenca_2 = total.difference(contagem)
print(diferenca_1)
print(diferenca_2)

# SYMMETRIC_DIFFERENCE: Retorna os valores diferentes entre dois sets
diferenca_3 = contagem.symmetric_difference(total)
diferenca_4 = total.symmetric_difference(contagem)
print(diferenca_3)
print(diferenca_4)

# ISSUBSET: Verifica se um set está ou não dentro de outro set maior
pares = {2, 4, 6, 8, 10}
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(pares.issubset(numeros))
print(numeros.issubset(pares))

# ISSUPERSET: Verifica se um set está ou não dentro de outro set menor
print(pares.issuperset(numeros))
print(numeros.issuperset(pares))

# ISDISJOINT: Verifica se um set possui ou não valores de outro set
impares = {1, 3, 5, 7, 9}
print(pares.isdisjoint(impares))
print(pares.isdisjoint(numeros))

# ADD: Adiciona um item ao set sem repeti-lo
pares.add(12)
pares.add(14)
pares.add(12)
print(pares)

# CLEAR: Apaga todos os itens do set
impares.clear()
print(impares)

# COPY: Gera uma cópia de um set
numeros_2 = numeros.copy()
print(numeros_2)

# DISCARD: Apaga um item do set
numeros.discard(10)
numeros.discard(34)
print(numeros)

# POP: Apaga o primeiro valor do set
numeros_2.pop()
numeros_2.pop()
print(numeros_2)

# REMOVE: Apaga um item do set (mas da erro se o item não existir)
numeros.remove(1)
print(numeros)

# LEN: Retorna o tamanho do set
print(len(numeros))
print(len(numeros_2))

# IN: Verifica se um item está em um set ou não
print(2 in numeros)
print(1 in numeros_2)