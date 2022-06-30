from Conta import Conta
from Cliente import Cliente
cliente_001 = Cliente(254378474880,'Marcos Carlos','Rua joão Franco 115a')
cliente_002 = Cliente(10354684841,'Maria Das Graças','Av. Expedicionario 01')

conta_001 = Conta(cliente_001, 1,1000)
conta_002 = Conta(cliente_002,2,15000)
cliente_001.imprimirCliente()
conta_001.depositar(2000)
conta_001.gerar_extrato()
cliente_002.imprimirCliente()
conta_002.depositar(2000)
conta_002.gerar_extrato()


