def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
        # print(lista)
    return lista


if __name__ == '__main__':

    print(bubble_sort([5, 3, 2, 4, 7, 1, 0, 6]))
    print(bubble_sort([5, 3, 2, 4, 7, 1, 0, 6, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(bubble_sort([5, 3, 2, 4, 7, 1, 0, 6,
          8, 9, 10, 11, 12, 13, 14, 15, 16]))
