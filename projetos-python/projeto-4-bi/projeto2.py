import pandas as pd
import openpyxl as  pxl
def verificar_situacao(media):
    if(media >= 6):
        situacao = "APROVADO"
        cor = "blue"
    elif(media >= 3.75 and media <= 5.9):
        situacao = "EXAME FINAL"
        cor = "yellow"
    elif(media < 3.75):
        situacao = "RETIDO"
        cor = "red"
    return  situacao, cor
        
def gerar_exel():
    global lista_dados
    global i
    dados_para_excel = []
    for aluno in lista_dados:
        dados_para_excel.append({
            "Matrícula do aluno": aluno["Matrícula"],
            "Nome do aluno": aluno["Nome"],
            "Nota de PVB": aluno["Nota de PVB"],
            "Nota de PAW": aluno["Nota de PAW"],
            "Nota de BD": aluno["Nota de BD"],
            "Nota de POO": aluno["Nota de POOI"],
            "Média": aluno["Média"]
        })

    # def para_planilha():
    df = pd.DataFrame(dados_para_excel)
    print(df)
    df.to_excel('NOTASFINAISALUNOS.xlsx', sheet_name = 'planilha_alunos', na_rep = '#N/A', header = True, index = False)

def verifica_notas(nome_materia, nota):
    if(str(nota).isnumeric == True):
        while nota < 0 or nota > 10:
            nota = float(input(f"Nota inválida! Redigite a nota de {nome_materia} (entre 0 e 10): "))
    else:
        while nota < 0 or nota > 10 and str(nota).isnumeric != True:
            nota = float(input(f"Nota inválida! Redigite a nota de {nome_materia} (entre 0 e 10): ")) 
    return nota
lista_dados = []
def forms_digitacao():
    global i
    try:
        while True:
            aluno_ra = input("Digite a matrícula do aluno: ")
            while(len(aluno_ra) > 6 or aluno_ra.isnumeric() == False or aluno_ra == ""):
                aluno_ra = input("Redigite a matrícula do aluno: ")

            nome_aluno = input("Digite o nome do aluno: ")
            while(nome_aluno == "" or nome_aluno.isnumeric() == True or len(nome_aluno) <= 3):
                nome_aluno = input("Redigite o nome do aluno: ")

            nota_pvb = float(input("Digite a nota da matéria P.V.B.: "))
            verifica_notas("P.V.B.",nota_pvb)
            nota_paw = float(input("Digite a nota da matéria P.A.W.: "))
            verifica_notas("P.A.W.",nota_paw)
            nota_bd = float(input("Digite a nota da matéria B.D.: "))
            verifica_notas("B.D.",nota_bd)
            nota_poo = float(input("Digite a nota da matéria P.O.O.I.: "))
            verifica_notas("P.O.O.I.",nota_poo)
            media = (nota_pvb + nota_paw + nota_poo + nota_bd) / 4
            situacao, cor = verificar_situacao(media)
            lista_dados.append({"Matrícula":aluno_ra, "Nome":nome_aluno, "Nota de PVB":nota_pvb, "Nota de PAW":nota_paw, "Nota de BD":nota_bd, "Nota de POOI":nota_poo, "Média":media, "Situação":situacao, "Cor":cor})
            # gerar_html(aluno_ra, nome_aluno,  nota_pvb, nota_paw, nota_bd, nota_poo, media, situacao, cor)
            res = input("Deseja inserir mais um aluno no exel? s/n ")
            if(res.lower() != "s"):
                break
        gerar_exel()
        gere = input("Deseja gerar um html de todos aluno(s) do exel? s/n ")
        if(gere.lower() == "s"):
            gerar_html(lista_dados)
    except Exception as erro:
        print("Ocorreu um erro: ",erro)
        menu()
    menu()
def gerar_html(lista_dados):
    for item in lista_dados:
        arquivo = open(f"{item['Matrícula']}.html", "w")
        arquivo.write(f"<!DOCTYPE html>\n<html lang='pt-br'>\n<head>\n    <meta charset='UTF-8'>\n    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n    <title>{item['Matrícula']}</title>\n<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n<div>\n    <p>Matricula: {item['Matrícula']}</p>\n    <p>Aluno</p>\n    <p id='nome'>{item['Nome']}<p>\n    <table>\n        <tr>\n            <th>PVB</th>\n            <th>PAW</th>\n            <th>BD</th>\n            <th>POO</th>\n            <th>MEDIA</th>\n        </tr>\n        <tr>\n            <td>{item['Nota de PVB']:,.1f}</td>\n            <td>{item['Nota de PAW']:,.1f}</td>\n            <td>{item['Nota de BD']:,.1f}</td>\n            <td>{item['Nota de POOI']:,.1f}</td>\n            <td>{item['Média']:,.1f}</td>\n        </tr>\n    </table>\n    <p>Situacao final: <p style='background-color: {item['Cor']};'>{item['Situação']}</p></p>\n</div>\n</body>\n</html>")
        arquivo.close()

def ver():
    pass

def menu():
    print("1 - Inserir dados exel de aluno(s);")
    print("2 - Ver alunos do exel;")
    print("3 - Sair.")
    opc = int(input("Escolha uma das opções: "))
    while(opc < 1 or opc > 4):
        opc = int(input("Escolha uma das opções entre 1 e 4 apenas: "))
    if(opc == 1):
        forms_digitacao()
    elif(opc == 2):
        ver()
    elif(opc == 3):
        print("Saindo...")
menu()
print("FIM DO Programa!!!")
# def gerar_html():
# def ver_alunos_planilha():
# ideia crie uma lista que irá conter todos os dados exemplo lista = [['111111','222222'][pvb]...]