from datetime import datetime
from time import strftime
from Conta import Conta
from ContaEspecial import ContaEspecial
from ContaPoupanca import ContaPoupanca
from ContaRemuneradaPoupanca import ContaRemuneracaoPoupanca
from Cliente import Cliente


class Extrato:
    def __init__(self):
        self.transacoes = []

    def extrato_b(self, numeroconta):
        
        print(f'Extrato : {numeroconta}\n')

        for p in self.transacoes:
                print(f'{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3]}')


         