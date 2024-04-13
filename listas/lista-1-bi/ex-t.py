print("Para sabermos a velocidade de um projétil precisamos de: ")
dist = float(input("Digite a distância percorrida em km: "))
time = float(input("Digite o tempo percorrido em minutos: "))

vel = ((dist * 1000) / time * 60)
print(f"A velocidade do projétil é de: {(vel):.1f}m/s")