import os
import sys
from time import sleep, time

from bubble_sort import bubble_sort
from funcs_teste import Verde
from Mensagem_terminal import Mensagem_terminal
from quick_sort import quick_sort
from resultados import mostrar_resultados, retornar_linha, salvar_resultado
from selection_sort import selection_sort


def pega_numeros(arquivo: str) -> list:
    with open(arquivo, 'r') as f:
        numeros: list = f.read().split('\n')
        if numeros[-1] == '':
            numeros.pop()

        try:
            numeros_int: list[int] = list(map(int, numeros))
        except ValueError:
            pass

    return numeros_int if numeros_int else numeros


def limpar_tela(tempo=0.5):
    sleep(tempo)
    os.system('cls' if os.name == 'nt' else 'clear')


def teste_automatico(lista, tecnica, tam) -> [float, str]:
    list_msg = [tecnica.__name__, len(lista)]
    titulo = retornar_linha(list_msg, colun_size=tam)
    temp = Mensagem_terminal()
    temp.add_mensagem(titulo)

    inicio = time()
    lista_ordenada = tecnica(lista)
    fim = time()

    salvar_resultado(lista_ordenada, tecnica)

    return fim - inicio, temp.retornar_mensagem()


def main():
    # Abrir arquivo de numeros
    lista_1000 = pega_numeros('1000_numbers.txt')
    lista_5000 = pega_numeros('5000_numbers.txt')
    lista_10000 = pega_numeros('10000_numbers.txt')
    lista_de_listas = [lista_1000, lista_5000, lista_10000]
    lista_de_funcoes = [bubble_sort, quick_sort, selection_sort]

    limpar_tela()
    lista_de_nome_tamanho_tempo = []
    tamanho_menu = 15
    for lista in lista_de_listas:
        mensagem = Mensagem_terminal()
        list_msg = ["Funcao", "Numeros"]
        msg = retornar_linha(list_msg, colun_size=tamanho_menu)

        mensagem.add_linha(msg)

        mensagem.add_mensagem(msg, Verde)

        for funcao in lista_de_funcoes:
            mensagem.add_linha(msg, " ")
        mensagem.add_linha(msg)
        print(mensagem.retornar_mensagem_colorida(), end="")
        for i, funcao in enumerate(lista_de_funcoes):
            tempo, linha = teste_automatico(lista, funcao, tamanho_menu)
            ntt = [funcao.__name__, len(lista), tempo]
            lista_de_nome_tamanho_tempo.append(ntt)
            limpar_tela(0)
            mensagem.remover_linha(i+2)
            mensagem.add_mensagem(linha, posicao=i+2)
            print(mensagem.retornar_mensagem_colorida(), end="")

        mensagem.add_linha(msg)
        sleep(3)
        limpar_tela()

    mostrar_resultados(lista_de_nome_tamanho_tempo)


if __name__ == '__main__':
    sys.setrecursionlimit(9999)
    main()
