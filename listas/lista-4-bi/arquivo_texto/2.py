import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='projetoalberson',
            user='root',
            password=''
        )
        if conexao.is_connected():
            print("Conectado ao banco de dados.")
            return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None
    
def criar_arquivos_html_professores():
    conexao = conectar()
    
    if conexao is None:
        return
    
    try:
        cursor = conexao.cursor(dictionary=True)
        
        
        consulta_professores = "SELECT registro, nomeProfessor FROM professores"
        cursor.execute(consulta_professores)
        professores = cursor.fetchall()
        
        consulta_disciplinas = """
            SELECT dp.coddisciplina, d.nomedisc, dp.codprofessor, dp.curso
            FROM disciplinasxprofessores dp
            JOIN disciplinas d ON dp.coddisciplina = d.codigodisc
        """
        cursor.execute(consulta_disciplinas)
        disciplinasxprofessores = cursor.fetchall()
        
        for professor in professores:
            professor_id = professor['registro']
            nome_professor = professor['nomeProfessor']
            
            nome_arquivo = f"{professor_id}.html"
            
            html = f"""
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Disciplinas do professor {nome_professor}</title>
            </head>
            <body>
                <h1>Disciplinas do professor: {nome_professor}</h1>
            """
            
            cursos = {}
            for registro in disciplinasxprofessores:
                if registro["codprofessor"] == professor_id:
                    curso_id = registro["curso"]
                    if curso_id not in cursos:
                        cursos[curso_id] = []
                    cursos[curso_id].append(registro)
            
            for curso_id, lista_disciplinas in cursos.items():
                html += f"<h2>Curso: {curso_id}</h2>"
                html += "<table border='1'><tr><th>Código da Disciplina</th><th>Nome da Disciplina</th></tr>"
                for registro in lista_disciplinas:
                    cod_disciplina = registro["coddisciplina"]
                    nome_disciplina = registro["nomedisc"]
                    html += f"<tr><td>{cod_disciplina}</td><td>{nome_disciplina}</td></tr>"
                html += "</table>"
            
            html += """
            </body>
            </html>
            """
            
            with open(nome_arquivo, "w") as arquivo:
                arquivo.write(html)
            
            print(f"Arquivo {nome_arquivo} criado com sucesso!")
    
    except mysql.connector.Error as erro:
        print(f"Erro ao consultar o banco de dados: {erro}")
    
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão ao banco de dados encerrada.")

criar_arquivos_html_professores()
