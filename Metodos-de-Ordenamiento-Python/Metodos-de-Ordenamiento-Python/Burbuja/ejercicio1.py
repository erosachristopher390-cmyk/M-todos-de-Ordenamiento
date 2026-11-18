def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


numeros = [8, 3, 5, 1, 9, 2]
print("Lista original:", numeros)
print("Lista ordenada:", burbuja(numeros))
