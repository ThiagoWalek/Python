# valor = 25
# e = 1
# qtd = 0
# conta = 0
# roda = 0
# for i in range(valor):
#     if i % 2 == 1:
#         print("Raiz quadrada impar")
#         if roda > 0:
#             conta = e*(e+2)
#         print(conta)
#         if e <= i and roda == 0:
#             qtd += 1
#             print("qtd 1 caso =",qtd)
#         elif conta <= i:
#             qtd += 1
#             print("qtd 2 caso =",qtd)
#         roda += 1
#     else:
#         print("Raiz quadrada par (2.4.6.8)")
# print(qtd)
valor = 25
e = 1
qtd = 0
conta = 0
roda = 0
for i in range(valor):
    if i % 2 != 0:
        print("Raiz quadrada impar")
        if roda > 0:
            conta = e*(e+2)
        elif e <= valor and roda == 0:
            qtd += 1
            print("qtd 1 caso =",qtd)
        elif conta <= i:
            qtd += 1
            print("qtd 2 caso =",qtd)
        roda += 1
        e += 1
print(qtd)