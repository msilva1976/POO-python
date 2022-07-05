from Cliente import Cliente
from ContasClientesExtratos import ContaEsp
from Conta import Conta
from Extrato import Extrato
import datetime

class ContaEspecial(Conta):
    def __init__(self, cliente, numeroconta, saldo, limite):
        Conta.__init__(Conta,cliente,numeroconta,saldo)
        #Conta.__init__(cliente, numeroconta, saldo)
        self.limite = limite
    def sacar(self, valor):
        if (self.saldo + self.limite)<valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['SAQUE', valor, 'Data',datetime.datetime.today()])
            return True

cliente_001 = Cliente(25437874880,'Marcos Carlos','Rua 1')
cliente_002 = Cliente(25689547520,'Monica Queiros','Rua3')
cliente_003 = Cliente(10354684841,'Maria das Graças','Rua4')
cliente_004 = Cliente (25689745210,'Marcia Regina','Rua 10')
conta_001 = Conta(cliente_001,1,2000)
conta_002 = Conta(cliente_002,2,5000)
conta_004 = Conta(cliente_001,4,6000)
conta_003 = ContaEspecial([cliente_003],3,1000,2000)
conta_001.gerarSaldo()
conta_002.gerarSaldo()
conta_003.gerarSaldo()
conta_004.gerarSaldo()
conta_003.gerar_extrato()
conta_003.depositar(2000)
conta_003.depositar(56210)
conta_003.sacar(58220)
conta_003.sacar(10000)
conta_003.sacar(1000)
conta_003.sacar(2000)
conta_003.depositar(10000)
conta_003.sacar(1000)
conta_003.gerarSaldo()
conta_003.extrato.extrato_b(conta_003.numeroconta)

