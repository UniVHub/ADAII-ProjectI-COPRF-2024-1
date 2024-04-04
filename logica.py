from Brute_Force.brute_force_S1 import FuerzaBruta
from Dynamic_Programming.dinamic_programming import ProgramacionDinamica
from Greedy_Programming.greedy_programming import ProgramacionVoraz


class Logica:
    def __init__(self):
        self.posiblesAlgoritmos = {
            "AFB": "Algoritmo de Fuerza Bruta",
            "APV": "Algoritmo de Programación Voraz",
            "APD": "Algoritmo de Programación Dinámica",
        }

        self.algoritmoSeleccionado = None
        self.numeroTablones = None
        self.finca = None
        self.resultadoOptimo = None

    # ---------------------------------- Getters --------------------------------- #
    def getPosiblesAlgoritmos(self):
        return self.posiblesAlgoritmos

    def getAlgoritmoSeleccionado(self):
        return self.algoritmoSeleccionado

    def getNumeroTablones(self):
        return self.numeroTablones

    def getFinca(self):
        return self.finca

    def getResultadoOptimo(self):
        return self.resultadoOptimo

    def getValorAlgoritmo(self):
        return self.posiblesAlgoritmos[self.algoritmoSeleccionado]

    # ---------------------------------- Setters --------------------------------- #
    def setAlgoritmoSeleccionado(self, keyAlgoritmo):
        if keyAlgoritmo in self.posiblesAlgoritmos:
            self.algoritmoSeleccionado = keyAlgoritmo

    def setNumeroTablones(self, numeroTablones):
        try:
            self.numeroTablones = int(numeroTablones)
        except:
            print("Error al convertir el número de tablones a entero")

    def setFinca(self, finca):
        self.finca = finca

    def setResultadoOptimo(self, resultadoOptimo):
        self.resultadoOptimo = resultadoOptimo

    # ---------------------------- Metodos Adicionales --------------------------- #
    def reiniciar(self):
        self.algoritmoSeleccionado = None
        self.numeroTablones = None
        self.finca = None
        self.resultadoOptimo = None

    def subir_archivo(self, archivo):
        try:
            with open(archivo, "r") as f:
                # Leer la primera línea que contiene el número de tablones
                n = int(f.readline().strip())

                # Inicializar una lista para almacenar los datos de los tablones
                tablones = []

                # Leer las siguientes líneas
                for linea in f:
                    # Saltar las líneas vacías
                    if linea.strip() == "":
                        continue

                    # Dividir la línea por las comas
                    partes = linea.strip().split(",")

                    # Verificar que la línea tiene tres partes
                    if len(partes) != 3:
                        return ["Formato de tablon incorrecto"]

                    # Convertir las partes a enteros y añadir los datos del tablón a la lista
                    try:
                        ts, tr, p = map(int, partes)
                        tablones.append((ts, tr, p))
                    except ValueError:
                        return ["Los datos del tablón deben ser números enteros"]

                # Verificar que el número de tablones coincide con n
                if len(tablones) != n:
                    return ["El número de tablones no coincide con n"]

                # Retornar la lista de tablones
                self.setFinca(tablones)
                self.setNumeroTablones(n)
                return tablones

        except ValueError:
            return ["El número de tablones debe ser un número entero"]
        except Exception as e:
            # Retornar una lista vacía en caso de esrror
            return ["Error al leer el archivo" + str(e)]

    def usar_algoritmo(self):
        if self.algoritmoSeleccionado == "AFB":
            riegoOptimo = FuerzaBruta(self.finca)
            solucion = riegoOptimo.calcularResultadoOptimo()
            self.resultadoOptimo = solucion
            return solucion

        elif self.algoritmoSeleccionado == "APV":
            riegoOptimo = ProgramacionVoraz(self.finca)
            solucion = riegoOptimo.roV()
            self.resultadoOptimo = solucion
            return [solucion[0]] + solucion[1]
        
        elif self.algoritmoSeleccionado == "APD":
            riegoOptimo = ProgramacionDinamica(self.finca)
            solucion = riegoOptimo.calcularResultadoOptimo()
            self.resultadoOptimo = solucion
            return solucion
        
        else:
            return ["Algoritmo no seleccionado"]
