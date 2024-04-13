file = open("lorem.txt", "r")
# print(file.read())
while len(linha := file.readline()):
    print(linha)
file.close()
