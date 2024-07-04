def visualizar(num, esc):
    s = []
    soma = 0
    global a
    if esc == "s".upper():
        a = True
    for i in range(0, num):
        soma += i+1 #paramos aqui - demorou mas foi, era só usar a mesma conta que usei no append abaixo, e somar em uma variavel
        s.append(str(i+1))
        #print(s)
        if a == True:
           res =  " + ".join(s)
        else:
            res = "Soma"
    #print(s)
    print(res," = ",soma)
    print("*"*50)

print("*"*50)
vz = int(input("Quantas vezes deseja rodar o programa: "))
for y in range(0, vz):
    num = int(input("Digite um número: "))
    esc = input("Deseja visualizar o processo da soma s/n ").upper() 
    a = False
    visualizar(num, esc)
print("*"*50)