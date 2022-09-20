nome = "oToNiel"

print(nome.upper())
print(nome.lower())
print(nome.title()) # deixa apenas a primeira letra maiúscula

texto = " olá mundo! "

print(texto)
print(texto.strip()) # retira espaços no começo e no final
print(texto.lstrip()) # lstrip = left strip
print(texto.rstrip()) # rstrip = right strip

menu = "Python"

print("###" + menu + "###")
print(menu.center(12))
print(menu.center(12, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))
