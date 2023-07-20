# NOME_FUNCAO(POSIÇÃO / POSIÇÃO OU CHAVE-VALOR * CHAVE-VALOR)


def cadastrar_pessoa(nome, data_nascimento, idade, /, cpf, rg, cnh):
    print(nome, data_nascimento, idade, cpf, rg, cnh)

cadastrar_pessoa(
    "Vinicius", 
    "29/11/2004", 
    18,
    cpf = "123.456.789-00",
    rg = "12.345.678-90",
    cnh = "53421"
)

def cadastrar_pessoa_2(*, nome, data_nascimento, idade, cpf, rg, cnh):
    print(nome, data_nascimento, idade, cpf, rg, cnh)

cadastrar_pessoa_2(
    nome = "Vinicius",
    data_nascimento = "29/11/2004",
    idade = 18,
    cpf = "123.456.789-00",
    rg = "12.345.678-90",
    cnh = "53421"
)

def cadastrar_pessoa_3(nome, data_nascimento, idade, /, *, cpf, rg, cnh):
    print(nome, data_nascimento, idade, cpf, rg, cnh)

cadastrar_pessoa_3(
    "Vinicius",
    "29/11/2004",
    18,
    cpf = "123.456.789-00",
    rg = "12.345.678-90",
    cnh = "53421"
)

def subtrair(x, y):
    return x - y

def somar(x, y):
    return x + y

def resultado(x, y, funcao):
    resultado = funcao(x, y)
    print(f"RESULTADO: {resultado}")

resultado(13, 7, subtrair)
resultado(13, 7, somar)

op = somar
print(op(32, 9))

preco = 320
def promocao(desconto):
    global preco
    preco -= desconto
    return preco

print(promocao(40))
