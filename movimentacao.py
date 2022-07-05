from Cliente import Cliente
from Conta import Conta
from Extrato import Extrato
cliente_001 = Cliente(254378474880,'Marcos Carlos','Rua joão Franco 115a')
cliente_002 = Cliente(10354684841,'Maria das Graças','Av expedicionarios')
cliente_003 = Cliente(20325132650,'Monica Queiros','Rua quinze')
conta_003 = Conta('Monica Queiros',3,3000)
conta_003.depositar(2000)
conta_003.sacar(100)

conta_001 = Conta('Marcos Carlos da Silva',1,2000)
conta_001.depositar(50000)
conta_001.depositar(562142)
conta_001.sacar(1240)
conta_002 = Conta('Maria das Graças Costa',2,10000)
conta_002.depositar(521425)
conta_001.transferenciaValores(conta_002,500)
conta_002.depositar(521425)
conta_001.transferenciaValores(conta_002,500)
conta_002.depositar(521425)
conta_001.transferenciaValores(conta_002,500)
conta_002.extrato.extrato_b(conta_002.numeroconta)
conta_001.gerarSaldo()
conta_003.extrato.extrato_b(conta_003.numeroconta)
conta_001.depositar(3000)
conta_001.extrato.extrato_b(conta_001.numeroconta)










