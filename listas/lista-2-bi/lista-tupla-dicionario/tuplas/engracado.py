classi = (0,1,2,3,4,5,6,7,8,9,10)
time = ("super","tigers","crodile","leakers","hipo","hiper","abelha","t-rex","bicuit","hombre")
print("-"*100)
print("Times")
print(time)
print("-"*100)
user = input("Digite o nome de um dos times: ")


print(" "*10,f"Os 5 primeiros colocados foram = {time[0:5]}\n")
print(" "*10,f"Os 4 últimos colocados foram = {time[-4:]}\n")
print(" "*10,f"O time informado está no posição = {time.index(user)}\n""-"*100)#Aqui esta a parte engraçada do programa na linha 12 ao lado do \n ele imprimi 100 vezes o resultado de todo print, tem que se colocar uma virgula para separar os dois \n","-"*100) assim
time = sorted(time)
print(" "*4,"Time ordem =",', '.join(time))
print("-"*100)