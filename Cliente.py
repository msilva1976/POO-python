class Cliente:


    def __init__(self, cpf, nome, endereço):
        self.cpf = cpf
        self.nome = nome
        self.endereço = endereço


    def imprimirCliente(self) -> object:
        print('----------------------------------------')
        print('Nome do cliente: {}'.format(self.nome))
        print('CPF: {}'.format(self.cpf))
        print('Endereço: {}'.format(self.endereço))

