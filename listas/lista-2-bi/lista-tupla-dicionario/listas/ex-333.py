lista = list()
a = 0
ant = 0
while True and a < 10:
    user = int(input("Digite um numero: "))
    if user in lista:
        user = int(input("Digite o número novamente: "))
    elif user not in lista:
        if user > ant and a > 0:
            lista.append(ant)
            lista.append(user)
        else:
            lista.append(user)
            lista.append(ant)
    ant = user
    a += 1
print("-"*40)
print(" "*5,"A lista finalizada ficou assim: ")
print(" "*5,lista)
print("-"*40)