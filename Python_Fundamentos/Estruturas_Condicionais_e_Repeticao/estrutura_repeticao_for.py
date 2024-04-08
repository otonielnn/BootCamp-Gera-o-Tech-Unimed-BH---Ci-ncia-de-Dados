texto = ""
VOGAIS = "AEIOU"


# exemplo usando o "in"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: # executa após finalizar o loop
    print()
    #print("for/else teste.") 

#exemplo usando o "range"
for numero in range(0, 51, 5):
    print(numero, end=" ")