from ContasClientesExtratos import ContaEsp
from ContaPoupanca import ContaPoupanca
from Conta import Conta
from Cliente import Cliente
class ContaRemuneracaoPoupanca(ContaEsp, ContaPoupanca):
    def __init__(self, taxaremuneracao,cliente,numeroconta,saldo):
        Conta.__init__(cliente, numeroconta, saldo)
        ContaPoupanca.__init__(self, taxaremuneracao)
        self.taxaremuneracao = taxaremuneracao
    def remuneracaoConta(self):
        self.saldo += self.saldo*(self.taxaremuneracao/30)
        self.saldo -= self.taxaremuneracao


cliente_001 = Cliente(25467874850,'Marcos Carlos','rua 1')
conta_001p = ContaPoupanca(1,1,1000)
ContaPoupanca1 = ContaPoupanca(0.1)
ContaRemuneracaoPoupanca1 = ContaRemuneracaoPoupanca(0.1,cliente_001,5,1000,0)
conta_001p.extrato.extrato_b(conta_001p)