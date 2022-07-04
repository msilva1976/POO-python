from Cliente import Cliente
class Conta:
    def __init__(self,cliente,numero,saldo):
        self.cliente = cliente
        self.numero = numero 
        self.saldo = saldo 
    def depositar(self,valor):
        self.saldo += valor

def sacar(self,valor):
    if self.saldo < valor:
        print('saldo insuficiente, saque não realizado')
    else:
        self.saldo -= valor
    return True

def gerar_extrato(self):
    print('------------extrato da conta------------') 
    print("numero: {} ".format(self.numero)) 
    print('Saldo: R$ {}'.format(self.saldo))
def transferenciaValores(Self,contaDestino,valor):
    if Self.saldo < valor:
        return('Saldo insuficiente')
    else:
        contaDestino.depositar(valor)
        Self.saldo -= valor
    return('transferencia realizada')
def gerarSaldo(self):
    print('Numero: {}'.format(self.numero))
    print('Saldo: {}'.format(self.saldo))
    print('----------------------------------------')