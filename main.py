import os
import sys
from time import time

from buble_sort import bubble_sort
from quick_sort import quick_sort
from selection_sort import selection_sort


def pega_numeros(arquivo):
    with open(arquivo, 'r') as f:
        numeros = f.readlines()
        numeros = [int(n) for n in numeros]
    return numeros


def teste_automatico(lista, tecnica):
    print('-'*20)
    print(tecnica.__name__, f'{len(lista)} numeros')

    inicio = time()
    lista_ordenada = tecnica(lista)
    fim = time()

    diretorio = f'{tecnica.__name__}'

    if not (os.path.exists(f"{diretorio}")):
        os.mkdir(f"{diretorio}")

    arq = f'{diretorio}/{len(lista_ordenada)}_ord_{tecnica.__name__}.txt'

    with open(arq, "w") as f:
        for i in lista_ordenada:
            f.write(f'{i}\n')

    return fim - inicio


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def espera_e_limpa():
    limpar_tela()


def main():
    # Abrir arquivo de numeros
    lista_1000 = pega_numeros('1000_numbers.txt')
    lista_5000 = pega_numeros('5000_numbers.txt')
    lista_10000 = pega_numeros('10000_numbers.txt')
    lista_de_listas = [lista_1000, lista_5000, lista_10000]
    # Teste automatico
    lista_de_funcoes = [bubble_sort,
                        quick_sort,
                        selection_sort]
    lista_de_nome_tamanho_tempo = []
    for lista in lista_de_listas:
        for funcao in lista_de_funcoes:
            tempo = teste_automatico(lista, funcao)
            ntt = [funcao.__name__, len(lista), tempo]
            lista_de_nome_tamanho_tempo.append(ntt)

        espera_e_limpa()

    lista_de_nome_tamanho_tempo.sort(key=lambda x: x[2])
    cont = 0
    for ntt in lista_de_nome_tamanho_tempo:
        if cont == 3:
            print('-'*20)
            cont = 0
        print(f"{ntt[0]}_{ntt[1]}:\t{ntt[2]}")
        cont += 1


if __name__ == '__main__':
    sys.setrecursionlimit(9999)
    main()
