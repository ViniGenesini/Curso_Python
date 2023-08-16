class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia
    
    def Depositar(self, valor):
        self._saldo += valor

    def Sacar(self, valor):
        self._saldo -= valor

    def Mostrar_Saldo(self):
        return self._saldo

conta = Conta("0001", 100)
conta.Depositar(100)
print(conta.numero_agencia)
print(conta.Mostrar_Saldo())
