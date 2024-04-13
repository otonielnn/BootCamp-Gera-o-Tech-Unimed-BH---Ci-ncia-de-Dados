file = open("teste.txt", "w")

file.write("Escrevendo em um arquivo novo\n")
file.writelines(["escrevendo\t", "um\t", "novo\t", "texto\t"])
file.close()
