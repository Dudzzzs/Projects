import json

def criar_tarefa(nome_usu):
    
    with open(f'{nome_usu}.json', 'r') as arquivo:
        objeto = json.load(arquivo)
        
    id_tarefa = objeto["id"]

    tarefa = {
            "id": id_tarefa,    
            "tarefa": "",
            "data": "",
            "status": "Pendente"    
        }
    
    
    tarefa["tarefa"] = input('\033[1;34mQual nome da tarefa?\033[m \n')
    tarefa["data"] = input('\033[1;34mQual a data da tarefa? DD/MM/AAAA\033[m \n')

    objeto["tarefas"].append(tarefa.copy())

    objeto['id'] += 1
        
    with open(f'{nome_usu}.json', 'w') as arquivo:
        json.dump(objeto, arquivo, indent=4, ensure_ascii=True)

    print('\033[1;32mTarefa cadastrada com sucesso!\033[m')



