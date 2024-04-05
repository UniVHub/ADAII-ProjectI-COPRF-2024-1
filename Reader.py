import sys
import os

# Añadir al path el directorio actual
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
import time

from Dynamic_Programming.dynamic_programming import ProgramacionDinamica

def leer_finca(nombre_archivo):
    finca = []
    numeroTablones = 0
    with open(f'Inputs/{nombre_archivo}.txt', 'r') as f:
        numeroTablones = int(next(f))
        next(f)  # Ignorar la primera línea
        for linea in f:
            tr, ts, p = map(int, linea.split(','))
            finca.append((tr, ts, p))
    return (finca,numeroTablones)

def main(nombreArchivo="Prueba7"):
    finca = leer_finca(nombreArchivo)[0]
    numeroTablones = leer_finca(nombreArchivo)[1]
    pd = ProgramacionDinamica(finca)
    startTime = time.time()
    solucion = pd.roPD()
    endTime = time.time()
    print(solucion)
    print (f"Tiempo de ejecución: {endTime - startTime} segundos")
    print("Número de tablones: ", numeroTablones)

if __name__ == "__main__":
    main()