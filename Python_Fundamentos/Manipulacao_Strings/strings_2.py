nome = "Otoniel"
idade = 20
profissão = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Otoniel", "idade": 20}

# Old style %
print("Nome: %s Idade: %d" %(nome, idade))

# format
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade)) # passando indice
print("Nome: {0} Idade: {1}. {0}".format(nome, idade)) # passando indice
print("Nome: {name} Idade: {age}. {name} {age}".format(name=nome, age=idade)) # repetindo a variavel
print("Nome: {nome} Idade {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} saldo: {saldo:.2f}")