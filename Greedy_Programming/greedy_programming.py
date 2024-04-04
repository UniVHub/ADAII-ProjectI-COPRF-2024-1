class ProgramacionVoraz:
    def __init__(self, finca):
        self.finca = finca
        self.n = len(finca)

    # Función que calcula la heurística de un tablón, determinada como el tiempo de riego dividido entre la prioridad del mismo.
    # (int, int, int) -> float
    def heuristica(self, tablon):
        tr = tablon[1]
        p = tablon[2]

        return tr/p

    # Función que calcula el costo de riego de un tablón en un tiempo dado.
    # (int, int, int), int -> int
    def calcularCosto(self, tablon, tiempo):
        if (tablon[0] - tablon[1]) >= tiempo:
            return tablon[0] - (tiempo + tablon[1])
        else:
            return tablon[2] * ((tiempo + tablon[1]) - tablon[0])

    # Función que calcula el costo total de riego de una finca.
    # list -> (int, list)
    def roV(self, fincaIngresada=None):
        if fincaIngresada == None:
            finca = self.finca.copy()
        else:
            finca = fincaIngresada.copy()

        # Se añade a cada tablon un índice que representa su posición en la finca.
        for i in range(len(finca)):
            finca[i] = (finca[i][0], finca[i][1], finca[i][2], i)

        riegoOptimo = []
        costoRiego = 0
        tiempo = 0
        n_tablones = self.n

        while n_tablones > 0:
            prioridades = []
            for i in range (n_tablones):
                prioridades.append(self.heuristica(finca[i]))

            indice_tablonOptimo = prioridades.index(min(prioridades))
            tablonOptimo = finca[indice_tablonOptimo]
            riegoOptimo.append(tablonOptimo[3])

            costoRiego += self.calcularCosto(tablonOptimo, tiempo)
            tiempo += tablonOptimo[1]

            finca.pop(indice_tablonOptimo)
            n_tablones -= 1

        return (costoRiego, riegoOptimo)