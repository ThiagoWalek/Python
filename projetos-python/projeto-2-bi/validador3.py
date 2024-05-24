cpf_armazen = list()
controle_cpf = 0
qtd_cpfs = 0
cpf_validos = 0
cpf_invalidos = 0
while True:
    cpf_usuario = input("Digite o seu cpf: ")
    print(cpf_usuario.isnumeric())
    print(len(cpf_usuario))
    if len(cpf_usuario) == 11 and cpf_usuario.isnumeric():
        segundo_dig = 0
        soma_dig = 0
        cpf_9digitos = ""
        cpf_armazen.append({"CPF":[], "VALIDACAO":"PROCESSANDO..."}) #Uma lista dentro de um dicionario
        print(cpf_armazen)
        print("Cpf valido")
        print("-"*30)
        print(cpf_armazen)
        cpf_9digitos = str(cpf_usuario[0:9])
        print("Cpf 9 = ",cpf_9digitos) #Isso daqui é uma lista dentro de outra lista aaaaaa por isso o for não funcionava cpf_9digitos[0][0][i]

        #Inicializamos a variaveis dos verificadores e controladores
        verificador1 = [10,9,8,7,6,5,4,3,2]
        verificador2 = [11,10,9,8,7,6,5,4,3,2]
        i = 0
        print("-"*30)
        #Calculamos o primeiro a soma de todos os digitos dos 9 primeiros valores 
        for x, y in zip(cpf_9digitos, verificador1):
            print(f"Resultado da multiplicação entre {int(x)} e {y} é {int(x)*y}")
            soma_dig += int(x)*y
            i = i+1
        #Inserimos o primeiro digito no cpf_9digitos = 10 valores
        if soma_dig % 11 < 2:
            primeiro_dig = 0
        else:
            primeiro_dig = 11 - soma_dig % 11
        print("Cpf 9dig = ",cpf_9digitos)
        print("soma dgitos = ",soma_dig)
        print("primeiro digito: ",primeiro_dig) 
        #Adicionamos o primeiro digito na frente dos outros 9 digitos
        cpf_9digitos += str(primeiro_dig)
        print("cpf 9dig = ",cpf_9digitos)
        #Zeramos a variavel soma 
        #Calculo da soma do 2 digito
        soma_dig = 0
        for x, y in zip(cpf_9digitos, verificador2):
            print(f"Resultado da multiplicação entre {int(x)} e {y} é {int(x)*y}")
            soma_dig += int(x)*y
            i = i+1
        print("A soma do 2 digito foi de:",soma_dig) 
        #caculo do 2 digito
        if soma_dig % 11 < 2:
            segundo_dig = 0
        else:
            segundo_dig = 11 - soma_dig % 11
        print(soma_dig)
        print("Segundo digito: ",segundo_dig)
        #Adicionamos o segundo digito a variavel cpf_9digitos
        cpf_9digitos += str(segundo_dig)
        print("CPF 9dig = ",cpf_9digitos)
        #Vendo se o cpf é realmente valido
        if cpf_9digitos[-1] == str(cpf_usuario[-1]) and cpf_9digitos[-2] == str(cpf_usuario[-2]):
            print("CPF valido valido")
            cpf_armazen[controle_cpf]["VALIDACAO"] = "VALIDO"
            print(cpf_armazen)
            cpf_validos += 1
        else:
            print("CPF invalido invalido")
            cpf_armazen[controle_cpf]["VALIDACAO"] = "INVALIDO"
            print(cpf_armazen)
            cpf_invalidos += 1
        cpf_armazen[controle_cpf]["CPF"].append(int(cpf_usuario))
        print(cpf_armazen)
        qtd_cpfs += 1
        controle_cpf += 1
        if input(str("Dejesa Continuar o programa? s/n")) != "s":
            break
# Após o laço while iremos imprimir os filtros sobre os cpfs testados
print("-"*95)
print(cpf_armazen)
print(" "*13,f"A quantidade de CPFS testado(s) foi de: {qtd_cpfs}")
print(" "*13,f"A quantdade de CPFS VÁLIDO(S) foram de: {cpf_validos}")
print(" "*13,f"A quantdade de CPFS INVÁLIDO(S) foram de: {cpf_invalidos}")
print(" "*13,f"A porcentagem de CPFS VÁLIDO(S) em relação ao total de CPFS testados foi de: {(cpf_validos*100)/qtd_cpfs}%")
print(" "*13,f"A porcentagem de CPFS INVÁLIDO(S) em relação ao total de CPFS testados foi de: {(cpf_invalidos*100)/qtd_cpfs}%")
print("-"*95)




