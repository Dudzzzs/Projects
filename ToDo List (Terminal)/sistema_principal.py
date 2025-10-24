from funcoes.controle_tarefas import controle_tarefas
from menus import menus

controle_tarefas.titulo('\033[1;35mBem vindo a TO-DO list!\033[m')

while True:
   
   menu = menus.menu_princ()

   if menu == False:
    break
     


