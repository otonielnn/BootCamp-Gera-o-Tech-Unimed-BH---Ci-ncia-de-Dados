entrada = input().split()

distancia = float(entrada[0])
diametro_1 = float(entrada[1])
diametro_2 = float(entrada[2])

ICM = distancia/(diametro_1 + diametro_2)

print(f"{ICM:.2f}")