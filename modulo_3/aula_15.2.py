class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18

p = Pessoa("Vini", 18)
print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(2004, 11, 29, "Vini")
print(p2.nome, p2.idade)

print(Pessoa.maior_de_idade(18))
print(Pessoa.maior_de_idade(8))
