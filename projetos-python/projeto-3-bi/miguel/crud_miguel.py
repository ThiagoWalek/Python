from prettytable import PrettyTable
import mysql.connector


def conecta_bd():
    try:
        bd_connection = mysql.connector.Connect(
            host='localhost',
            database='projetoalberson',
            user='root',
            password=''
        )
        return bd_connection
    except Exception as e:
        print("erro ao ao banco de dados: ", e)
        return None

def criar_disciplina():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            codigo = int(input("Digite o código da disciplina: "))
            nome = input("Digite o nome da disciplina: ")
            bd_cursorr.execute("INSERT INTO disciplinas (codigodisc, nomedisc) VALUES (%s, %s)", (codigo, nome))
            bd_connection.commit()
            print("Disciplina cadastrada com sucesso!")
        except Exception as e:
            print(f"erro ao cadastrar disciplina: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")

def alterar_disciplina():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            codigo = int(input("Digite o código da disciplina que deseja alterar: "))
            nome = input("Digite o novo nome da disciplina: ")
            bd_cursorr.execute("UPDATE disciplinas SET nomedisc=%s WHERE codigodisc=%s", (nome, codigo))
            bd_connection.commit()
            print("Disciplina alterada com sucesso!")
        except Exception as e:
            print(f"erro ao alterar disciplina: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")

def apagar_disciplina():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            codigo = int(input("Digite o código da disciplina que deseja excluir: "))
            bd_cursorr.execute("DELETE FROM disciplinas WHERE codigodisc=%s", (codigo,))
            bd_connection.commit()
            print("Disciplina excluída com sucesso!")
        except Exception as e:
            print(f"erro ao excluir disciplina: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")

def mostrar_disciplinas():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            bd_cursorr.execute("SELECT * FROM disciplinas")
            grid = PrettyTable(['Código', 'Nome da Disciplina'])
            for (codigo, nome) in bd_cursorr:
                grid.add_row([codigo, nome])
            print(grid)
        except Exception as e:
            print(f"erro ao consultar disciplinas: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")

def criar_professor():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            registro = int(input("Digite o registro que deseja dar a ele: "))
            nome = input("Digite o nome do professor: ")
            telefone = input("Digite o telefone do professor: ")
            salario = float(input("Digite o salário do professor: "))
            idade = int(input("Digite a idade do professor: "))
            while(idade < 1 or idade > 100):
                idade = int(input("Digite a idade do professor: "))
            bd_cursorr.execute("""
                INSERT INTO professores (nomeProfessor, telefoneProfessor, idadeProfessor, salarioProfessor, registro)
                VALUES (%s, %s, %s, %s, %s)
            """, (nome, telefone, idade, salario,registro))
            bd_connection.commit()
            print("Professor cadastrado com sucesso!")
        except Exception as e:
            print(f"erro ao cadastrar professor: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")

def alterar_professor():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            registro = int(input("Digite o registro do professor que deseja alterar: "))
            nome = input("Digite o novo nome do professor: ")
            telefone = input("Digite o novo telefone do professor: ")
            salario = float(input("Digite o novo salário do professor: "))
            idade = int(input("Digite a nova idade do professor: "))
            while(idade < 1 or idade > 100):
                idade = int(input("Digite a idade do professor: "))
            bd_cursorr.execute("""
                UPDATE professores
                SET nomeProfessor=%s, telefoneProfessor=%s, idadeProfessor=%s, salarioProfessor=%s
                WHERE codprofessor=%s
            """, (nome, telefone, idade, salario, registro))
            bd_connection.commit()
            print("Professor alterado com sucesso!")
        except Exception as e:
            print(f"erro ao alterar professor: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")

def apagar_professor():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            registro = int(input("Digite o registro do professor que deseja excluir: "))
            bd_cursorr.execute("DELETE FROM professores WHERE registro=%s", (registro,))
            bd_connection.commit()
            print("Professor excluído com sucesso!")
        except Exception as e:
            print(f"erro ao excluir professor: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")

def mostrar_professores():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            bd_cursorr.execute("SELECT * FROM professores")
            grid = PrettyTable(['Registro', 'Nome', 'Telefone', 'Idade', 'Salário'])
            for (registro, nome, telefone, idade, salario) in bd_cursorr:
                grid.add_row([registro, nome, telefone, idade, salario])
            print(grid)
        except Exception as e:
            print(f"erro ao consultar professores: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")

