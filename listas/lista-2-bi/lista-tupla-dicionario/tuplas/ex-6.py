print("Digite 5 palavras:")
tupla = (input(),input(),input(),input(),input())
vowels = ("a","e","i","o","u")
for i in tupla:
    print(f"A palavra {i.upper()} tem essas letras do alfabeto: ",end="")
    for x in i:
        if x in vowels:
            print(x,end=" ")
    print()
