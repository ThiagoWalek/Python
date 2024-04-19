dicionario = [dict(),dict(),dict()]
for i in range(3):
    print("-"*48)
    pessoa = input(f"Digite o nome da pessoa que deseja adicionar({i}): ")
    media = float(input("Digite a média dessa pessoa: "))
    if media >= 6:
        cond = "Aluno na média"
    elif media < 6:
        cond = "Aluno em recuperação!"
    dicionario[i]["Nome"] = pessoa.capitalize()
    dicionario[i]["Média"] = media
    dicionario[i]["Condição"] = cond
    print(dicionario)
print("-"*48)
for i in range(3):
    print(f"Informações da pessoa({i+1}):")
    print(" "*8,f"Nome = {dicionario[i]["Nome"]}")
    print(" "*8,f"Média = {dicionario[i]["Média"]}")
    print(" "*8,f"Condição = {dicionario[i]["Condição"]}")
    print("-"*48)