from funcs_teste import t_color


def bubble_sort(lista, mostrar_passos=False):
    for a in range(len(lista)):
        for b in range(len(lista)-1):
            l_antiga = lista.copy() if mostrar_passos else None
            if lista[b] > lista[b+1]:
                lista[b], lista[b+1] = lista[b+1], lista[b]
            t_color(l_antiga, lista.copy()) if mostrar_passos else None

    return lista
