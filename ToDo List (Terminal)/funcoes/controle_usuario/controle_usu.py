import json
import os

def cadastro(nome_usu):
    try:
        with open(f'{nome_usu}.json', 'x') as arquivo:
            estrutura_inicial = {
                "id": 1,
                "tarefas": []
            }

            json.dump(estrutura_inicial, arquivo, indent=4, ensure_ascii=True)
            print('\033[1;32mUsuário cadastrado com sucesso!\033[m')
    except FileExistsError:
        print('\033[1;31mEsse usuário já foi cadastrado.\033[m')


def login(nome_usu):
    try:
        with open(f'{nome_usu}.json', 'r') as arquivo:
            arquivo.read()
            print('\033[1;32mLogin concluído com sucesso!\033[m')
            return True
    except:
        opcao = input('\033[1;33mNão foi encontrado seu usuário. Deseja realizar o cadastro? (S/N) \033[m').upper()
        
        if opcao == 'S':
            cadastro(nome_usu)
        else:
            return False
        
def excluir(nome_usu):
    try:
        os.remove(f'{nome_usu}.json')
        print('\033[1;32mUsuário excluído com sucesso!\033[m')
    except FileNotFoundError:
        print('\033[1;31mUsuário não encontrado.\033[m')
    


    


