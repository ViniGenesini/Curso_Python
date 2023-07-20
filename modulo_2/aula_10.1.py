def mensagem_aniversario():
    print("Feliz aniversário!")

def mensagem_aniversario_2(nome):
    print(f"Feliz aniversário, {nome}!")

def mensagem_aniversario_3(nome="Anônimo"):
    print(f"Feliz aniversário, {nome}!")

mensagem_aniversario()
mensagem_aniversario_2(nome="Vinicius")
mensagem_aniversario_3()
mensagem_aniversario_3(nome="Alexandre")

def calcular_soma(numeros):
    return sum(numeros)

def multiplica_e_divide_por_5(numero):
    multiplicacao = numero * 5
    divide = numero / 5
    return multiplicacao, divide

def teste():
    print("teste!")

print(calcular_soma([13, 87, 51]))
print(multiplica_e_divide_por_5(10))
teste()
print(teste())

def salvar_casa(cor, rua, numero, cep):
    print(f"Casa inserida com sucesso! {cor}/{rua}/{numero}/{cep}")

salvar_casa("Cinza", "Rua Tigres", "13", "12345-67")
salvar_casa(cor="Vermelho", rua="Rua Leões", numero="33", cep="76543-21")
salvar_casa(**{"cor": "Azul", "rua": "Rua Onças", "numero": "15", "cep": "64753-21"})

# *ARGS: Retorna um parâmetro em forma de tupla
# **KWARGS: Retorna um parâmetro em forma de dicionário
