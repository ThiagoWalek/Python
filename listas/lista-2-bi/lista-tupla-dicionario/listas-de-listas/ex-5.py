import random
# random.radint
n = list()
print("-"*90)
num = int(input("Quantas simulações dejesa fazer do jogo da mega-sena? ")) # define o range
print("-"*90)
for i in range(0,num):
    a = random.randint(1,999999999999) # gera o numero
    if a not in n: # verifica se o numero naõ está na lista 
        n.append([a])
    else: # se estiver na lista
        print(" "*30,"REPETIU UM NUMERO")
        print(" "*30,"-"*17)
print("-"*90)
print("Os números que foram gerados sem repetição foram respectivamente: \n\n",n)
print("-"*90)