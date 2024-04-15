lista = [["50230537", "João", 10.00, 5.00],["50230376", "Lucas", 9.00, 3.00],["50230645", "Gabriel", 8.00, 10.00],["50230839", "Iago", 1.00, 0.00],["50230765", "Pietra", 6.50, 7.00]]
print("Qual matricula deseja saber:")
print(" "*8,"-"*21)
for i in lista:
    print(" "*8,f"matricula = ",i[0])
print(" "*8,"-"*21)
num = input("Digite uma matricula: ")
for i in lista:
    if num in i[0]:
        print("A pessoa digitada foi: ",i[1])
        print("Nota da prova 1 = ",i[2])
        print("Nota da prova 2 = ",i[3])
        print("-"*35)
