num = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez")
user = int(input("Digite um numero entre 0 e 10: "))
while user < 0 or user > 10:
    user = int(input("Digite um numero entre 0 e 10: "))
for x in range(0,11):
    if user == x:
        print("O número digitado foi = ",num[x])