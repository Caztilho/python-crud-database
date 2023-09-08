import mysql.connector
from prettytable import PrettyTable

from database_disciplinas import disciplinas
from database_professores_project import professores
from database_disciplinasprofessores_project import disciplinas_professores

while True:
    try:

        resp = int(input("\nQUAL DATABASE VOCÊ DESEJA ACESSAR?\n[1] DISCIPLINAS\n[2] PROFESSORES\n[3] DISCIPLINAS X PROFESSORES\n[4] SAIR\n"))

        if resp == 1:
            disciplinas()
        elif resp == 2:
            professores()
        elif resp == 3:
            disciplinas_professores()
        elif resp == 4:
            print("\nSAINDO...")
            break
        else:
            print('DIGITE APENAS OS PROGRAMAS LISTADOS!!!\n')
    
    except ValueError:
            print('\nDIGITE APENAS O QUE É PEDIDO!!!\n')

            if input('Deseja continuar? S [SIM] | N [NÃO]: ') != 'S':
                break

    except Exception as erro:
        print(f"Erro: {erro}")

        if input('Deseja continuar? S [SIM] | N [NÃO]: ') != 'S':
            break