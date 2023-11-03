def selection_sort(lista, mostrar_passos=False) -> list:
    for i in range(len(lista)):
        print(lista) if mostrar_passos else None
        exchange = False
        menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
                exchange = True
        if exchange:
            lista[i], lista[menor] = lista[menor], lista[i]
    return lista
