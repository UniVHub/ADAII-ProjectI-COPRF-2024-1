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

def riegoOptimo(finca, tiempo = 0, memo = {}):
  # type: (list[tuple[int, int, int]], int, dict) -> tuple[int, list[tuple[int, int, int]]]

  if (len(finca) == 1):
    tablon = finca[0] # Obtener el tablon
    costo = evaluarCosto(tablon, tiempo) # Evaluar el tablon con el tiempo
    return (costo, [tablon]) # Devolver el costo y el tablon
  
  else:
    costoF = float('inf')
    ordenF = []
    ordenesCandidatos = []

    for i, tablon in enumerate(finca):
      fincaRestante = finca[:] # Se crea una copia de finca
      fincaRestante.pop(i) # Se elimina el tablon iterando

      costoTablon = evaluarCosto(tablon, tiempo) # Se calcula el costo del tbln

      # Se realiza recursión con la finca restante (Sumando el tiempo de regado)
      if ((tuple(fincaRestante), tiempo) in memo):
        costo, orden = memo[(tuple(fincaRestante), tiempo)]
      else:
        costo, orden = riegoOptimo(fincaRestante, tiempo + tablon[1], memo)

      memo[(tuple(fincaRestante), tiempo)] = (costo, orden)
      # Se actualiza el costo y el orden ya que no tienen el tablon restante
      costo += costoTablon
      orden = [tablon] + orden

      # Se añade el orden candidato
      ordenesCandidatos.append((costo, orden))

    # Se evalua cual es el orden que consume menos
    for orden in ordenesCandidatos:
      if (orden[0] < costoF): # Si el costo del orden es menor al que se tiene
        costoF = orden[0]
        ordenF = orden[1]

      # De resto, no se hace nada
        
  # Retornar el orden y costo final
  return (costoF, ordenF)

finca = [(13,2,4),(15,9,2),(12,10,3),(13,22,3),(15,9,2),(11,11,2),(10,13,4),(27,14,4),(12,8,3),(23,7,1),(16,9,3), (27,21,4)]
print(riegoOptimo(finca))
