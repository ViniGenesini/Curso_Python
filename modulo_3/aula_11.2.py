class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe...")
    
    def falar(self):
        print("AUAU!")

def criar_cachorro():
    c = Cachorro("Bob", "Rosa", False)
    print(c.nome)

print("teste")
c = Cachorro("Rex", "azul")
c.falar()

print("teste")
del c
print("teste")
print("teste")
print("teste")
print("teste")

# criar_cachorro()

# __INIT__: É sempre executado ao criar uma instância, sendo o primeiro método executado
# __DEL__: E sempre exectuado no fim do código, sendo o último método executado
