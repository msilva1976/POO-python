import datetime
from Extrato import Extrato

class Conta:
    def __init__(self,cliente,numeroconta,saldo):
        self.cliente = cliente
        self.numeroconta = numeroconta
        self.saldo = saldo 
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()       

    def depositar(self,valor):
        self.saldo += valor
        self.extrato.transacoes.append(['DEPOSITO',valor,'Data', datetime.datetime.today()])

    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['SAQUE',valor,'Data', datetime.datetime.today()])

        return True

    def gerar_extrato(self):
        print('------------extrato da conta------------') 
        print("numero: {} ".format(self.numeroconta)) 
        print('Saldo: R$ {}'.format(self.saldo))
        
    def transferenciaValores(Self,contaDestino,valor):
        if Self.saldo < valor:
            return('Saldo insuficiente')
        else:
            contaDestino.depositar(valor)
            Self.saldo -= valor
            Self.extrato.transacoes.append(['TRANSFERENCIA',valor,'Data', datetime.datetime.today()])
        return('transferencia realizada')
    def gerarSaldo(self):
        print('Numero: {}'.format(self.numeroconta))
        print('Saldo: {}'.format(self.saldo))
        print('----------------------------------------')
    
    
