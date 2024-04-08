def mensagem(nome):
    print('executando mensagem')
    return f'Oi {nome}'


def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Olá tudo bem com você {nome}?'


def executar(funcao, parametro):
    print('executando executar')
    return funcao(parametro)


print(executar(mensagem, 'Otoniel'))
print(executar(mensagem_longa, 'Otoniel'))
