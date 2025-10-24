import json
import os
from funcoes.controle_tarefas import controle_tarefas

def cadastro(nome_usu):
    """
        - Função que 'cadastra o usuário' criando um arquivo .JSON com o nome escolhido. Cada vez que é criado um usuário ele cria o JSON com uma estrutura inicial que consiste em um contador de ID de tarefas e uma lista para adicionar aas tarefas cadastradas.
    """
    try:
        with open(f'{nome_usu}.json', 'x', encoding='utf-8') as arquivo:
            estrutura_inicial = {
                "id": 1,
                "tarefas": []
            }

            json.dump(estrutura_inicial, arquivo, indent=4, ensure_ascii=False)

            controle_tarefas.titulo('\033[1;32mUsuário cadastrado com sucesso!\033[m')

    except FileExistsError:
        controle_tarefas.titulo('\033[1;31mEsse usuário já foi cadastrado.\033[m')


def login(nome_usu):
    """
        - Função que realiza o login do usuário. Consiste em verificar se existe um arquivo JSON com o nome de usuário. Caso não exista é criada a opção de cadastrar.
    """
    try:
        with open(f'{nome_usu}.json', 'r', encoding='utf-8') as arquivo:
            arquivo.read()
            controle_tarefas.titulo('\033[1;32mLogin concluído com sucesso!\033[m')
            return True
    except:
        controle_tarefas.titulo('\033[1;33mNão foi encontrado seu usuário. Deseja realizar o cadastro? (S/N) \033[m')
        opcao = input().upper()

        
        if opcao == 'S':
            cadastro(nome_usu)
        else:
            return False


def excluir(nome_usu):
    """
        - Função que exclui o arquivo JSON escolhido.
    """
    try:
        os.remove(f'{nome_usu}.json')
        controle_tarefas.titulo('\033[1;32mUsuário excluído com sucesso!\033[m')
    except FileNotFoundError:
        controle_tarefas.titulo('\033[1;31mUsuário não encontrado.\033[m')
    


    


