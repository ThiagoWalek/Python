lista = list()
a = 0
user_anterior = 0
control = True
while control == True and a < 10:
    user = int(input("Digite um numero: "))
    if user in lista and user != 0:
        user = int(input("Digite o número novamente: "))
        if user == 0:
            control = False
    elif user not in lista and user != 0:
        lista.append(user)
        if user == 0:
            control = False
    if user_anterior > user:
        lista.append(user)
        lista.append(user_anterior)
    else:
        lista.append(user_anterior)
        lista.append(user)
    user_anterior = user
    a += 1
print("-"*40)
print(" "*5,"A lista finalizada ficou assim: ")
print(" "*5,lista)
print("-"*40)