lista = list()
lista_par = list()
lista_impar = list()

def par_or_impar(n):
    if n % 2 == 0:
        lista_par.append(n)
    elif n % 2 != 0:
        lista_impar.append(n)

for i in range(10):
    user = int(input("digite um número: "))
    lista.append(user)
    print(lista)
    par_or_impar(user)
    
print("lista original = ",lista)
print("lista de números pares em ordem crescente = ",sorted(lista_par))
print("lista de números impares em ordem crescente = ",sorted(lista_impar))