class FuerzaBruta:
    # type: (list[tuple], int, int) -> tuple[int, list[tuple]]
    """
    Clase que implementa el algoritmo de Fuerza Bruta para resolver el problema de riego de tablones de una finca.
    
    Args:
      finca (list): Una lista de tablones de la finca. Cada tablón es una tupla de tres elementos: tiempo de supervivencia (ts), tiempo de riego (tr) y prioridad (p).
      
    Attributes:
      finca (list): Lista de tablones de la finca.
      n (int): Número de tablones en la finca.
      
    Methods:
      evaluarCosto(tablon, ti): Evalúa el costo de riego de un tablón en un tiempo dado.
      calcular(i, j): Calcula el costo mínimo de riego y el orden óptimo de riego de los tablones en el rango [i, j).
      roFB(): Devuelve los índices de los tablones en el orden en que se deben regar según la solución óptima.
    """
    
    def __init__(self, finca):
        self.finca = finca
        self.n = len(finca)

    def evaluarCosto(self, tablon, ti):
        # type: (tuple[int, int, int], int) -> int

        """
        Evalúa el costo de riego de un tablón en un tiempo dado.

        Args:
        - tablon (tuple): Una tupla que representa un tablón de la finca.
          - tr (int): Tiempo de riego.
          - ts (int): Tiempo de supervivencia.
          - p (int): Prioridad.
        - ti (int): Tiempo actual.

        Returns:
        - int: El costo de riego del tablón en el tiempo dado.
        """
        ts = tablon[0]
        tr = tablon[1]
        p = tablon[2]

        if ts - tr >= ti:
            return ts - (ti + tr)

        return p * ((ti + tr) - ts)

    def calcular(self, i, j):
        """
        Calcula el costo mínimo de riego y el orden óptimo de riego de los tablones en el rango [i, j).

        Args:
        - i (int): Indice inicial del rango.
        - j (int): Indice final del rango.

        Returns:
        - tuple: Una tupla que contiene el costo mínimo de riego y una lista con el orden óptimo de riego de los tablones.
        """
        if i == j:
            costo = 0
            tiempo = 0

            for tablon in self.finca:
                costo += self.evaluarCosto(tablon, tiempo)
                tiempo += tablon[1]

            return (costo, self.finca[:])

        else:
            costo = float("inf")
            nuevaFinca = []

            # Aquí se realizan las permutaciones
            for k in range(i, j):
                self.finca[i], self.finca[k] = self.finca[k], self.finca[i]
                elementos = self.calcular(i + 1, j)
                self.finca[i], self.finca[k] = self.finca[k], self.finca[i]

                # Si el costo de la permutación es menor a la encontrada, guardar el plan de riego
                if elementos[0] < costo:
                    costo = elementos[0]
                    nuevaFinca = elementos[1]

            return (costo, nuevaFinca)

    def roFB(self):
        """
        Devuelve los índices de los tablones en el orden en que se deben regar según la solución óptima.
        a partir del resultado obtenido de la función "Calcular"

        Returns:
        - list: Una lista de índices que representa el orden óptimo de riego de los tablones, 
        cuyo primer elemento es el costo total del riego y los siguientes son los índices de los tablones 
        en el orden en que se deben regar.
        """
        finca = self.finca[:]
        resultado = self.calcular(0, self.n)
        indices = []

        indices.append(resultado[0])

        for tablon in resultado[1]:
            indice = finca.index(tablon)
            indices.append(indice)
            finca[indice] = None

        return indices



