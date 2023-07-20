pessoa = {"nome": "Vinicius", "idade": 18}
pessoa = dict(nome="Vinicius", idade=28)

pessoa["celular"] = "+55 (11) 91234-5678"
print(pessoa)

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["celular"])

pessoa["nome"] = "Alexandre"
pessoa["idade"] = 48
pessoa["celular"] = "+55 (11) 98765-4321"
print(pessoa)

roupas = {
    "camiseta": {"cor": "vermelho", "tamanho": "P"},
    "regata": {"cor": "verde", "tamanho": "GG"},
    "moletom": {"cor": "preto", "tamanho": "PP"},
    "tênis": {"cor": "branco", "tamanho": "41", "extra": {"desconto": "20%"}},
}
print(roupas["regata"]["tamanho"])
print(roupas["tênis"]["extra"]["desconto"])

for chave in roupas:
    print(chave, roupas[chave])

for chave, valor in roupas.items():
    print(chave, valor)
