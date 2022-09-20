valores = input().split()

tempo_gasto = int(valores[0])
velocidade_media = int(valores[1])

litro = velocidade_media / 12
resultado = tempo_gasto * litro

print(f"{resultado:1.3f}")
