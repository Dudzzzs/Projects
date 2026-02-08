class Transacao:

    def __init__(self, valor, tipo, descricao):
        self.valor = float(valor)
        self.tipo = tipo
        self.descricao = descricao

    def exibir_trans(self):
        print(f'Transação de valor R${self.valor}, de tipo {self.tipo} e descrição: {self.descricao} ')

    def __str__(self):
        return f'Transação de valor R${self.valor}, de tipo {self.tipo} e descrição: {self.descricao} '