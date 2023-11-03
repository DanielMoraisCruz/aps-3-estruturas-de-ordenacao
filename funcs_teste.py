Verde = '\033[92m'
Vermelho = '\033[91m'
Fim = '\033[0m'


def print_colorido(texto, cor=None) -> str:
    return f"{(cor + texto + Fim) if cor else texto}"


def t_color(lista_antiga, lista_atual) -> None:
    alteracao = False
    nova_lista = ""
    for i in range(len(lista_atual)):
        if lista_atual[i] != lista_antiga[i]:
            item = print_colorido(str(lista_atual[i]), Vermelho)
            nova_lista += item
            alteracao = True
        else:
            nova_lista += str(lista_atual[i]) + " "

    print(nova_lista) if alteracao else None
