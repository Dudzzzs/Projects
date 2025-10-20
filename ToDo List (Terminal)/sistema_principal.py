from funcoes.controle_usuario import controle_usu
from menus import menus

while True:
    menu = menus.menu_princ()
    
    if menu == False:
        break