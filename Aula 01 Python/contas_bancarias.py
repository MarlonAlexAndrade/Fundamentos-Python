'''
Criar uma classe chamada Conta, com os seguintes atributos e funções
atributos: Código, proprietario, agencia, saldo
funções: exibir saldo, depositar, sacar
'''
import arrow

class Conta:
    def __init__(self, codigo, proprietario, agencia):
        self.codigo = codigo
        self.proprietario = proprietario
        self.agencia = agencia
        self.saldo = 0
        self.extrato = []

    def exibir_saldo(self):
        print(f'Saldo Atual: R${self.saldo}')

    def depositar(self, valor_deposito):
        data = arrow.now().format('DD/MM/YYYY HH:mm')
        self.saldo += valor_deposito
        self.extrato.append(['Crédito', valor_deposito, self.saldo, data])

    #   Extrato: Movimentação (entrada/saida)
    #            Valor da Movimentação
    #            Saldo após a Movimentação
    #            Valor da Movimentação
    def sacar(self, valor_saque):
        if self.saldo < valor_saque:
            print('Você nao tem saldo')
        else:
            data = arrow.now().format('DD/MM/YYYY HH:mm')
            self.extrato.append(['Débito', valor_saque, self.saldo, data])
            self.saldo -= valor_saque

    def exibir_extrato(self):
        for i in self.extrato:
            print(i)


c1 = Conta('123', 'Marlon Alex Andrade', '135')
c1.depositar(100)
c1.sacar(50)
c1.exibir_extrato()
