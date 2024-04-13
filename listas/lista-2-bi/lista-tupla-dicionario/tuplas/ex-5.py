preco = ("1.75","2.00","15.90","25.00","4.20","9.99","120.32","22.30","34.90")
produto = ("Lápis", "Borracha", "Caderno", "Estojo", "Tranferidor","Compasso","Mochla","Canetas","Livro")
print("-"*34)
print("        Listagem de preços".upper())
print("-"*34)
for i, x in zip(produto, preco):
    print(i,end="")
    print("."*(31-len(i)),"R$",x)
