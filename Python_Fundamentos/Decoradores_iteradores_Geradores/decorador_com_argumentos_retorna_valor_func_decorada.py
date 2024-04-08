def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('faz algo antes de executar')
        resultado = funcao(*args, **kwargs)
        print('faz algo depois de executar')
        return resultado

    return envelope


@meu_decorador
def ola_mundo(nome, outro_parametro):
    print(f'Olá mundo! {nome}')
    return nome.upper()


resultado = ola_mundo("Otoniel", 21)
print(resultado)
