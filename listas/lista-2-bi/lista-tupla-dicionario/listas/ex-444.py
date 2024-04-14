lista_par = list()
lista_impar = list()    
lista = list()

def par_or_impar(n):
    if n % 2 == 0:
        lista_par.append(n)
    elif n % 2 != 0:
        lista_impar.append(n)
for i in range(8):
    user = int(input("Digite um número: "))
    lista.append(user)
    par_or_impar(user)
print("lista = ",lista)
print("lista de números pares = ",lista_par)
print("lista de números ímpares = ",lista_impar)

    