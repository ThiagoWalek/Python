from reportlab.pdfgen import canvas
import mysql.connector


def conectar_banco():
    conexao = mysql.connector.connect(
        host="localhost",        
        user="root",             
        password="",    
        database="projetoalberson"     
    )
    return conexao


def gerar_pdf(nome_arquivo, conteudo):
    pdf = canvas.Canvas(nome_arquivo)
    pdf.setFont("Helvetica", 12)
    
    for i, linha in enumerate(conteudo, start=1):
        pdf.drawString(100, 750 - 15 * i, linha)

    pdf.save()
    print(f"PDF '{nome_arquivo}' gerado com sucesso!")

def consultar_professor_por_registro(conexao, registro):
    cursor = conexao.cursor()
    query = "SELECT * FROM professores WHERE registro = %s"
    cursor.execute(query, (registro,))
    resultado = cursor.fetchall()

    if resultado:
        conteudo = [str(linha) for linha in resultado]
        gerar_pdf(f"professor_{registro}.pdf", conteudo)
    else:
        print("Professor não encontrado.")

def consultar_professores_por_nome(conexao, prefixo):
    cursor = conexao.cursor()
    query = "SELECT * FROM professores WHERE nomeprof LIKE %s"
    cursor.execute(query, (prefixo + '%',))
    resultado = cursor.fetchall()

    if resultado:
        conteudo = [str(linha) for linha in resultado]
        gerar_pdf(f"professores_com_{prefixo}.pdf", conteudo)
    else:
        print("Nenhum professor encontrado com esse prefixo.")

def consultar_disciplinas_por_curso(conexao, curso):
    cursor = conexao.cursor()
    query = """
        SELECT disciplinas.nomdisc 
        FROM disciplinasprofessores 
        JOIN disciplinas ON disciplinasprofessores.coddisc = disciplinas.coddisc 
        WHERE disciplinasprofessores.curso = %s
    """
    cursor.execute(query, (curso,))
    resultado = cursor.fetchall()

    if resultado:
        conteudo = [linha[0] for linha in resultado]
        gerar_pdf(f"disciplinas_do_curso_{curso}.pdf", conteudo)
    else:
        print("Nenhuma disciplina encontrada para esse curso.")

def consultar_professores_por_curso(conexao, curso):
    cursor = conexao.cursor()
    query = """
        SELECT professores.nomeprof 
        FROM disciplinasprofessores 
        JOIN professores ON disciplinasprofessores.codprof = professores.registro 
        WHERE disciplinasprofessores.curso = %s
    """
    cursor.execute(query, (curso,))
    resultado = cursor.fetchall()

    if resultado:
        conteudo = [linha[0] for linha in resultado]
        gerar_pdf(f"professores_do_curso_{curso}.pdf", conteudo)
    else:
        print("Nenhum professor encontrado para esse curso.")

def consultar_carga_horaria_por_ano(conexao, curso, ano_letivo):
    cursor = conexao.cursor()
    query = """
        SELECT SUM(cargahoraria) 
        FROM disciplinasprofessores 
        WHERE curso = %s AND anoletivo = %s
    """
    cursor.execute(query, (curso, ano_letivo))
    resultado = cursor.fetchone()

    if resultado[0]:
        conteudo = [f"Carga horária total do curso {curso} para o ano {ano_letivo}: {resultado[0]} horas"]
        gerar_pdf(f"carga_horaria_{curso}_{ano_letivo}.pdf", conteudo)
    else:
        print("Nenhuma carga horária encontrada para esse curso e ano letivo.")

def menu():
    conexao = conectar_banco()
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar dados de um professor por registro")
        print("2. Consultar professores por prefixo do nome")
        print("3. Consultar disciplinas de um curso")
        print("4. Consultar professores de um curso")
        print("5. Consultar carga horária total de um curso para um ano letivo")
        print("0. Sair")

        opcao = input("Digite sua escolha: ")

        if opcao == '1':
            registro = input("Digite o número de registro do professor: ")
            consultar_professor_por_registro(conexao, registro)
        elif opcao == '2':
            prefixo = input("Digite o prefixo do nome do professor: ")
            consultar_professores_por_nome(conexao, prefixo)
        elif opcao == '3':
            curso = input("Digite o código do curso: ")
            consultar_disciplinas_por_curso(conexao, curso)
        elif opcao == '4':
            curso = input("Digite o código do curso: ")
            consultar_professores_por_curso(conexao, curso)
        elif opcao == '5':
            curso = input("Digite o código do curso: ")
            ano_letivo = input("Digite o ano letivo: ")
            consultar_carga_horaria_por_ano(conexao, curso, ano_letivo)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
    
    conexao.close()


menu()
