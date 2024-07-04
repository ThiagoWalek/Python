num = int(input("Digite um número: "))
i = 1
def primo():
    global num
    global i
    cont = 0
    while True:
        if num % i == 0:
            cont += 1
        i += 1
        if num == i:
            break
    if cont == 2:
        print("Primo")
    elif cont > 2:
        print("Não é primo")
primo()