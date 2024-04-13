frase = input("Digite uma frase: ")
print(f"A letra 'A' ou 'a' aparece {frase.count('a'.upper())+frase.count('a'.lower())} vezes na frase digitada")
print("A primeira aparição da letra 'A' é na posição - ",frase.find('A'))
for x in range (0,len(frase)):
    if frase[x] == 'A' or frase[x] == 'a':
        y = x
print (f'A ultima vez que apareceu o A foi na posição = {y}')