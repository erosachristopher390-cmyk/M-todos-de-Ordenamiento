def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] < actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista


numeros = [10, 45, 20, 5, 30, 15]
print("Lista original:", numeros)
print("Lista ordenada de mayor a menor:", insercion(numeros))
