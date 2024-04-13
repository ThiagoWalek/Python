cand1 = cand2 = cand3 = branco = nulo = 0
controle = "s"

while controle == "s":
    candidato = int(input("Quer votar em qual candidato 1, 2 ou 3? 4 para branco "))
    if candidato == 1:
        cand1 += 1
    elif candidato == 2:
        cand2 += 1
    elif candidato == 3:
        cand3 += 1
    elif candidato == 4:
        branco += 1
    else:
        nulo += 1

    controle = input("Deseja continuar o programa? s/n ")

validos = cand1 + cand2 + cand3
total_eleitores = validos + branco + nulo
pv = (validos / total_eleitores) * 100
pb = (branco / total_eleitores) * 100
pn = (nulo / total_eleitores) * 100
pa = (cand1 / total_eleitores) * 100
pb = (cand2 / total_eleitores) * 100
pc = (cand3 / total_eleitores) * 100

print(f"O total de eleitores foram de {total_eleitores} eleitores")
print(f"O percentual de votos válidos em relação ao total de eleitores foi de {pv}")
print(f"O percentual de votos em branco em relação ao total de eleitores foi de {pb}")
print(f"O percentual de votos nulos em relação ao total de eleitores foi de {pn}")
print(f"O percentual de votos válidos do candidato 1 em relação ao total de eleitores é de {pa}")
print(f"O percentual de votos válidos do candidato 2 em relação ao total de eleitores é de {pb}")
print(f"O percentual de votos válidos do candidato 3 em relação ao total de eleitores é de {pc}")
print("Fim do Programa!")