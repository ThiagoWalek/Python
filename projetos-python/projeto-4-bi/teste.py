import pandas as pd
import openpyxl as  pxl

def verifica_notas(nome_materia, nota):
    if(nota.isnumeric() == True):
        nota = int(nota)
        if(nota <= 10 and nota >= 0):
            print(f"{nome_materia} = {nota}")
        else:
            nota = input(f"Redigite sua nota de {nome_materia}: ")
    else:
        while(nota.isnumeric() == False):
                nota = input(f"Redigite sua nota de {nome_materia}: ")

lista_aluno_ra = list()
lista_nome_aluno = list()
lista_nota_pvb = list()
lista_nota_paw = list()
lista_nota_bd = list()
lista_nota_poo = list()
lista_media = list()
while True:
    aluno_ra = input("Digite a sua matrícula: ")
    while(len(aluno_ra) != 6):
        aluno_ra = input("Redigite a sua matrícula: ")

    nome_aluno = input("Digite o nome do aluno: ")
    while(nome_aluno == "" or nome_aluno.isnumeric() == True or len(nome_aluno) <= 3):
        nome_aluno = input("Redigite o nome do aluno: ")

    nota_pvb = input("Digite a nota da matéria P.V.B.: ")
    verifica_notas("P.V.B.",nota_pvb)
    nota_paw = input("Digite a nota da matéria P.A.W.: ")
    verifica_notas("P.A.W.",nota_paw)
    nota_bd = input("Digite a nota da matéria B.D.: ")
    verifica_notas("B.D.",nota_bd)
    nota_poo = input("Digite a nota da matéria P.O.O.: ")
    verifica_notas("P.O.O.",nota_poo)
    nota_pvb = int(nota_pvb)
    nota_paw = int(nota_paw)
    nota_bd =  int(nota_bd)
    nota_poo =  int(nota_poo)
    media = (nota_pvb + nota_paw + nota_poo + nota_bd) / 4
    lista_aluno_ra.append(aluno_ra)
    lista_nome_aluno.append(nome_aluno)
    lista_nota_pvb.append(nota_pvb)
    lista_nota_paw.append(nota_paw)
    lista_nota_bd.append(nota_bd)
    lista_nota_poo.append(nota_poo)
    lista_media.append(media)
    res = input("Deseja inserir mais um aluno no exel? s/n ")
    if(res.lower() != "s"):
        break
dict_dados = {"Matrícula do aluno":lista_aluno_ra, "Nome do aluno":lista_nome_aluno, "Nota de PVB":lista_nota_pvb, "Nota de PAW":lista_nota_paw, "Nota de BD":lista_nota_bd, "Nota de POO":lista_nota_poo, "Média":lista_media}
print("Dicionário = ",dict_dados)

# def para_planilha():
df = pd.DataFrame(dict_dados)
print("DataFrame = ", df)
df.to_excel('NOTASFINAISALUNOS.xlsx', sheet_name = 'planilha_alunos', na_rep = '#N/A', header = True, index = False)

def menu():
    print("1 - Inserir dados exel de aluno(s)")
    print("2 - Gerar html de aluno")
    print("3 - Ver alunos do exel")
    print("4 - Sair")

def gerar_exel():
def gerar_html():
def ver_alunos_planilha():
# ideia crie uma lista que irá conter todos os dados exemplo lista = [['111111','222222'][pvb]...]