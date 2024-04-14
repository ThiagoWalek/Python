lista = list()
total = 0
for i in range(9):
    user = int(input(f"Digite o número da posição {i} da matriz: "))
    lista.append(user)
    total += user
print("-"*90)
print(f"Essa lista = {lista} irá se transformar em uma matriz!")
print("-"*90)
print("Matriz:")
print(" "*14,"         coluna 1   coluna 2   coluna 3")
print()
print(" "*14,"linha 1 -  ",lista[0]," "*8,lista[1]," "*8,lista[2],"\n")
print(" "*14,"linha 2 -  ",lista[3]," "*8,lista[4]," "*8,lista[5],"\n")
print(" "*14,"linha 3 -  ",lista[6]," "*8,lista[7]," "*8,lista[8],"\n")
print("-"*90)
print("Os dados contidos na diagonal da matriz da esquerda para a direita são: ",lista[0::4])
if lista[8] in lista[2::2]:
    print(f"Os dados contidos na diagonal da matriz da direita para a esquerda são: [{lista[2]}, {lista[4]}, {lista[6]}]")
else:
    print("Os dados contidos na diagonal da matriz da direita para a esquerda são: ",lista[2::2])
print("-"*90)