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
    dict_dados = {"Matrícula do aluno":lista_dados[0], "Nome do aluno":lista_dados[1], "Nota de PVB":lista_dados[2], "Nota de PAW":lista_dados[3], "Nota de BD":lista_dados[4], "Nota de POO":lista_dados[5], "Média":lista_dados[6]}
    print("Dicionário = ",dict_dados)

    # def para_planilha():
    df = pd.DataFrame(dict_dados)
    print(df)
    df.to_excel('NOTASFINAISALUNOS.xlsx', sheet_name = 'planilha_alunos', na_rep = '#N/A', header = True, index = False)

def verifica_notas(nome_materia, nota):
    if(nota <= 10 and nota >= 0):
        print(f"{nome_materia} = {nota}")
    else:
        while(nota > 10 and nota < 0):
            nota = input(f"Redigite sua nota de {nome_materia}: ")
lista_dados = [[],[],[],[],[],[],[],[],[]]
def forms_digitacao():
    try:
        while True:
            aluno_ra = input("Digite a matrícula do aluno: ")
            while(len(aluno_ra) <= 6 and aluno_ra.isnumeric() == False):
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
            nota_poo = float(input("Digite a nota da matéria P.O.O.: "))
            verifica_notas("P.O.O.",nota_poo)
            media = (nota_pvb + nota_paw + nota_poo + nota_bd) / 4
            lista_dados[0].append(aluno_ra)
            lista_dados[1].append(nome_aluno)
            lista_dados[2].append(nota_pvb)
            lista_dados[3].append(nota_paw)
            lista_dados[4].append(nota_bd)
            lista_dados[5].append(nota_poo)
            lista_dados[6].append(media)
            situacao, cor = verificar_situacao(media)
            lista_dados[7].append(situacao)
            lista_dados[8].append(cor)
            # gerar_html(aluno_ra, nome_aluno,  nota_pvb, nota_paw, nota_bd, nota_poo, media, situacao, cor)
            res = input("Deseja inserir mais um aluno no exel? s/n ")
            if(res.lower() != "s"):
                break
        gerar_exel()
        gere = input("Deseja gerar um html de todos aluno(s) do exel? s/n")
        if(gere.lower() == "s"):
            gerar_html(lista_dados[0], lista_dados[1],  lista_dados[2], lista_dados[3], lista_dados[4], lista_dados[5], lista_dados[6], lista_dados[7], lista_dados[8])
    except Exception as erro:
        print("Ocorreu um erro: ",erro)
        menu()
    menu()
def gerar_html(aluno_ra, nome_aluno,  nota_pvb, nota_paw, nota_bd, nota_poo, media, situacao, cor):
    for aluno_ra, nome_aluno, nota_pvb, nota_paw, nota_bd, nota_poo, media, situacao, cor in zip(aluno_ra, nome_aluno, nota_pvb, nota_paw, nota_bd, nota_poo, media, situacao, cor):
        arquivo = open(aluno_ra+".html", "w")
        arquivo.write(f"<!DOCTYPE html>\n<html lang='pt-br'>\n<head>\n    <meta charset='UTF-8'>\n    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n    <title>{aluno_ra}</title>\n<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n<div>\n    <p>Matricula: {aluno_ra}</p>\n    <p>Aluno</p>\n    <p id='nome'>{nome_aluno}<p>\n    <table>\n        <tr>\n            <th>PVB</th>\n            <th>PAW</th>\n            <th>BD</th>\n            <th>POO</th>\n            <th>MEDIA</th>\n        </tr>\n        <tr>\n            <td>{nota_pvb:,.2f}</td>\n            <td>{nota_paw:,.2f}</td>\n            <td>{nota_bd:,.2f}</td>\n            <td>{nota_poo:,.2f}</td>\n            <td>{media:,.2f}</td>\n        </tr>\n    </table>\n    <p>Situacao final: <p style='background-color: {cor};'>{situacao}</p></p>\n</div>\n</body>\n</html>")
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