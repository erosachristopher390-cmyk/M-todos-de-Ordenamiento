def insercion(precios):
    for i in range(1, len(precios)):
        actual = precios[i]
        j = i - 1
        while j >= 0 and precios[j] > actual:
            precios[j + 1] = precios[j]
            j -= 1
        precios[j + 1] = actual
    return precios


precios = [250, 120, 500, 80, 350, 150]
print("Precios originales:", precios)
print("Precios ordenados:", insercion(precios))
