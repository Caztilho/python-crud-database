import mysql.connector 
from prettytable import PrettyTable 

def disciplinas_professores():
    while True:
        try:
            
            question = int(input("\nO que você deseja fazer na tabela 'Disciplinas x Professores':\n[1] CADASTRO \n[2] ALTERAÇÃO \n[3] EXCLUSÃO \n[4] CONSULTA A REGISTROS\n[5] SAIR\n"))


            #! CADASTRO
            #! CADASTRO
            #! CADASTRO

            if question == 1:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')

                if conexao.is_connected():
                    comandosql = conexao.cursor()

                    coddisc_curso = int(input("\nDigite o código da disciplina do curso: "))
                    coddisc = int(input("Digite o código da disciplina: "))
                    codprof = int(input("Digite o código do professor: "))
                    curso = int(input("Digite o número do curso: "))
                    carga_horaria = int(input("Digite a carga horária (em horas): "))
                    anoletivo = int(input("Digite o ano letivo: "))

                    comandosql.execute(f'insert into disciplinasprofessores(codigodisciplinacurso, coddisciplina, codprofessor, curso, cargahoraria, anoletivo) values({coddisc_curso}, {coddisc}, {codprof}, {curso}, {carga_horaria}, {anoletivo});')

                    conexao.commit()

                    print("\nCadastro feito com sucesso!")

                    comandosql.close()
                    conexao.close()
            
            #! ALTERAÇÃO
            #! ALTERAÇÃO
            #! ALTERAÇÃO


            elif question == 2:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')

                if conexao.is_connected():
                    comandosql = conexao.cursor()

                    coddisc_curso = int(input("Digite o código da disciplina do curso: "))
                    comandosql.execute(f"select * from disciplinasprofessores where codigodisciplinacurso = {coddisc_curso};")

                    tabela = comandosql.fetchall()

                    if comandosql.rowcount > 0:
                        change = int(input("\nO que você deseja alterar?\n[1] NÚMERO DO CURSO\n[2] CARGA HORÁRIA\n[3] ANO LETIVO\n"))

                        if change == 1:
                            if comandosql.rowcount > 0:
                                for registro in tabela:
                                    print(f"Número do curso: {registro[3]}")

                                    novo_codigo = int(input("Digite o novo número do curso: "))

                                    comandosql.execute(f"update disciplinasprofessores set curso = {novo_codigo} where codigodisciplinacurso = {coddisc_curso}; ")

                                    conexao.commit()
                                    print("\nAlteração feita com sucesso!")

                                    comandosql.close()
                                    conexao.close()
                        
                        if change == 2:
                            if comandosql.rowcount > 0:
                                for registro in tabela:
                                    print(f"Carga horária do curso: {registro[4]}")

                                    nova_hora = int(input("Digite a nova carga horária do curso: "))

                                    comandosql.execute(f"update disciplinasprofessores set cargahoraria = {nova_hora} where codigodisciplinacurso = {coddisc_curso}; ")

                                    conexao.commit()
                                    print("\nAlteração feita com sucesso!")

                                    comandosql.close()
                                    conexao.close()
                        
                        if change == 3:
                            if comandosql.rowcount > 0:
                                for registro in tabela:
                                    print(f"Ano letivo do curso: {registro[5]}")

                                    novo_ano = int(input("Digite o novo ano letivo do curso: "))

                                    comandosql.execute(f"update disciplinasprofessores set anoletivo = {novo_ano} where codigodisciplinacurso = {coddisc_curso}; ")

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
                
                coddisc_curso = int(input("\nDigite o código da disciplina do curso: "))
                comandosql.execute(f"select * from disciplinasprofessores where codigodisciplinacurso = {coddisc_curso};")

                tabela = comandosql.fetchall()

                if comandosql.rowcount > 0:
                    
                    comandosql.execute(f'select nomedisc from disciplinas where codigodisc = {coddisc_curso}')
                     
                    tabela = comandosql.fetchone()[0]
                    print(f'Nome do curso: {tabela}')

                    resp = input(("DESEJA REALMENTE EXCLUIR ESTA DISCIPLINA? SIM [S] | NÃO [N]: "))

                    if resp == 'S':
                            comandosql.execute(f"delete from disciplinasprofessores where codigodisciplinacurso = {coddisc_curso};")
                            conexao.commit()
                            print("\nExclusão feita com sucesso")
                else:
                    print("NÃO EXISTE UMA DISCIPLINA COM ESTE CÓDIGO!!!")

                comandosql.close()
                conexao.close()
                
            #! CONSULTA
            #! CONSULTA
            #! CONSULTA

            elif question == 4:
                conexao = mysql.connector.Connect(host='localhost',database='univap', user='root')

                if conexao.is_connected():
                    comandosql = conexao.cursor()

                grid = PrettyTable(['COD DA DISC DO CURSO', 'COD DISC ', 'COD PROF', 'CURSO', 'CARGA HORÁRIA', 'ANO LETIVO'])

                comandosql.execute("select * from disciplinasprofessores;")

                tabela = comandosql.fetchall()

                if comandosql.rowcount > 0:
                        for registro in tabela:
                            grid.add_row([registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]])
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





