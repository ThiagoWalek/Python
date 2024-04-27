nome_cidade = input("Digite o nome de uma cidade: ")
c = nome_cidade
nome_cidade = nome_cidade.split()
if nome_cidade[0].count("São") >= 1:
    print(f"A cidade de '{c}' começa com São")
print("Fim do programa!")