MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas téoricas, mas não pode fazer aulas práticas.")
else:
    print("Menor de idade, não pode tirar a CNH")