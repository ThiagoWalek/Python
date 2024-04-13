num = input("Digite um número entre 0 e 9999: ")
num = num.replace(' ', '')
num_len = len(num)
print(num)

milhar = ''
centena = ''
dezena = ''
unidade = ''

# 9999

if num_len == 1:
    unidade = num[0]
elif num_len == 2:
    dezena = num[0]
    unidade = num[1]
elif num_len == 3:
    centena = num[0]
    dezena = num[1]
    unidade = num[2]
elif num_len == 4:
    milhar = num[0]
    centena = num[1]
    dezena= num[2]
    unidade = num[3]
    
print(f"O número digitado tem {milhar} milhar(es), {centena} centena(s), {milhar} dezena(s), {unidade} unidade(s).")

'''print("Unidades = ",unidade)
print("dezenas = ",dezena)
print("Centenas = ",centena)
print("Milhares = ",milhar)'''