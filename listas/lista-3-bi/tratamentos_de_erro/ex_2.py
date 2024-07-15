print("1 - QUADRADO DE UM NÚMERO\n2 - RAIZ CÚBICA DE UM NÚMERO\n3 - FATORIAL DE UM NÚMERO\n","-"*24)

def opcao_valid():
    while True:
        try:
            opc = int(input("Escolha uma das opções: "))
            if opc == 1:
                quad()
            elif opc == 2:
                cub()
            elif opc == 3:
                fat()
            break
        except Exception:
            print("Opção inválida!!!")
def quad():
    print("1 - QUADRADO DE UM NÚMERO")
    while True:
        try:
            num = int(input("Digite um número: "))
            print(f"O quadrado de {num} é {num**2}")
            break
        except Exception:
            print("Digito inválido!!!")
def cub():
    print("1 - RAIZ CÚBICA DE UM NÚMERO")
    while True:
        try:
            num = int(input("Digite um número: "))
            print(f"A raiz cúbica de {num} é {num**(1/3)}")
            break
        except Exception:
            print("Digito inválido!!!")
def fat():
    print("3 - FATORIAL DE UM NÚMERO")
    while True:
        try:
            num = int(input("Digite um número: "))
            fatorial = 1
            for i in range(1, num + 1):
                fatorial *= i
            print(f"A raiz cúbica de {num} é {fatorial}")
            break
        except Exception:
            print("Digito inválido!!!")
opcao_valid()