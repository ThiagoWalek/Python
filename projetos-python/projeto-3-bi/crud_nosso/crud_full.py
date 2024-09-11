from prettytable import PrettyTable
import mysql.connector
import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def conectar():
    try:
        conexao = mysql.connector.Connect(
            host='localhost',
            database='projetoalberson',
            user='root',
            password=''
        )
        return conexao
    except Exception as erro:
        print("Erro ao conectar ao banco de dados: ", erro)
        return None

def cadastrar_disciplina():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            codigo = int(input("Digite o código da disciplina: "))
            nome = input("Digite o nome da disciplina: ")
            cursor.execute("INSERT INTO disciplinas (codigodisc, nomedisc) VALUES (%s, %s)", (codigo, nome))
            conexao.commit()
            print("Disciplina cadastrada com sucesso!")
        except Exception as erro:
            print(f"Erro ao cadastrar disciplina: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def alterar_disciplina():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            codigo = int(input("Digite o código da disciplina que deseja alterar: "))
            nome = input("Digite o novo nome da disciplina: ")
            cursor.execute("UPDATE disciplinas SET nomedisc=%s WHERE codigodisc=%s", (nome, codigo))
            conexao.commit()
            print("Disciplina alterada com sucesso!")
        except Exception as erro:
            print(f"Erro ao alterar disciplina: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def excluir_disciplina():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            codigo = int(input("Digite o código da disciplina que deseja excluir: "))
            cursor.execute("DELETE FROM disciplinas WHERE codigodisc=%s", (codigo,))
            conexao.commit()
            print("Disciplina excluída com sucesso!")
        except Exception as erro:
            print(f"Erro ao excluir disciplina: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def consultar_disciplinas():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            cursor.execute("SELECT * FROM disciplinas")
            grid = PrettyTable(['Código', 'Nome da Disciplina'])
            for (codigo, nome) in cursor:
                grid.add_row([codigo, nome])
            print(grid)
        except Exception as erro:
            print(f"Erro ao consultar disciplinas: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def cadastrar_professor():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            registro = int(input("Digite o registro que deseja dar a ele: "))
            nome = input("Digite o nome do professor: ")
            telefone = input("Digite o telefone do professor: ")
            salario = float(input("Digite o salário do professor: "))
            idade = int(input("Digite a idade do professor: "))
            while(idade < 1 or idade > 100):
                idade = int(input("Digite a idade do professor: "))
            cursor.execute("""
                INSERT INTO professores (nomeProfessor, telefoneProfessor, idadeProfessor, salarioProfessor, registro)
                VALUES (%s, %s, %s, %s, %s)
            """, (nome, telefone, idade, salario,registro))
            conexao.commit()
            print("Professor cadastrado com sucesso!")
        except Exception as erro:
            print(f"Erro ao cadastrar professor: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def alterar_professor():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            registro = int(input("Digite o registro do professor que deseja alterar: "))
            nome = input("Digite o novo nome do professor: ")
            telefone = input("Digite o novo telefone do professor: ")
            salario = float(input("Digite o novo salário do professor: "))
            idade = int(input("Digite a nova idade do professor: "))
            while(idade < 1 or idade > 100):
                idade = int(input("Digite a idade do professor: "))
            cursor.execute("""
                UPDATE professores
                SET nomeProfessor=%s, telefoneProfessor=%s, idadeProfessor=%s, salarioProfessor=%s
                WHERE codprofessor=%s
            """, (nome, telefone, idade, salario, registro))
            conexao.commit()
            print("Professor alterado com sucesso!")
        except Exception as erro:
            print(f"Erro ao alterar professor: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def excluir_professor():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            registro = int(input("Digite o registro do professor que deseja excluir: "))
            cursor.execute("DELETE FROM professores WHERE registro=%s", (registro,))
            conexao.commit()
            print("Professor excluído com sucesso!")
        except Exception as erro:
            print(f"Erro ao excluir professor: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def consultar_professores():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            cursor.execute("SELECT * FROM professores")
            grid = PrettyTable(['Registro', 'Nome', 'Telefone', 'Idade', 'Salário'])
            for (registro, nome, telefone, idade, salario) in cursor:
                grid.add_row([registro, nome, telefone, idade, salario])
            print(grid)
        except Exception as erro:
            print(f"Erro ao consultar professores: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def cadastrar_relacao():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            codigo_disc = int(input("Digite o código da disciplina: "))
            registro_prof = int(input("Digite o código do professor: "))
            ano_curso = int(input("Digite o ano do curso: "))
            carga_horaria = int(input("Digite a carga horária do professor: "))
            curso = input("Digite o curso: ")
            ano_letivo = int(input("Digite o ano letivo: "))
            cursor.execute("""
                INSERT INTO disciplinasxprofessores (coddisciplina, codprofessor, codigodisciplinanocurso, curso, cargahoraria, anoletivo)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (codigo_disc, registro_prof, ano_curso, curso, carga_horaria, ano_letivo))
            conexao.commit()
            print("Relação cadastrada com sucesso!")
        except Exception as erro:
            print(f"Erro ao cadastrar relação: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def consultar_relacoes():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            cursor.execute("""
                SELECT * FROM disciplinasxprofessores
            """)
            grid = PrettyTable(['Código Disciplina Curso', 'Código Disciplina', 'Código Professor', 'Curso', 'Carga Horária', 'Ano Letivo'])
            for (cod_disc_curso, cod_disc, cod_prof, curso, carga_horaria, ano_letivo) in cursor.fetchall():
                grid.add_row([cod_disc_curso, cod_disc, cod_prof, curso, carga_horaria, ano_letivo])
            print(grid)
        except Exception as erro:
            print(f"Erro ao consultar relações: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")


def atualizar_relacao():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()


        try:
            cod_disc_curso = input("Digite o código da disciplina no curso que deseja atualizar: ")
            cod_disc = int(input("Digite o novo código da disciplina: "))
            cod_prof = int(input("Digite o novo código do professor: "))
            curso = input("Digite o novo curso: ")
            carga_horaria = int(input("Digite a nova carga horária: "))
            ano_letivo = int(input("Digite o novo ano letivo: "))
            cursor.execute("""
                UPDATE disciplinasxprofessores
                SET coddisciplina=%s, codprofessor=%s, curso=%s, cargahoraria=%s, anoletivo=%s
                WHERE codigodisciplinanocurso=%s
            """, (cod_disc, cod_prof, curso, carga_horaria, ano_letivo, cod_disc_curso))
            conexao.commit()
            print("Relação atualizada com sucesso!")
        except Exception as erro:
            print(f"Erro ao atualizar relação: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")


def excluir_relacao():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        try:
            cod_disc_curso = input("Digite o código da disciplina no curso que deseja excluir: ")
            cursor.execute("DELETE FROM disciplinasxprofessores WHERE codigodisciplinanocurso=%s", (cod_disc_curso,))
            conexao.commit()
            print("Relação excluída com sucesso!")
        except Exception as erro:
            print(f"Erro ao excluir relação: {erro}")
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")



def menu():
    try:
        while True:
            print("\nMenu de Opções:")
            print("1 - Menu Disciplinas")
            print("2 - Menu Professores")
            print("3 - Menu DisciplinasXProfessores")
            print("4 - Menu completo")
            opcao_menu = int(input("Escolha uma opção: "))

            if opcao_menu == 1:
                limpar_tela()
                while True:
                    print("1. Cadastrar Disciplina")
                    print("2. Consultar Disciplinas")
                    print("3. Alterar Disciplina")
                    print("4. Excluir Disciplina")
                    print("5. Sair")

                    opcao_dis = int(input("Escolha uma opção: "))

                    if opcao_dis == 1:
                        cadastrar_disciplina()
                    elif opcao_dis == 2:
                        consultar_disciplinas()
                    elif opcao_dis == 3:
                        alterar_disciplina()
                    elif opcao_dis == 4:
                        excluir_disciplina()
                    elif opcao_dis == 5:
                        print("Saindo do sistema...")
                        break
                    else:
                        print("Opção inválida! Tente novamente.")

            elif opcao_menu == 2:
                limpar_tela()
                while True:
                    print("1. Cadastrar Professor")
                    print("2. Consultar Professores")
                    print("3. Alterar Professor")
                    print("4. Excluir Professor")
                    print("5. Sair")

                    opcao_prof = int(input("Escolha uma opção: "))

                    if opcao_prof == 1:
                        cadastrar_professor()
                    elif opcao_prof == 2:
                        consultar_professores()
                    elif opcao_prof == 3:
                        alterar_professor() 
                    elif opcao_prof == 4:
                        excluir_professor()
                    elif opcao_prof == 5:
                        print("Saindo do sistema...")
                        break
                    else:
                        print("Opção inválida! Tente novamente.")

            elif opcao_menu == 3:
                limpar_tela()
                while True:
                    print("1. Cadastrar Relação Disciplina-Professor")
                    print("2. Consultar Relações Disciplina-Professor")
                    print("3. Atualizar Relação Disciplina-Professor")
                    print("4. Excluir Relação Disciplina-Professor")
                    print("5. Sair")

                    opcao_rel = int(input("Escolha uma opção: "))

                    if opcao_rel == 1:
                        cadastrar_relacao()
                    elif opcao_rel == 2:
                        consultar_relacoes()
                    elif opcao_rel == 3:
                        atualizar_relacao()   
                    elif opcao_rel == 4:
                        excluir_relacao()
                    elif opcao_rel == 5:
                        print("Saindo do sistema...")
                        break
                    else:
                        print("Opção inválida! Tente novamente.")
            elif opcao_menu == 4:
                limpar_tela()
                while True:
                    print("\nMenu de Opções:")
                    print("1. Cadastrar Disciplina")
                    print("2. Alterar Disciplina")
                    print("3. Excluir Disciplina")
                    print("4. Consultar Disciplinas")
                    print("5. Cadastrar Professor")
                    print("6. Alterar Professor")
                    print("7. Excluir Professor")
                    print("8. Consultar Professores")
                    print("9. Cadastrar Relação Disciplina-Professor")
                    print("10. Consultar Relações Disciplina-Professor")
                    print("11. Excluir Relação Disciplina-Professor")
                    print("12. Atualizar Relação Disciplina-Professor")
                    print("13. Sair")

                    opcao = int(input("Escolha uma opção: "))

                    if opcao == 1:
                        cadastrar_disciplina()
                    elif opcao == 2:
                        alterar_disciplina()
                    elif opcao == 3:
                        excluir_disciplina()
                    elif opcao == 4:
                        consultar_disciplinas()
                    elif opcao == 5:
                        cadastrar_professor()
                    elif opcao == 6:
                        alterar_professor()
                    elif opcao == 7:
                        excluir_professor()
                    elif opcao == 8:
                        consultar_professores()
                    elif opcao == 9:
                        cadastrar_relacao()
                    elif opcao == 10:
                        consultar_relacoes()
                    elif opcao == 11:
                        excluir_relacao()
                    elif opcao == 12:
                        atualizar_relacao()
                    elif opcao == 13:
                        print("Saindo do sistema...")
                        break
                    else:
                        print("Opção inválida! Tente novamente.")
    except Exception as erro:
        print("ERRO: ", erro)
        menu()


menu()
