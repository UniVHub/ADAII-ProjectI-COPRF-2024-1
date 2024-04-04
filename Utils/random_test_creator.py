from random import randint

# Función para generar pruebas aleatorias
def generar_pruebas():
    n_fincas = 100
    n_tablones = 15                                 # N. tablones por finca 
    pruebas = []
    for _ in range(n_fincas):
        finca = []
        for _ in range(n_tablones):
            tiempo_supervivencia = randint(5, 30)   # Variar según la necesidad
            tiempo_riego = randint(1, 10)           # Variar según la necesidad
            prioridad = randint(1, 4)
            finca.append((tiempo_supervivencia, tiempo_riego, prioridad))
        pruebas.append(finca)
    return pruebas
