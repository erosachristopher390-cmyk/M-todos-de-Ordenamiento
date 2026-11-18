def seleccion(edades):
    n = len(edades)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if edades[j] < edades[minimo]:
                minimo = j
        edades[i], edades[minimo] = edades[minimo], edades[i]
    return edades


edades = [35, 20, 45, 18, 29, 50]
print("Edades originales:", edades)
print("Edades ordenadas:", seleccion(edades))
