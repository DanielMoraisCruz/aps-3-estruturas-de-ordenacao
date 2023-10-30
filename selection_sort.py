def selection_sort(lista):
    try:
        for i in range(len(lista)):
            menor = i
            for j in range(i+1, len(lista)):
                if lista[j] < lista[menor]:
                    menor = j
            lista[i], lista[menor] = lista[menor], lista[i]
            # print(lista)
        return lista
    except Exception as e:
        raise e


if __name__ == '__main__':
    print(selection_sort([5]))
    print(selection_sort([5, 3, 2, 4, 7, 1, 0, 6]))
    print(selection_sort(
        [5, 3, 2, 4, 7, 1, 0, 6, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(selection_sort([5, 3, 2, 4, 7, 1, 0,
          6, 8, 9, 10, 11, 12, 13, 14, 15, -16]))
