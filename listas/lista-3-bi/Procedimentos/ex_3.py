num = int(input("Digite um número: "))
def primo(num):
    cont = 0
    for i in range(0, num):
        if num % (i+1) == 0:
            cont += 1
    if cont == 2:
        print("Primo")
    else:
        print("Não é primo")
primo(num)