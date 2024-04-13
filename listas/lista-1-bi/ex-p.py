sm = float(input("Quanto você ganha mensalmente? R$"))
pr = float(input("Quantos porcento recebeu de reajuste? "))
rea = (pr/100)*sm
ns = rea+sm
print(f"O seu novo sálario mensal será de: R${(ns):.2f} por mês")