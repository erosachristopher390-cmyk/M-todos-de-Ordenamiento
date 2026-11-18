def seleccion(lista):
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista


numeros = [29, 10, 14, 37, 13, 5]
print("Lista original:", numeros)
print("Lista ordenada:", seleccion(numeros))
