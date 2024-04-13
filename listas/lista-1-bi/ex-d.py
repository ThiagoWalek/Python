t = float(input("Qual foi o tempo gasto?(em horas) "))
vel_med = float(input("Qual foi a velocidade média?(em km/h) "))
dist = t * vel_med
litros_usados = dist / 12

print("Dados da viagem:\nVelocidade média = {:.2f} km/h\nTempo gasto = {:.2f} h\nDistância = {:.2f} km\nLitros gastos = {:.2f} L".format(vel_med, t, dist, litros_usados))

