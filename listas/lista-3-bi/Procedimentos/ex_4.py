pos = 0
casa = 0.0
def calc_area(comodos):
    global pos
    global resposta
    global casa
    resposta[pos] = {"Cômodo" : comodos[pos][0],"Largura" : comodos[pos][1],"Comprimento" : comodos[pos][2],"Área" : comodos[pos][1]*comodos[pos][2]}
    casa += comodos[pos][1]*comodos[pos][2]
    pos += 1
    # print(resposta)
    if (i+1) == vz:
        resposta[pos] = {"Casa" : casa}
        # print(resposta)
        return resposta
    #largura*comprimento
comodos = []
resposta = {}
vz = int(input("Quantos cômodos tem em sua casa? "))
for i in range(0, vz):
   nome = input("Digite o nome do cômodo: ")
   comprimento = float(input(f"Digite o comprimento de seu/sua {nome}: "))
   largura = float(input(f"Digite a largura de seu/sua {nome}: "))
   comodos.append((nome,largura,comprimento))
   res = calc_area(comodos)
p = 0
print("\n","-"*10,"Cômodos e suas respectivas áreas","-"*10)
for x in range(0, vz):
    no = res[x]["Cômodo"]
    ar = res[x]["Área"]
    casa = res[pos]["Casa"]
    print(" "*15,no,"= ", str(ar)+"m2")
    if (x+1) == vz:
        print(" "*15,"Casa = ",str(casa)+"m2")