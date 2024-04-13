
def maior(v,w,x,y,z):
    max = v

    if w > max:
        max = w
    if x > max:
        max = x
    if y > max:
        max = y
    if z > max:
        max = z

    return max

def menor(v,w,x,y,z):
    min = v

    if w < min:
        min = w
    if x < min:
        min = x
    if y < min:
        min = y
    if z < min:
        min = z
        
    return min

a = input("Deseja iniciar o programa? s/n")
campeao = ""
medcampeao = 0
while a == "s" or a == "S":
        name = str(input("Atleta:"))
        resul1 = float(input("Primeiro Salto:"))
        resul2 = float(input("Segundo Salto:"))
        resul3 = float(input("Terceiro Salto:"))
        resul4 = float(input("Quarto Salto:"))
        resul5 = float(input("Quinto Salto:"))
        print("Melhor Salto foi: ", maior(resul1,resul2,resul3,resul4,resul5))
        print("Pior Salto foi: ", menor(resul1,resul2,resul3,resul4,resul5))
        med = ((resul1+resul2+resul3+resul4+resul5)- maior(resul1,resul2,resul3,resul4,resul5) - menor(resul1,resul2,resul3,resul4,resul5))/3
        print("Média dos demais saltos: {:.2f}".format(med))
        if med >= medcampeao:
            medcampeao = med
            campeao = name
        a = input("deseja continuar? s/n")
print("resultado final: ")
print(campeao.upper() +' : '+ str(medcampeao))
print("fim do programa")