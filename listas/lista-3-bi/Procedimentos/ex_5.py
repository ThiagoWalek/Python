def lista(l):
    maior = 0
    menor = 0
    menor = min(l)
    maior = max(l)
    
    print(f"Maior valor é {maior}, e está na posição {l.index(maior)}")
    print(f"Menor valor é {menor}, e está na posição {l.index(menor)}\n")
lis = list()
while True:
    num = int(input("Digite um número: "))
    while num in lis:
        num = int(input("Digite outro número: "))
    if num not in lis:
        lis.append(num)
    # print(lis)
    if input("Deseja continuar? s/n ") != "s":
        break
print("\n","-"*15,"Valores","-"*15)
lista(lis)