def maximo(v,ma):
    if v > ma:
        ma = v
    return ma
def minimo(v,mi):
    if v < mi:
        mi = v
    return mi
def dicionario(f,ma,mi,i):
    global total, vz
    total += f
    maior = maximo(f,ma)
    menor = minimo(f,mi)
    media = total/vz
    if (vz-1) == i: # principal erro que o chat indentificou
        dic = {"Faturamento total":total,"Maior faturamento":maior,"Menor faturamento":menor,"Faturamento médio":media}
        return dic
vz = int(input("Quantos faturamentos deseja informar? "))
max = -10000
min = 100000 # problema ao encontrar o minimo
total = 0
for i in range(0, vz):
    fat = int(input(f"Digite o {i+1}° faturamento: "))
    dici = dicionario(fat,max,min,i)
    max = maximo(fat, max)#alteração feita, porém não compreendida
    min = minimo(fat, min)
print("*"*40)
print(dici)
print("*"*40)
for x in dici:
    print(x,"= ",end="")
    y = dici[x]
    print(y)
print("*"*40)