frase = input("Digite uma frase: ")
print("-"*55)
print("-"*55)
print(f"A letra 'A' ou 'a' aparece {frase.count('a'.upper())+frase.count('a'.lower())} vezes na frase digitada")
print("-"*55)
if frase.find('A') == -1:
    print("A letra 'A' não foi digitada!")
    print("-"*55)
else:
    print("A primeira aparição da letra 'A' é na posição - ",frase.find('A'))
    print("-"*55)
y = 0
for x in range (0,len(frase)):
    if frase[x] == 'A' or frase[x] == 'a':
        y = x
if 0 != y:
    print (f"A ultima vez que apareceu o 'a' foi na posição = {y}")
    print("-"*55)
else:
    print("A letra 'a' não foi digitada!")
    print("-"*55)