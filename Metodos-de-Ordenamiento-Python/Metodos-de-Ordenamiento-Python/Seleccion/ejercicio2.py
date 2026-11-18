def seleccion(calificaciones):
    n = len(calificaciones)
    for i in range(n):
        mayor = i
        for j in range(i + 1, n):
            if calificaciones[j] > calificaciones[mayor]:
                mayor = j
        calificaciones[i], calificaciones[mayor] = calificaciones[mayor], calificaciones[i]
    return calificaciones


calificaciones = [75, 90, 65, 100, 80, 85]
print("Calificaciones originales:", calificaciones)
print("Calificaciones ordenadas:", seleccion(calificaciones))
