import json

class Usuario:
    
    def __init__(self, nome, salvar=False):
        self.nome = nome
        self.transacoes = {}
        self.salvar = salvar

        if not self.salvar:
            try: 
                with open(f'{self.nome}.json', 'x', encoding='utf-8') as arquivo:
                    json.dump(self.transacoes, arquivo, indent=4, ensure_ascii=False)

                print(f'\033[1;32mUsuário {self.nome} cadastrado com sucesso!\033[m')
            except FileExistsError:
                print('\033[1;31mEsse usuário já existe!\033[m')\
            

class Transacao:

    def __init__(self, id, data, tipo, valor, categoria):
        self.id = id
        self.data = data
        self.tipo = tipo
        self.valor = valor
        self.categoria = categoria

    def cadastrar_transacao(self, usuario, mes):

        with open(f'{usuario}.json', 'r') as arquivo:
            load = json.load(arquivo)

        if len(load) == 0:
            novo_mes = input('\033[1;34mEm qual mês deseja cadastrar a transação?\033[m \n').title()

            load.update({f'{novo_mes}': {}})
            load[novo_mes].update({'id': 1})
            load[novo_mes].update({'transacoes': []})

            print('\033[1;32mMês cadastrado com sucesso!\033[m')

            with open(f'{usuario}.json', 'w', encoding='utf-8') as arquivo:
                json.dump(load, arquivo, indent=4, ensure_ascii=False)
        else:
            while True:
                print('\033[1;35mMeses cadastrados:\033[m')

                keys = []
                for m in list(load.keys()):
                    keys.append(m)
                    print(f'\033[1;34m{m}\033[m\n')
                    
                mes_escol = input('\033[1;34mEm qual mês deseja cadastrar a transação?\033[m \n').title()

                if mes_escol in keys:
                    load[f"{mes_escol}"]["transacoes"].append('Transacao')

                    print('\033[1;32mTransação salva com sucesso\033[m')

                    with open(f'{usuario}.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(load, arquivo, indent=4, ensure_ascii=False)
                    
                    break
                
                else:
                    print('\033[1;31mMês não cadastrado')

class Mes:
    pass


            


            

            
        
        
        

