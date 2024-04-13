con = 0
while con == 0:
    f = float(input("Digite um valor em Fahrenheit: "))
    c = (f - 32) * (5/9)
    print("O resultado em Celsius foi de: {:.2f}C\n".format(c))
    con = int(input("Dejesa continuar 0 / 1?"))

    

