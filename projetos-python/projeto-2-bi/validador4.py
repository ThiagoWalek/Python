cpf_armazen = list()
controle_cpf = 0
qtd_cpfs = 0
cpf_validos = 0
cpf_invalidos = 0
while True:
    cpf_usuario = input("Digite o seu cpf: ")
    cpf_usuario = cpf_usuario.replace(" ", "")
    cpf_usuario = cpf_usuario.replace(".", "")
    cpf_usuario = cpf_usuario.replace("-", "")
    if len(cpf_usuario) == 11 and cpf_usuario.isnumeric():
        print("#"*33)
        print(f"O CPF digitado foi: {cpf_usuario[0:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:]}")
        print("#"*33)
        segundo_dig = 0
        soma_dig = 0
        cpf_9digitos = ""
        cpf_armazen.append({"CPF":[], "VALIDACAO":"PROCESSANDO..."})
        cpf_9digitos = str(cpf_usuario[0:9])
        verificador1 = [10,9,8,7,6,5,4,3,2]
        verificador2 = [11,10,9,8,7,6,5,4,3,2]
        i = 0
        for x, y in zip(cpf_9digitos, verificador1):
            soma_dig += int(x)*y
            i = i+1
        if soma_dig % 11 < 2:
            primeiro_dig = 0
        else:
            primeiro_dig = 11 - soma_dig % 11
        cpf_9digitos += str(primeiro_dig)
        soma_dig = 0
        for x, y in zip(cpf_9digitos, verificador2):
            soma_dig += int(x)*y
            i = i+1
        if soma_dig % 11 < 2:
            segundo_dig = 0
        else:
            segundo_dig = 11 - soma_dig % 11
        cpf_9digitos += str(segundo_dig)
        if cpf_9digitos[-1] == str(cpf_usuario[-1]) and cpf_9digitos[-2] == str(cpf_usuario[-2]):
            cpf_armazen[controle_cpf]["VALIDACAO"] = "VALIDO"
            cpf_validos += 1
        else:
            cpf_armazen[controle_cpf]["VALIDACAO"] = "INVALIDO"
            cpf_invalidos += 1
        cpf_armazen[controle_cpf]["CPF"].append(int(cpf_usuario))
        qtd_cpfs += 1
        controle_cpf += 1
        resp = input(str("Dejesa Continuar o programa? s/n\n"))
        if resp.lower() != "s":
            break
print("\n"," "*20,"----> Resultado CPFs testados <----".upper(),"\n","-"*95)
print("CPFs armazendos: ",cpf_armazen)
print("-"*95)
print(" "*13,f"A quantidade de CPFS testado(s) foi de: {qtd_cpfs}")
print(" "*13,f"A quantdade de CPFS VÁLIDO(S) foram de: {cpf_validos}")
print(" "*13,f"A quantdade de CPFS INVÁLIDO(S) foram de: {cpf_invalidos}")
print(" "*13,f"A porcentagem de CPFS VÁLIDO(S) em relação ao total de CPFS testados foi de: {((cpf_validos*100)/qtd_cpfs):.2f}%")
print(" "*13,f"A porcentagem de CPFS INVÁLIDO(S) em relação ao total de CPFS testados foi de: {((cpf_invalidos*100)/qtd_cpfs):.2f}%")
print("-"*95,"\n")