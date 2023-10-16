def quick_sort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menor = [i for i in lista[1:] if i <= pivo]
        maior = [i for i in lista[1:] if i > pivo]
        return quick_sort(menor) + [pivo] + quick_sort(maior)


if __name__ == '__main__':
    print(quick_sort([5]))
    print(quick_sort([5, 3, 2, 4, 7, 1, 0, 6]))
    print(quick_sort([5, 3, 2, 4, 7, 1, 0, 6, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(quick_sort([5, 3, 2, 4, 7, 1, 0, 6,
          8, 9, 10, 11, 12, 13, 14, 15, -16]))
