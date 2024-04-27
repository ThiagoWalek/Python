num = input("Digite um número entre 0 e 9999: ")
num = num.replace(' ', '')
num_len = len(num)
print(num)

milhar = ''
centena = ''
dezena = ''
unidade = ''

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
    
print("O número digitado tem:")
print("Milhar(es) = ",milhar)
print("Centena(s) = ",centena)
print("Dezena(s) = ",dezena)
print("Unidade(s) = ",unidade)