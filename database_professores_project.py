import mysql.connector 
from prettytable import PrettyTable 

def professores():
    while True:
        try:
            
            question = int(input("\nO que você deseja fazer na tabela 'Professores':\n[1] CADASTRO \n[2] ALTERAÇÃO \n[3] EXCLUSÃO \n[4] CONSULTA A REGISTROS\n[5] SAIR\n"))

            #! CONSULTA
            #! CONSULTA
            #! CONSULTA

            if question == 1:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')

                if conexao.is_connected():
                    comandosql = conexao.cursor()
                    cd = int(input("\nCodigo do professor: "))
                    nd = input("Nome do professor: ")
                    tel = input("Telefone do professor: ")
                    age = int(input(("Idade do professor: ")))
                    cash = float(input(("Salário do professor: ")))

                    comandosql.execute(f'insert into professores(registro, nomeprof, telefoneprof, idadeprof, salarioprof) values({cd}, "{nd}", "{tel}", {age}, {cash});')

                    conexao.commit()

                    print("\nCadastro feito com sucesso")

                    comandosql.close()
                    conexao.close()
                    
            #! ALTERAÇÃO
            #! ALTERAÇÃO
            #! ALTERAÇÃO

            elif question == 2:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')

                if conexao.is_connected():
                    comandosql = conexao.cursor()

                    cd = int(input("\nCodigo do professor: "))

                    comandosql.execute(f"select * from professores where registro = {cd}")
                    tabela = comandosql.fetchall()
                    if comandosql.rowcount > 0:

                        

                        change = int(input("O que você deseja alterar? \n [1] NOME \n [2] TELEFONE \n [3] IDADE \n [4] SALÁRIO \n"))

                        if change == 1:
                            if comandosql.rowcount > 0:
                                for registro in tabela:
                                    print(f"Nome do professor: {registro[1]}")
                                
                                novo_nome = input("Digite o novo nome do professor: ")

                                comandosql.execute(f'update professores set nomeprof = "{novo_nome}" where registro = {cd};')

                                conexao.commit()
                                print("\nAlteração feita com sucesso!")

                                comandosql.close()
                                conexao.close()

                        elif change == 2:
                            if comandosql.rowcount > 0:
                                for registro in tabela:
                                    print(f"Telefone do professor: {registro[2]}")
                                
                                novo_telefone = input("Digite o novo telefone do professor: ")

                                comandosql.execute(f'update professores set telefoneprof = "{novo_telefone}" where registro = {cd};')

                                conexao.commit()
                                print("\nAlteração feita com sucesso!")

                                comandosql.close()
                                conexao.close()

                        elif change == 3:
                            if comandosql.rowcount > 0:
                                for registro in tabela:
                                    print(f"Idade do professor: {registro[3]}")
                                
                                nova_idade = input("Digite a nova idade do professor: ")

                                comandosql.execute(f'update professores set idadeprof = "{nova_idade}" where registro = {cd};')

                                conexao.commit()
                                print("\nAlteração feita com sucesso!")

                                comandosql.close()
                                conexao.close()
                        
                        elif change == 4:
                            if comandosql.rowcount > 0:
                                for registro in tabela:
                                    print(f"Salario do professor: {registro[4]}")
                                
                                novo_salario = input("Digite o novo salario do professor: ")

                                comandosql.execute(f'update professores set salarioprof = "{novo_salario}" where registro = {cd};')

                                conexao.commit()
                                print("\nAlteração feita com sucesso!")

                                comandosql.close()
                                conexao.close()
                    else:
                        print("NÃO EXISTE UM PROFESSOR COM ESTE CÓDIGO!!!")

                    comandosql.close()
                    conexao.close()

            #! EXCLUSÃO
            #! EXCLUSÃO
            #! EXCLUSÃO

            elif question == 3:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')

                if conexao.is_connected():
                    comandosql = conexao.cursor()
                    cd = int(input("\nCodigo do professor: "))
                    comandosql.execute(f"select * from professores where registro = {cd};")
                    tabela = comandosql.fetchall()
                    if comandosql.rowcount > 0:
                        

                        for registro in tabela:
                            print(f"Nome do professor: {registro[1]}")

                        resp = input(("DESEJA REALMENTE EXCLUIR ESTE PROFESSOR? SIM [S] | NÃO [N]: "))

                        if resp == 'S':
                            comandosql.execute(f"delete from professores where registro = {cd};")
                            conexao.commit()
                            print("\nExclusão feita com sucesso")
                        else:
                            comandosql.close()
                            conexao.close()
                    else:
                        print("NÃO EXISTE UM PROFESSOR COM ESTE CÓDIGO!!!")

                    comandosql.close()
                    conexao.close()

            #! CONSULTA
            #! CONSULTA
            #! CONSULTA

            elif question == 4:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')
                if conexao.is_connected():
                    comandosql = conexao.cursor()

                    grid = PrettyTable(['Registro Professores', 'Nome ', 'Telefone', 'Idade', 'Salario'])

                    comandosql.execute("select * from professores;")

                    tabela = comandosql.fetchall()

                    if comandosql.rowcount > 0:
                        for registro in tabela:
                            grid.add_row([registro[0], registro[1], registro[2], registro[3], registro[4]])

                        print(grid)
                    else:
                        print("\nSEM CADASTROS!!!")
                    comandosql.close()
                    conexao.close()
            
            elif question == 5:
                print("\nSAINDO DO PROGRAMA...")

                if 'comandosql' in locals():
                    comandosql.close()
                if 'conexao' in locals() and conexao.is_connected():
                    conexao.close()
                break

            else:
                print("\nOPÇÃO INVÁLIDA. DIGITE UM NÚMERO DE 1 A 5.\n")
        
        #! EXCEPT
        #! EXCEPT
        #! EXCEPT
        except (ValueError):
            print('\nDIGITE APENAS O QUE É PEDIDO(APENAS NÚMEROS OU APENAS LETRAS)!!!\n')
            
            if input('DESEJA CONTINUAR? S [SIM] | N [NÃO]: ') != 'S':
                break

        except Exception as erro:
            print(f'ERRO: {erro}\n')
            if input('DESEJA CONTINUAR? S [SIM] | N [NÃO]: ') != 'S':
                if 'comandosql' in locals():
                    comandosql.close()
                if 'conexao' in locals() and conexao.is_connected():
                    conexao.close()
                break

