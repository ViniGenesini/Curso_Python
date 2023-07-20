# CLEAR: Apaga todas as chaves/valores do dict
roupas = {
    "camiseta": {"cor": "vermelho", "tamanho": "P"},
    "regata": {"cor": "verde", "tamanho": "GG"},
    "moletom": {"cor": "preto", "tamanho": "PP"},
    "tênis": {"cor": "branco", "tamanho": "41", "extra": {"desconto": "20%"}},
}
roupas.clear()
print(roupas)

# COPY: Gera uma cópia de um dict
roupas = {
    "camiseta": {"cor": "vermelho", "tamanho": "P"},
    "regata": {"cor": "verde", "tamanho": "GG"},
    "moletom": {"cor": "preto", "tamanho": "PP"},
    "tênis": {"cor": "branco", "tamanho": "41", "extra": {"desconto": "20%"}},
}
roupas_2 = roupas.copy()
roupas_2["camiseta"] = {"cor": "amarelo"}

print(roupas["camiseta"])
print(roupas_2["camiseta"])

# FROMKEYS: Cria/altera uma/mais chaves em um dict com um valor padrão
casa = dict.fromkeys(["rua", "número"])
print(casa)
casa = dict.fromkeys(["rua", "número"], "12")
print(casa)

# GET: Retorna o valor de uma chave, mas sem erro caso ele não exista
print(casa.get("bairro"))
print(casa.get("bairro", "informação indisponível!"))
print(casa.get("rua", "informação indisponível"))

# ITEMS: Gera uma lista com as chaves/valores de um dict
print(casa.items())

# KEYS: Gera uma lista com as chaves de um dict
print(casa.keys())

# POP: Remove uma chave/valor de um dict, mas sem erro caso não exista
casa.pop("número")
print(casa)
print(casa.pop("número", "operação inválida!"))

# POPITEM: Remove a ultima chave/valor de um dict
casa = {"rua": "Av. Flores", "numero": "12"}
casa.popitem()
print(casa)

# SETDEFAULT: Adiciona uma chave em um dict, mas sem erro caso exista
casa = {"rua": "Av. Flores", "numero": "12"}
casa.setdefault("rua", "Av. Campos")
print(casa)
casa.setdefault("bairro", "Jardim do Bosque")
print(casa)

# UPDATE: Atualiza/adiciona chaves/valores de um dict
casa.update({"rua": "Av. Rosas"})
print(casa)
casa.update({"cidade": "Jundiaí"})
print(casa)

# VALUES: Gera uma lista com os valores de um dict
print(casa.values())

# IN: Verifica se uma chave/valor está em um dict ou não
print("rua" in casa)
print("estado" in casa)
print("Av. Flores" in casa["rua"])
print("12" in casa["numero"])

# DEL: Deleta uma chave/valor de um dict ou o próprio dict
casa = {"rua": "Av. Flores", "numero": "12", "extra": {"apto": "1234", "bloco": "A"}}
del casa["extra"]["bloco"]
del casa["numero"]
print(casa)
del casa