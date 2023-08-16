class Pessoa:
    def __init__(self, nome, ano_de_nascimento):
        self.nome = nome
        self._ano_de_nascimento = ano_de_nascimento
    
    @property
    def Idade(self):
        _ano_atual = 2023
        return _ano_atual - self._ano_de_nascimento
    
pessoa = Pessoa("Vinicius", 2004)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.Idade}")
