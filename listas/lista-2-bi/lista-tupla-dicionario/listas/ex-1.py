print("Digite 5 valores: ")
lista = [int(input()), int(input()), int(input()), int(input()), int(input())]
print("-"*19)
print("O maior valor é ",max(lista))
print("O menor valor é ",min(lista))
print("-"*19)
print("Posição do maior é a posição ", lista.index(max(lista)))
print("Posição do menor é a posição ", lista.index(min(lista)))
if max(lista) == min(lista):
    print("As posições dos número iguais do maior e do menor são: ",(lista[0:4]))