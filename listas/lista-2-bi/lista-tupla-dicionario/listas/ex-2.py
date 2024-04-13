lista = list()
a = 1
while a >= 1:
    user = int(input("Digite um numero: "))
    if user in lista and user != 0:
        user = int(input("Digite o número novamente: "))
        if user == 0:
            a = 0
    elif user not in lista and user != 0:
        lista.append(user)
        if user == 0:
            a = 0

print("-"*40)
print(" "*5,"A lista finalizada ficou assim: ")
print(" "*5,lista)
print("-"*40)
