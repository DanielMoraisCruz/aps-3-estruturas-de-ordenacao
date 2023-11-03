def quick_sort(lista, mostrar_passos=False) -> list:
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menor = [i for i in lista[1:] if i <= pivo]
        maior = [i for i in lista[1:] if i > pivo]
        res = quick_sort(menor, mostrar_passos) + \
            [pivo] + quick_sort(maior, mostrar_passos)
        return res
