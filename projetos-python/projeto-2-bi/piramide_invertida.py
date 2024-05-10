cpf_armazen = list()
cpf_usuario = input("Digite o seu cpf: ")
print(cpf_usuario.isnumeric())
print(len(cpf_usuario))
if len(cpf_usuario) == 11 and cpf_usuario.isnumeric():
    cpf_armazen.append(cpf_usuario)
    print("Cpf valido")
    print("-"*30)
    print(cpf_armazen)
    cpf_9digitos = list(cpf_armazen[0][0:9])
    verificador = [10,9,8,7,6,5,4,3,2]
    print(cpf_9digitos)
    print("-"*30)
    for i in range(0,9):
        print(cpf_9digitos[i]*verificador[i])
else:
    print("Cpf invalido")


