from funcoes.controle_usuario import controle_usu
from funcoes.controle_tarefas import controle_tarefas

def menu_princ():
    prog_princ = int(input('O que você deseja fazer hoje? \n1: Cadastrar usuário; \n2: Login; \n3: Excluir usuário; \n4: Finalizar programa. \n'))

    match prog_princ:
        case 1:
            nome_usu = input('\033[1;34mQual nome de usuário você deseja cadastrar?\033[m\n')
            controle_usu.cadastro(nome_usu)
        case 2:
            nome_usu = input('\033[1;34mQual seu nome de usuário?\033[m\n')
            
            if controle_usu.login(nome_usu):
                
                while True:
                    verif = menu_tarefa(nome_usu)
                    
                    if verif ==  False:
                        break
                
        case 3:
            nome_usu = input('\033[1;34mQual usuário deseja excluir?\033[m\n')
            controle_usu.excluir(nome_usu)
        case 4:
            print('\033[1;31mPrograma finalizado!\033[m')
            return False
        case _:
            print('\033[1;33mOpção inválida.\033[m')

def menu_tarefa(nome_usu):

        menu_tarefa = int(input('O que deseja fazer? \n1: Criar tarefa; \n2: Exibir tarefas; \n3: Editar tarefa; \n4: Concluir tarefa; \n5: Excluir tarefa; \n6: Finalizar programa.\n'))

        match menu_tarefa:
            case 1:
                controle_tarefas.criar_tarefa(nome_usu)
            case 6:
                print('\033[1;31mPrograma finalizado!\033[m')
                return False
            case _:
                print('\033[1;33mOpção inválida.\033[m')
