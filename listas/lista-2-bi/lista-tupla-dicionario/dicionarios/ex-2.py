import random
dicionario = {"jogador1":random.randint(1,6),"jogador2":random.randint(1,6),"jogador3":random.randint(1,6),"jogador4":random.randint(1,6)}
lista_valores = list(dicionario.values())
lista_nomes = list(dicionario.keys())
for i in range(0, 4):
    print(f"{lista_nomes[i]} = {lista_valores[i]}")
#for i in range(0, 4):
