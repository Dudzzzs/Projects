from models import transacao
from models import mesFinanceiro
from service import sistemaFinanceiro

sistema = sistemaFinanceiro.Sistema()
sistema.criar_mes('Janeiro')
mes_e = sistema.buscar_mes('Janeiro')

sistema.cadastrar_trans(500, 'entrada', 'mercado')



