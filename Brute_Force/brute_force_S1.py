def riegoOptimo(finca, i, j):
  # type: (list[tuple], int, int) -> tuple[int, list[tuple]]

  """
  Dada una finca con 'n' tablones, calcula el plan de riego óptimo tal que
  la sumatoria de costos de riegos del plan sea mínima.

  Parámetros
  ----------
  finca : list[tuple]
    Lista de tablones donde cada tablón es una tupla de tres enteros que: 
    contienen la información del tablon: (Supervivencia, Regado, Prioridad).

  i : int
    Indice inicial

  j : int
    Indice final

  Retorna
  -------
  Tuple[int, list[tuple[int, int, int]]]
    Tupla que contine el costo mínimo y la lista de tablones correspondiente que
    obedecen al plan de riego.
  """

  def evaluarCosto(tablon, ti):
    # type: (tuple[int, int, int], int) -> int

    """
    Calcula el costo de regar un tablón en un determinado tiempo
    """

    ts = tablon[0]
    tr = tablon[1]
    p = tablon[2]

    if (ts - tr >= ti):
      return ts - (ti + tr)

    return p * ((ti + tr) - ts)

  if (i == j):
    costo = 0
    tiempo = 0

    for tablon in finca:
      costo += evaluarCosto(tablon, tiempo)
      tiempo += tablon[1]

    return (costo, finca[:])

  else:
    costo = float('inf')
    nuevaFinca = []

    # Aquí se realizan las permutaciones
    for k in range(i, j):
      finca[i], finca[k] = finca[k], finca[i] 
      elementos = riegoOptimo(finca, i+1, j)
      finca[i], finca[k] = finca[k], finca[i]
      
      # Si el costo de la permutación es menor a la encontrada, guardar
      # el plan de riego
      if elementos[0] < costo:
        costo = elementos[0]
        nuevaFinca = elementos[1]

    return (costo, nuevaFinca)

finca = [(10,3,4), (2,2,1), (5,3,3), (8,1,1), (6,4,2)]
n = len(finca)

print(riegoOptimo(finca, 0, n))