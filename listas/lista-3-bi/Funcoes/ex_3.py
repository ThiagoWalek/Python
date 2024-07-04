def idade(n, ida):
    while n == "":
        n = input("Não informou seu nome, digite novamente: ")
    while ida == "" or ida.isnumeric() == False:
        ida = input("Não informou corretamente sua idade, digite novamente: ")
    if int(ida) >= 18:
        print(f"Você {n} é maior de idade!")
    else:
        print(f"Você {n} é menor de idade!")
        
nom = input("Digite seu nome: ")
ida = input("Digite sua idade: ")
idade(nom, ida)