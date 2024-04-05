class ProgramacionDinamica:
    # type: (tuple[int, int, int], int) -> int

    """
    Clase que implementa el algoritmo de programación dinámica para calcular el 
    orden óptimo de riego de los tablones en una finca.

    Args:
      finca (list): Lista de tablones de la finca. Cada tablón es una lista de tres elementos: tiempo de riego (tr), tiempo de supervivencia (ts) y prioridad (p).

    Attributes:
      finca (list): Lista de tablones de la finca.
      n (int): Número de tablones en la finca.

    Methods:
      evaluarCosto(tablon, ti): Calcula el costo de regar un tablón en un tiempo dado.
      calcular(finca=None, tiempo=0, memo={}): Calcula el orden óptimo de riego de los tablones en la finca.
      roPD(): Devuelve los índices de los tablones en el orden en que se deben regar según la solución óptima.
    """

    def __init__(self, finca):
        self.finca = finca
        self.n = len(finca)

    def evaluarCosto(self, tablon, ti):
        """
        Calcula el costo de regar un tablón en un tiempo dado.

        Args:
          tablon (list): Lista que representa un tablón de la finca. Contiene tres elementos: tiempo de riego (tr), tiempo de supervivencia (ts) y prioridad (p).
          ti (int): Tiempo en el que se desea regar el tablón.

        Returns:
          float: El costo de regar el tablón en el tiempo dado.
        """
        ts = tablon[0]
        tr = tablon[1]
        p = tablon[2]

        if ts - tr >= ti:
            return ts - (ti + tr)

        return p * ((ti + tr) - ts)
    
    def calcularTiempo(self, finca):
      """
      Calcula el tiempo tomado en regar una determinada finca.

      Args:
        finca (list): Lista que contiene varios tablones.

      Returns:
        float: El costo de regar el tablón en el tiempo dado.
      """
      tiempo = 0

      for tablon in finca:
        tiempo += tablon[1]

      return tiempo

    def calcular(self, finca=None, memo={}):
        # type: (list[tuple[int, int, int]], dict) -> tuple[int, list[tuple[int, int, int]]]

        """
        Calcula el orden óptimo de riego de los tablones en la finca.

        Args:
          finca (list, optional): Lista de tablones de la finca. Si no se proporciona, se utiliza la finca almacenada en el atributo `finca` de la clase. Default es None.
          memo (dict, optional): Diccionario para almacenar resultados ya calculados. Default es {}.

        Returns:
          tuple: Una tupla que contiene el costo total de riego y la lista de tablones en el orden óptimo de riego.
        """
        if finca is None:
            finca = self.finca

        if (len(finca) == 0):
           return (0, [])
        
        else:
          costoF = float('inf')
          ordenF = []
          ordenesCandidatos = []

          for i in range (len(finca) - 1, -1, -1):
            fincaRestante = finca[:]
            tablon = fincaRestante.pop(i)[:]
            tiempoR = self.calcularTiempo(fincaRestante)

            costoTablon = self.evaluarCosto(tablon, tiempoR)

            if ((tuple(fincaRestante)) in memo):
              costo, orden = memo[(tuple(fincaRestante))]
            else:
              costo, orden = self.calcular(fincaRestante, memo)

            memo[tuple(fincaRestante)] = (costo, orden)

            costo += costoTablon
            orden = orden + [tablon]

            ordenesCandidatos.append((costo, orden))

          for orden in ordenesCandidatos:
            if (orden[0] < costoF):
              costoF = orden[0]
              ordenF = orden[1]
              
        return (costoF, ordenF)

    def roPD(self):
        """
        Devuelve los índices de los tablones en el orden en que se deben regar según la solución óptima
        a partir del resultado obtenido de la función "Calcular"

        Returns:
          list: Lista de índices de los tablones en el orden óptimo de riego.
        """
        finca = self.finca[:]
        resultado = self.calcular()
        indices = []

        indices.append(resultado[0])

        for tablon in resultado[1]:
          indice = finca.index(tablon)
          indices.append(indice)
          finca[indice] = None

        return indices


finca = [
    (13, 2, 4),
    (15, 9, 2),
    (12, 10, 3),
    (13, 22, 3),
    (15, 9, 2),
    (11, 11, 2),
    (10, 13, 4),
    (27, 14, 4),
    (12, 8, 3),
    (23, 7, 1),
    (16, 9, 3),
    (27, 21, 4),
]

