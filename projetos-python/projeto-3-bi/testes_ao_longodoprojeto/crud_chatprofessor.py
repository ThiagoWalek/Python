import mysql.connector
from mysql.connector import errorcode


def conectar():
    try:
        conexao = mysql.connector.Connect(host='localhost', database='projetoalberson', user='root', password='')
        return conexao
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuário ou senha inválidos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
        else:
            print(err)


def cadastrar_professor():
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Digite o nome do professor: ")
    telefone = input("Digite o telefone do professor: ")
    idade = int(input("Digite a idade do professor: "))
    salario = float(input("Digite o salário do professor: "))

    try:
        cursor.execute("""
            INSERT INTO professores (nomeProfessor, telefoneprofessor, idadeProfessor, salarioProfessor)
            VALUES (%s, %s, %s, %s)
        """, (nome, telefone, idade, salario))
        conexao.commit()
        print("Professor cadastrado com sucesso!")
    except Exception as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conexao.close()


def alterar_professor():
    conexao = conectar()
    cursor = conexao.cursor()

    registro = int(input("Digite o registro do professor que deseja alterar: "))
    nome = input("Digite o novo nome do professor: ")
    telefone = input("Digite o novo telefone do professor: ")
    idade = int(input("Digite a nova idade do professor: "))
    salario = float(input("Digite o novo salário do professor: "))

    try:
        cursor.execute("""
            UPDATE professores
            SET nomeProfessor=%s, telefoneprofessor=%s, idadeProfessor=%s, salarioProfessor=%s
            WHERE registro=%s
        """, (nome, telefone, idade, salario, registro))
        conexao.commit()
        print("Professor alterado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conexao.close()


def excluir_professor():
    conexao = conectar()
    cursor = conexao.cursor()

    registro = int(input("Digite o registro do professor que deseja excluir: "))

    try:
        cursor.execute("SELECT * FROM disciplinasxprofessores WHERE codprofessor=%s", (registro,))
        resultado = cursor.fetchall()

        if resultado:
            print("Não é possível excluir este professor, pois ele está vinculado a uma disciplina.")
        else:
            cursor.execute("DELETE FROM professores WHERE registro=%s", (registro,))
            conexao.commit()
            print("Professor excluído com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conexao.close()


def consultar_professores():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM professores")
        for (registro, nome, telefone, idade, salario) in cursor:
            print(f"Registro: {registro}, Nome: {nome}, Telefone: {telefone}, Idade: {idade}, Salário: {salario}")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conexao.close()


def menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Professor")
        print("2. Alterar Professor")
        print("3. Excluir Professor")
        print("4. Consultar Professores")
        print("5. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_professor()
        elif opcao == 2:
            alterar_professor()
        elif opcao == 3:
            excluir_professor()
        elif opcao == 4:
            consultar_professores()
        elif opcao == 5:
            break
        else:
            print("Opção inválida! Tente novamente.")


menu()