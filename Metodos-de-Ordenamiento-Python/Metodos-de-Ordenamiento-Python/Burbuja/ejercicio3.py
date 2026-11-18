def burbuja(edades):
    n = len(edades)
    for i in range(n):
        for j in range(n - i - 1):
            if edades[j] > edades[j + 1]:
                edades[j], edades[j + 1] = edades[j + 1], edades[j]
    return edades


edades = [25, 18, 40, 32, 21, 16]
print("Edades originales:", edades)
print("Edades ordenadas:", burbuja(edades))