def criar_relacao():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            codigo_disc = int(input("Digite o código da disciplina: "))
            registro_prof = int(input("Digite o código do professor: "))
            ano_curso = int(input("Digite o ano do curso: "))
            carga_horaria = int(input("Digite a carga horária do professor: "))
            curso = input("Digite o curso: ")
            ano_letivo = int(input("Digite o ano letivo: "))
            bd_cursorr.execute("""
                INSERT INTO disciplinasxprofessores (coddisciplina, codprofessor, codigodisciplinanocurso, curso, cargahoraria, anoletivo)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (codigo_disc, registro_prof, ano_curso, curso, carga_horaria, ano_letivo))
            bd_connection.commit()
            print("Relação cadastrada com sucesso!")
        except Exception as e:
            print(f"erro ao cadastrar relação: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")

def mostrar_relacoes():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            bd_cursorr.execute("""
                SELECT * FROM disciplinasxprofessores
            """)
            grid = PrettyTable(['Código Disciplina Curso', 'Código Disciplina', 'Código Professor', 'Curso', 'Carga Horária', 'Ano Letivo'])
            for (cod_disc_curso, cod_disc, cod_prof, curso, carga_horaria, ano_letivo) in bd_cursorr.fetchall():
                grid.add_row([cod_disc_curso, cod_disc, cod_prof, curso, carga_horaria, ano_letivo])
            print(grid)
        except Exception as e:
            print(f"erro ao consultar relações: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")


def atualizar_relacao():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()


        try:
            cod_disc_curso = input("Digite o código da disciplina no curso que deseja atualizar: ")
            cod_disc = int(input("Digite o novo código da disciplina: "))
            cod_prof = int(input("Digite o novo código do professor: "))
            curso = input("Digite o novo curso: ")
            carga_horaria = int(input("Digite a nova carga horária: "))
            ano_letivo = int(input("Digite o novo ano letivo: "))
            bd_cursorr.execute("""
                UPDATE disciplinasxprofessores
                SET coddisciplina=%s, codprofessor=%s, curso=%s, cargahoraria=%s, anoletivo=%s
                WHERE codigodisciplinanocurso=%s
            """, (cod_disc, cod_prof, curso, carga_horaria, ano_letivo, cod_disc_curso))
            bd_connection.commit()
            print("Relação atualizada com sucesso!")
        except Exception as e:
            print(f"erro ao atualizar relação: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")


def apagar_relacao():
    bd_connection = conecta_bd()
    if bd_connection:
        bd_cursorr = bd_connection.cursor()

        try:
            cod_disc_curso = input("Digite o código da disciplina no curso que deseja excluir: ")
            bd_cursorr.execute("DELETE FROM disciplinasxprofessores WHERE codigodisciplinanocurso=%s", (cod_disc_curso,))
            bd_connection.commit()
            print("Relação excluída com sucesso!")
        except Exception as e:
            print(f"erro ao excluir relação: {e}")
        finally:
            bd_cursorr.close()
            bd_connection.close()
    else:
        print("Não foi possível ao banco de dados.")



def menu():
    try:
        while True:
            print("\nMenu:")
            print("1. Criar Disciplina")
            print("2. Alterar Disciplina")
            print("3. Apagar Disciplina")
            print("4. Mostrar Disciplinas")
            print("5. Criar Professor")
            print("6. Alterar Professor")
            print("7. Apagar Professor")
            print("8. Mostrar Professores")
            print("9. Criar Relação Disciplina-Professor")
            print("10. Mostrar Relações Disciplina-Professor")
            print("11. Apagar Relação Disciplina-Professor")
            print("12. Atualizar Relação Disciplina-Professor")
            print("13. Sair")

            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                criar_disciplina()
            elif escolha == 2:
                alterar_disciplina()
            elif escolha == 3:
                apagar_disciplina()
            elif escolha == 4:
                mostrar_disciplinas()
            elif escolha == 5:
                criar_professor()
            elif escolha == 6:
                alterar_professor()
            elif escolha == 7:
                apagar_professor()
            elif escolha == 8:
                mostrar_professores()
            elif escolha == 9:
                criar_relacao()
            elif escolha == 10:
                mostrar_relacoes()
            elif escolha == 11:
                apagar_relacao()
            elif escolha == 12:
                atualizar_relacao()
            elif escolha == 13:
                break
            else:
                print("Opção inválida!!!")
    except Exception as e:
        print("erro: ", e)

menu()
