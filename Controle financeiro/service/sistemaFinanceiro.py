from models import transacao
from models import mesFinanceiro


class Sistema:

    def __init__(self):
        self.meses = []

    def criar_mes(self, nome):
        novo_mes = mesFinanceiro.MesFinanca(nome)
        self.meses.append(novo_mes)
        print(f'Mês {nome} criado com sucesso!')

    def buscar_mes(self, nome):
        for mes in self.meses:
            if nome == mes.nome:
                print('Mês encontrado com sucesso!')
                return mes

        print('Esse mês ainda não foi cadastrado!')
        return None
    
    def cadastrar_trans(self, valor, tipo, descricao):
        mes = mesFinanceiro.MesFinanca()
        trans = transacao.Transacao(valor, tipo, descricao)
        mes.salvar_trans(trans)
        