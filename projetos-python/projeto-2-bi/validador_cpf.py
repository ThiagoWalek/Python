cpf_armazen = list(dict())
cpf_usuario = input("Digite o seu cpf: ")
print(cpf_usuario.isnumeric())
print(len(cpf_usuario))
soma_dig = 0
if len(cpf_usuario) == 11 and cpf_usuario.isnumeric():
    cpf_armazen.append({"CPF":[cpf_usuario]})
    print("Cpf valido")
    print("-"*30)
    print(cpf_armazen)
    cpf_9digitos = [cpf_armazen[0:9]]
    print("Cpf 9 = ",cpf_9digitos) #Isso daqui é uma lista dentro de outra lista aaaaaa por isso o for não funcionava cpf_9digitos[0][0][i]
    verificador = [10,9,8,7,6,5,4,3,2]
    soma_dig = 0
    print("-"*30)
    for x, y in zip(cpf_9digitos[0][0], verificador):
        print(f"Resultado da multiplicação entre {int(x)} e {y} é {int(x)*y}")
        soma_dig += int(x)*y
else:
    print("Cpf invalido")

if soma_dig % 11 < 2:
    primeiro_dig = 0
else:
    primeiro_dig = 11 - soma_dig % 11
print(primeiro_dig) 
