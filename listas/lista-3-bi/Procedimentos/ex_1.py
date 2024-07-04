num = int(input("Digite um número: "))
def dec_bin():
    global num
    bin = ""
    while num != 0:
        if num % 2 == 0:
            bin += "0"
        elif num % 2 != 0:
            bin += "1"
        num = round(num/2)
    if num == 0:
        print(bin[::-1])
dec_bin()