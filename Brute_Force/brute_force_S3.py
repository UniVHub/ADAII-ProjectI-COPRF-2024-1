def evaluarCosto(tablon, ti = 0):
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


def calcularTiempo(finca):
  tiempo = 0

  for tablon in finca:
    tiempo += tablon[1]

  return tiempo


def riegoOptimo(finca):
  # type: (list[tuple[int, int, int]]) -> tuple[int, list[tuple[int, int, int]]]

  if (len(finca) == 1):
    tablon = finca[0] # Obtener el tablon
    costo = evaluarCosto(tablon, 0) # Evaluar el tablon con el tiempo
    return (costo, [tablon]) # Devolver el costo y el tablon
  
  else:
    costoF = float('inf')
    ordenF = []
    ordenesCandidatos = []

    for i in range (len(finca) - 1, -1, -1):
      fincaRestante = finca[:] # Se crea una copia de finca
      tablon = fincaRestante.pop(i)[:] # Se elimina y guarda el tablon iterado
      tiempoR = calcularTiempo(fincaRestante)

      costoTablon = evaluarCosto(tablon, tiempoR) # Se calcula el costo del tbln

      # Se realiza recursión con la finca restante
      # No hay necesidad de sumar tiempo ya que se hace recursión de atras hacia
      # adelante, por lo que el tiempo inicial es 0
      costo, orden = riegoOptimo(fincaRestante)

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

finca = [(10,3,4), (2,2,1), (5,3,3), (8,1,1), (6,4,2)]
print(riegoOptimo(finca))