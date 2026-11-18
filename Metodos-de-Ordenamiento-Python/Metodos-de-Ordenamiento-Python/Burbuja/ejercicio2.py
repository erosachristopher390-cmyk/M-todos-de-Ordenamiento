def burbuja(calificaciones):
    n = len(calificaciones)
    for i in range(n):
        for j in range(n - i - 1):
            if calificaciones[j] > calificaciones[j + 1]:
                calificaciones[j], calificaciones[j + 1] = calificaciones[j + 1], calificaciones[j]
    return calificaciones


calificaciones = [85, 70, 95, 60, 78, 90]
print("Calificaciones originales:", calificaciones)
print("Calificaciones ordenadas:", burbuja(calificaciones))
