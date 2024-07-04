def digitenumero(msg):
    try:
        n = int(input(msg))
        while str(n).isnumeric() == False:
            msg = "Digite um número inteiro: "
            n = int(input(msg))
    except Exception:
        msg = "Digite um valor inteiro: "
        n = int(input(msg))
    return n
n = digitenumero("Digite um numero: ")
print(f"O número inteiro digitado foi {n}")