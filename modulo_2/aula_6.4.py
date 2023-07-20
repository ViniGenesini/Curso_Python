# APPEND: Adiciona o item ao fim da array
lista = []

lista.append(0)
lista.append("Vinicius")
lista.append([39, 2, 76])

print(lista)

# CLEAR: Apaga todos os itens da array
lista.clear()
print(lista)

# COPY: Cria uma array independente copiando os itens de outra array
lista = [0, "Vinicius", [39, 2, 76]]

lista_2 = lista.copy()
print(id(lista), id(lista_2))

lista_2[0] = 3
print(lista, lista_2, sep="\n")

# COUNT: Conta a quantidade de vezes em que um elemento aparece
meses = ["outubro", "abril", "maio", "abril", "dezembro"]

print(meses.count("outubro"))
print(meses.count("abril"))
print(meses.count("dezembro"))

# EXTEND: Adiciona uma array ao fim de outra array
print(meses)
meses.extend(["novembro", "fevereiro", "abril"])
print(meses)

# INDEX: Retorna o índice da primeira ocorrência de um item numa array
print(meses.index("novembro"))
print(meses.index("dezembro"))
print(meses.index("abril"))

# POP: Apaga pelo índice algum item (ou último, por padrão) da array
print(meses.pop())
print(meses.pop())
print(meses.pop(0))
print(meses)

# REMOVE: Apaga, pelo próprio item, sua primeira ocorrência numa array
meses.remove("maio")
print(meses)

# REVERSE: Faz o espelhamento da array
meses.reverse()
print(meses)

# SORT: Ordena os itens da array (alfabética, crescente, etc...)
meses.sort()
print(meses)

meses.sort(reverse=True)
print(meses)

meses.sort(key = lambda x: len(x))
print(meses)
meses.sort(key = lambda x: len(x), reverse=True)
print(meses)

# SORTED: Ordena os itens da array, mas é uma função

print(sorted(meses, key=lambda x: len(x)))
print(sorted(meses, key=lambda x: len(x)), reverse=True)

# LEN: Retorna o tamanho de um objeto iterável
idiomas = ["Português", "Inglês", "Espanhol", "Mandarim", "Francês"]
print(len(idiomas))

