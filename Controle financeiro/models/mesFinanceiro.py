class MesFinanca:

    def __init__(self, nome):
        self.nome = nome
        self.transacoes = []
        self.entradas = 0
        self.saidas = 0
        self.contador = 0
        self.saldo = 0

    def salvar_trans(self, trans):
        if trans.tipo.lower() == 'entrada':
            self.entradas += trans.valor
            self.saldo += trans.valor
        elif trans.tipo.lower() == 'saida':
            self.saidas += trans.valor
            self.saldo -= trans.valor

        self.contador += 1

        self.transacoes.append(trans)
        print('Transação adicionada com sucesso!')

    def relatorio_simplificado(self):
        print(f'{self.contador} transações // R${self.entradas} entraram // R${self.saidas} saíram // R${self.saldo} de saldo final.')

    

