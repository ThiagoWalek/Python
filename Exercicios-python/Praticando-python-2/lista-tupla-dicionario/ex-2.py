classi = (0,1,2,3,4,5,6,7,8,9,10)
time = ("super","tigers","crodile","leakers","hipo","hiper","abelha","t-rex","bicuit","hombre","modri")
print("Times")
print(time)
print("-"*100)
user = input("Digite o nome de um dos times: ")
'''for x in range(0,11):
    if user == x:
        print("O número digitado foi = ",time.find(user))

'''


clasi = sorted(classi)
print("sorted =",classi)





print("Os 5 primeiros colocados foram = ",time[0:5])
print("")
print("Os 4 últimos colocados foram = ")
print("")
print("-"*100)
print("O time informado está no posição = ",time.index(user))
print("")
time = sorted(time)
print("Time ordem =",', '.join(time))