mat = input("Digite a matéria deseja inserir a média: ")
med = float(input("Digite qual foi a média: "))
mesg = "k"
def msg(med, mat):
    if med >= 6:
        mesg = f"Você foi APROVADO em {mat}"
    elif med >= 3.5 and med < 6:
        mesg = f"Você ficou de EXAME em {mat}"
    elif med < 3.5:
        mesg = f"Você foi REPROVADO em {mat}"
    return mesg        
print("*"*42)
res = msg(med, mat) #mesmo nome para não confundir
print(res)
print("*"*42)
