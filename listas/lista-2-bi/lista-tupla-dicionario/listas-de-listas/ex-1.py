info = [["alemão", 14.00],["francês", 1400.00],["americano", 1.00],["britânico", 49.00],["russo", 10000.00],["paulista",0.10]]
total = 0
ant = 10000
for i in info:
    total += i[1]
    if i[1] < ant:
        min = i[1]
    ant = i[1]
print("O total dos salários é de = ",total)
print("O total de pessoas informadas foram de = ",len(info))
print("O menor salário foi = ",min)