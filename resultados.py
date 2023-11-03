import os

from funcs_teste import Verde
from Mensagem_terminal import Mensagem_terminal


def salvar_resultado(lista, tecnica) -> None:
    if isinstance(tecnica, str):
        diretorio = f'{tecnica}'
    else:
        diretorio = f'{tecnica.__name__}'

    if not (os.path.exists(f"{diretorio}")):
        os.mkdir(f"{diretorio}")

    if isinstance(lista, list):
        arq = f'{diretorio}/{len(lista)}_ord_{diretorio}.txt'
        with open(arq, "w") as f:
            for linha in lista:
                f.write(f'{linha}\n')
    else:
        # nome_arquivo
        nome_arquivo = diretorio + "_1"
        while os.path.exists(f"{diretorio}/{nome_arquivo}.txt"):
            indice = nome_arquivo.rfind("_")
            x = int(nome_arquivo[indice+1:])
            nome_arquivo = diretorio + f"_{x+1}"

        arq = f'{diretorio}/{nome_arquivo}.txt'
        with open(arq, "w") as f:
            f.write(f'{lista}')


def retornar_linha(list_msg, colun_size: int = 10) -> str:
    msg = ""
    colun_size += 2
    for mensagem in list_msg:
        texto = str(mensagem)
        if isinstance(mensagem, float):
            texto = f" {mensagem:.10f} "
        else:
            texto = f" {mensagem} "
        if mensagem == list_msg[-1] and len(list_msg) > 2:
            msg += texto.rjust(colun_size)
        elif mensagem == list_msg[0] and len(list_msg) > 2:
            msg += texto.ljust(colun_size)
        else:
            msg += texto.center(colun_size)

        msg += "|" if list_msg[-1] != mensagem else ""

    msg = "|" + msg + "|"
    return msg


def retornar_lista(lista, tam) -> str:
    cont = 0
    msg_total = Mensagem_terminal()

    for ntt in lista:
        list_msg = [f"{ntt[0]}_{ntt[1]}", ntt[2]]
        msg = retornar_linha(list_msg, colun_size=tam)
        if cont == 3:
            msg_total.add_linha(msg)
            cont = 0
        msg_total.add_mensagem(msg)
        cont += 1
        if ntt == lista[-1]:
            msg_total.add_linha(msg)
    return msg_total.retornar_mensagem()


def retornar_media_de_tempo(lista) -> list:
    lista_funcoes: list = []
    lista.sort(key=lambda x: x[0])

    lista_funcoes = []
    nomes_adicionados = []
    for j in range(3):
        soma = 0
        for i in range(3):
            if lista[0][0] not in nomes_adicionados:
                nomes_adicionados.append(lista[0][0])
            soma += lista[0][2]
            lista.remove(lista[0])
        media = soma/3
        lista_funcoes.append([f"Media: {nomes_adicionados[j]}", media])

    return lista_funcoes


def mostrar_resultados(lista) -> None:
    # Define Largura da Tabela
    tamanho = 0
    lista_medias = retornar_media_de_tempo(lista.copy())
    # pega o maior numero da lista
    lista_medias.sort(key=lambda x: x[1])

    maior_numero = lista_medias[-1][1]
    maior_numero = f"{maior_numero:.7f}"
    # pega a maior nome da lista
    lista_medias.sort(key=lambda x: len(x[0]))
    maior_nome = lista_medias[-1][0]
    # Compara pra ver quem é maior
    if len(str(maior_nome)) > len(str(maior_numero)):
        tamanho = len(str(maior_nome))
    else:
        tamanho = len(str(maior_numero))

    # PRIMEIRA TABELA
    list_msg = ["Funcao_Numeros", "Tempo"]
    msg = retornar_linha(list_msg, colun_size=tamanho)

    resultado = Mensagem_terminal()
    # ADD TITULO
    resultado.add_linha(msg)
    resultado.add_mensagem(msg, Verde)
    resultado.add_linha(msg)

    # ADD VALORES
    valores = retornar_lista(lista.copy(), tam=tamanho)
    resultado.add_mensagem(valores)

    # SEGUNDA TABELA
    list_msg2 = ["Funcao", "Media"]
    msg2 = retornar_linha(list_msg2, colun_size=tamanho)

    resultado.add_linha(msg2)
    resultado.add_mensagem(msg2, Verde)
    resultado.add_linha(msg2)

    # ADD VALORES
    medias = []

    lista_medias.sort(key=lambda x: x[1])
    for lista_ in lista_medias:
        medias.append(retornar_linha(lista_, colun_size=tamanho))
    medias.sort(key=lambda x: x[1])
    for i in medias:
        resultado.add_mensagem(i)

    resultado.add_linha(msg2)

    # SALVAR RESULTADO
    salvar_resultado(resultado.retornar_mensagem(), "resultados")

    print(resultado.retornar_mensagem_colorida())
