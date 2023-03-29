from classe_conta import Conta

class ContaCorrente(Conta):
    def __init__(self, id_conta, saldo, limite):
        super().__init__(id_conta, saldo)
        self.limite = limite
        
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
        
    def depositar(self, valor):
        self.saldo += valor
