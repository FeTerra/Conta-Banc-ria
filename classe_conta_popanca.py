from classe_conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, id_conta, saldo):
        super().__init__(id_conta, saldo)
        
    # Sei que não foi pedido, mas criei esta forma de calcular a taxa de rendimento para ficar mais realista:
    def calcular_taxa_de_rendimento(self):
        tabela_taxas = {
            (0, 1000): 0.005, # 0,5%
            (1000, 5000): 0.01, # 1%
            (5000, 10000): 0.015, # 1,5%
            (10000, None): 0.02 # 2%
        }
        
        for intervalo, taxa in tabela_taxas.items():
            if intervalo[0] <= self.saldo < intervalo[1] or intervalo[1] is None and self.saldo >= intervalo[0]:
                return taxa
        
    def verificar_rendimento_ao_ano(self):
        taxa_de_rendimento = self.calcular_taxa_de_rendimento()
        rendimento = self.saldo * taxa_de_rendimento
        return rendimento
        
    def depositar(self, valor):
        self.saldo += valor
        rendimento = self.verificar_rendimento_ao_ano()
        self.saldo += rendimento
        
    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            rendimento = self.verificar_rendimento_ao_ano()
            self.saldo += rendimento