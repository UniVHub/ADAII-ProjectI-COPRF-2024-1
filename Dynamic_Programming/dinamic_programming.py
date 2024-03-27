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
      calcularResultadoOptimo(): Devuelve los índices de los tablones en el orden en que se deben regar según la solución óptima.
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

        if (len(finca) == 1):
          tablon = finca[0] # Obtener el tablon
          costo = self.evaluarCosto(tablon, 0) # Evaluar el tablon con el tiempo
          return (costo, [tablon]) # Devolver el costo y el tablon
        
        else:
          costoF = float('inf')
          ordenF = []
          ordenesCandidatos = []

          for i in range (len(finca) - 1, -1, -1):
            fincaRestante = finca[:] # Se crea una copia de finca
            tablon = fincaRestante.pop(i)[:] # Se elimina y guarda el tablon iterado
            tiempoR = self.calcularTiempo(fincaRestante)

            costoTablon = self.evaluarCosto(tablon, tiempoR) # Se calcula el costo del tbln

            # Se realiza recursión con la finca restante
            if ((tuple(fincaRestante)) in memo):
              costo, orden = memo[(tuple(fincaRestante))]
            else:
              costo, orden = self.calcular(fincaRestante, memo)

            memo[tuple(fincaRestante)] = (costo, orden)

            # Se actualiza el costo y el orden ya que no tienen el tablon restante
            costo += costoTablon
            orden = orden + [tablon]

            # Se añade el orden candidato
            ordenesCandidatos.append((costo, orden))

          # Se evalua cual es el orden que consume menos
          for orden in ordenesCandidatos:
            if (orden[0] < costoF): # Si el costo del orden es menor al que se tiene
              costoF = orden[0]
              ordenF = orden[1]
              
        # Retornar el orden y costo final
        return (costoF, ordenF)

    def calcularResultadoOptimo(self):
        """
        Devuelve los índices de los tablones en el orden en que se deben regar según la solución óptima.

        Returns:
          list: Lista de índices de los tablones en el orden óptimo de riego.
        """
        resultado = self.calcular()
        indices = []

        indices.append(resultado[0])

        for tablon in resultado[1]:
            indices.append(self.finca.index(tablon))

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

