print("Digite 5 valores:")
par = 0
tupla = (int(input()),int(input()),int(input()),int(input()),int(input()))
print("-"*45)
print(f"O número 10 aparece {tupla.count(10)} vezes entre os valores digitados")
print("-"*45)
if tupla.count(3) == 0:
    print("Nenhum número digitado foi o numero 3!!!")
else:
    print("O número 3 aparece a primeira vez na posição: ",tupla.index(3))
for x in tupla:
    if x % 2 == 0:
        par += 1
print(f"O total de números pares na tupla é de: {par} número pares")
print("-"*45)