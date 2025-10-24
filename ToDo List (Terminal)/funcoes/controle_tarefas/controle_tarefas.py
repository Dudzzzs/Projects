import json

def criar_tarefa(nome_usu):
    """
        - Essa função cria um tarefa com nome e data escolhidos pelo usuário e adiciona ao arquivo .JSON de seu respectivo usuário.
    """
    
    with open(f'{nome_usu}.json', 'r', encoding='utf-8') as arquivo:
        objeto = json.load(arquivo)
        
    id_tarefa = objeto["id"]

    tarefa = {
            "id": id_tarefa,    
            "tarefa": "",
            "data": "",
            "status": "Pendente"    
        }
    
    
    tarefa["tarefa"] = input('\033[1;34mQual nome da tarefa?\033[m \n').title()
    tarefa["data"] = input('\033[1;34mQual a data da tarefa? DD/MM/AAAA\033[m \n')

    objeto["tarefas"].append(tarefa.copy())

    objeto['id'] += 1
        
    with open(f'{nome_usu}.json', 'w', encoding='utf-8') as arquivo:
        json.dump(objeto, arquivo, indent=4, ensure_ascii=False)
    
    titulo('\033[1;32mTarefa cadastrada com sucesso!\033[m')


def exibir_tarefas(nome_usu):
    """
        - Essa função exibe todas as tarefas cadastradas do respectivo usuário, caso não haja nenhuma tarefa cadastrada ele exibe a mensagem "Nenhuma tarefa cadastrada".
    """

    titulo('\033[1;33mExibindo tarefas\033[m')

    with open(f'{nome_usu}.json', 'r',encoding='utf-8') as arquivo:
        load = json.load(arquivo)

    if len(load["tarefas"]) == 0:
        titulo('\033[1;31mAinda não foi cadastrada nenhuma tarefa!\033[m')
    else:

        for t in load["tarefas"]:
            if t["status"] == 'Pendente':
                print(f'id: {t["id"]}\ntarefa: {t["tarefa"]}\ndata: {t["data"]}\nstatus: \033[1;31m{t["status"]}\033[m')
                print('=' *20)
            else:
                print(f'id: {t["id"]}\ntarefa: {t["tarefa"]}\ndata: {t["data"]}\nstatus: \033[1;32m{t["status"]}\033[m')
                print('=' *20)  


def editar_tarefa(nome_usu):
    """
        - Essa função edita a tarefa escolhida pelo respectivo usuário, caso não haja nenhuma tarefa cadastrada ele exibe a mensagem "Nenhuma tarefa cadastrada".
    """

    with open(f'{nome_usu}.json', 'r', encoding='utf-8') as arquivo:
        load = json.load(arquivo)
    
    if len(load["tarefas"]) == 0:
        titulo('\033[1;31mAinda não foi cadastrada nenhuma tarefa!\033[m')
    else: 
        exibir_tarefas(nome_usu) 

        id_tarefa_edit = int(input('\033[1;34mQual ID da tarefa que deseja editar?\033[m \n'))

        tarefa_encontrada = False

        for t in load["tarefas"]:
            if t["id"] == id_tarefa_edit:

                tarefa_encontrada = True

                print(f'{t["id"]} | {t["tarefa"]} | {t["data"]} ')

                opcao = int(input('\033[1;34mO que deseja editar? \n1: Nome da tarefa; \n2: Data.\033[m \n'))

                match opcao:
                    case 1:
                        t["tarefa"] = input('\033[1;34mQual o nome deseja inserir?\033[m \n').title()
                    
                    case 2: 
                        t["data"] = input('\033[1;34mQual o data deseja inserir? (DD/MM/AAAA)\033[m \n')
                
                titulo('\033[1;32mTarefa editada com sucesso!\033[m')

        if tarefa_encontrada == False:
            titulo('\033[1;31mTarefa não encontrada!\033[m')
        else:
            with open(f'{nome_usu}.json', 'w', encoding='utf-8') as arquivo:
                json.dump(load, arquivo, indent=4, ensure_ascii=False)


def concluir_tarefa(nome_usu):
    """
        - Essa função marca como 'concluída' a tarefa escolhida pelo respectivo usuário, caso não haja nenhuma tarefa cadastrada ele exibe a mensagem "Nenhuma tarefa cadastrada".
    """

    with open(f'{nome_usu}.json', 'r', encoding='utf-8') as arquivo:
        load = json.load(arquivo)

    if len(load["tarefas"]) == 0:
        titulo('\033[1;31mAinda não foi cadastrada nenhuma tarefa!\033[m')
    else: 
        exibir_tarefas(nome_usu)

        id_tarefa_concl = int(input('\033[1;34mQual ID da tarefa que deseja concluir?\033[m \n'))

        tarefa_encontrada = False

        for t in load["tarefas"]:
            if t["id"] == id_tarefa_concl:
                
                tarefa_encontrada = True
                t["status"] = 'Concluído'

                titulo('\033[1;32mTarefa concluída com sucesso!\033[m')

        if tarefa_encontrada == False:
            titulo('\033[1;31mTarefa não encontrada!\033[m')
        else:
            with open(f'{nome_usu}.json', 'w', encoding='utf-8') as arquivo:
                json.dump(load, arquivo, indent=4, ensure_ascii=False)


def excluir_tarefa(nome_usu):
    """
        - Essa função exclui a tarefa escolhida pelo respectivo usuário, caso não haja nenhuma tarefa cadastrada ele exibe a mensagem "Nenhuma tarefa cadastrada."
    """

    with open(f'{nome_usu}.json', 'r', encoding='utf-8') as arquivo:
        load = json.load(arquivo)

    if len(load["tarefas"]) == 0:
        titulo('\033[1;31mAinda não foi cadastrada nenhuma tarefa!\033[m')
    else:
        exibir_tarefas(nome_usu)

        id_tarefa_excl = int(input('\033[1;34mQual ID da tarefa que deseja excluir?\033[m \n'))

        tarefa_encontrada = False

        for i, t in enumerate(load["tarefas"]):
            if t["id"] == id_tarefa_excl:
                tarefa_encontrada = True
                del load["tarefas"][i]
                load["id"] -= 1

                for ta in load["tarefas"]:
                    if ta["id"] > id_tarefa_excl:
                        ta["id"] -= 1

                titulo('\033[1;32mTarefa concluída com sucesso!\033[m')

        if tarefa_encontrada == False:
            titulo('\033[1;31mTarefa não encontrada!\033[m')
        else:
            with open(f'{nome_usu}.json', 'w', encoding='utf-8') as arquivo:
                json.dump(load, arquivo, indent=4, ensure_ascii=False)


def titulo(frase):
    """
        - Função criada apenas para melhorar a exibição no terminal de frases importantes na execução do programa
    """
    largura = len(frase) + 10
    print('=' * largura)
    print(frase.center(largura))
    print('=' * largura)
   







