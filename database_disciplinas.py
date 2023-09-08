import mysql.connector 
from prettytable import PrettyTable 

def disciplinas():
    while True:
        try:
            question = int(input("\nO que você deseja fazer na tabela 'Disciplinas':\n[1] CADASTRO \n[2] ALTERAÇÃO \n[3] EXCLUSÃO \n[4] CONSULTA A REGISTROS\n[5] SAIR\n"))


            #! CADASTRO
            #! CADASTRO
            #! CADASTRO

            if question == 1:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')

                if conexao.is_connected():
                    comandosql = conexao.cursor()
                    coddisc = int(input("\nDigite o código da disciplina: "))
                    nomedisc = (input("Digite o nome da disciplina: "))

                comandosql.execute(f'insert into disciplinas(codigodisc, nomedisc) values({coddisc}, "{nomedisc}");')

                conexao.commit()

                print("\nCadastro feito com sucesso!")

                comandosql.close()
                conexao.close()

            #! ALTERAÇÃO
            #! ALTERAÇÃO
            #! ALTERAÇÃO

            elif question == 2:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')
                comandosql = conexao.cursor()

                if conexao.is_connected():
                    coddisc = int(input("\nDigite o código da disciplina: "))
                    comandosql.execute(f'select * from disciplinas where codigodisc = {coddisc};')
                    tabela = comandosql.fetchall()

                    if comandosql.rowcount > 0:
                        

                        if comandosql.rowcount > 0:
                                for registro in tabela:
                                    print(f"Nome do curso: {registro[1]}")

                                    novo_nome = (input("Digite o novo nome do curso: "))

                                    comandosql.execute(f'update disciplinas set nomedisc = "{novo_nome}" where codigodisc = {coddisc};')

                                    conexao.commit()

                                    print("\nAlteração feita com sucesso!")

                                    comandosql.close()
                                    conexao.close()
                    else:
                        print("NÃO EXISTE UMA DISCIPLINA COM ESTE CÓDIGO!!!")
                        comandosql.close()
                        conexao.close()
                
            #! EXCLUSÃO
            #! EXCLUSÃO
            #! EXCLUSÃO

            elif question == 3:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')
                if conexao.is_connected():
                    comandosql = conexao.cursor()
                
                coddisc = int(input("\nDigite o código da disciplina: "))
                comandosql.execute(f'select * from disciplinas where codigodisc = {coddisc};')

                tabela = comandosql.fetchall()
                if comandosql.rowcount > 0:
                    

                    for registro in tabela:
                        print(f"Nome do curso: {registro[1]}")

                    resp = input(("DESEJA REALMENTE EXCLUIR ESTA DISCIPLINA? SIM [S] | NÃO [N]: "))

                    if resp == 'S':
                        comandosql.execute(f'delete from disciplinas where codigodisc = {coddisc};')
                        conexao.commit()
                        print("\nExclusão feita com sucesso")
                else:
                    print("NÃO EXISTE UMA DISCIPLINA COM ESTE CÓDIGO!!!!!!")

                comandosql.close()
                conexao.close()

            #! CONSULTA
            #! CONSULTA
            #! CONSULTA

            elif question == 4:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')
                if conexao.is_connected():
                    comandosql = conexao.cursor()

                    grid = PrettyTable(['CÓDIGO DISCIPLINA', 'NOME DISCIPLINA'])

                    comandosql.execute("select * from disciplinas;")

                    tabela = comandosql.fetchall()

                    if comandosql.rowcount > 0:
                        for registro in tabela:
                            grid.add_row([registro[0], registro[1]])
                        
                        print(grid)

                    else:
                        print("\nSEM CADASTROS!!!")
                    comandosql.close()
                    conexao.close()
            
            elif question == 5:
                print("SAINDO DO PROGRAMA...")

                if 'comandosql' in locals():
                    comandosql.close()
                if 'conexao' in locals() and conexao.is_connected():
                    conexao.close()
                break

            else:
                print("OPÇÃO INVÁLIDA. DIGITE UM NÚMERO DE 1 A 5.\n")

        #! EXCEPT
        #! EXCEPT
        #! EXCEPT

        except (ValueError):
            print('DIGITE APENAS O QUE É PEDIDO (APENAS NÚMEROS OU APENAS LETRAS)!!!')
            
            if input('DESEJA CONTINUAR? S [SIM] | N [NÃO]: ') != 'S':
                if 'comandosql' in locals():
                    comandosql.close()
                if 'conexao' in locals() and conexao.is_connected():
                    conexao.close()
                break
        

        except Exception as erro:
            print(f"ERRO: {erro}\n")

            if input('DESEJA CONTINUAR? S [SIM] | N [NÃO]: ') != 'S':
                if 'comandosql' in locals():
                    comandosql.close()
                if 'conexao' in locals() and conexao.is_connected():
                    conexao.close()
                break


        