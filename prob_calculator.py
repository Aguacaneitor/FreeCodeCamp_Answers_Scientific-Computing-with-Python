import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    if kwargs:
      self.dictPelotas = kwargs
      self.contents = []
      for (k,v) in self.dictPelotas.items():
        for cantidad in range(0,v):
          self.contents.append(k) 

  def draw(self, number):
    salida = []
    cantidad_pelotas = len(self.contents)
    if number >= cantidad_pelotas: number = cantidad_pelotas
    for i in range(0,number):
      salida.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
    return salida

  def __str__(self):
    diccionario_temp = dict()
    for v in self.contents:
      diccionario_temp[v] = diccionario_temp.get(v,0)+1
    salida = "{"
    contador = len(diccionario_temp)
    for (k,v) in diccionario_temp.items():
      salida += '"'+k+'":'+str(v)
      contador -= 1
      if not (contador == 0):
        salida += ", "
    salida += "}"
    return salida

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  casos_acertados = 0
  for e in range(0, num_experiments):
    contenido_prueba = hat.contents[:]
    resultado = []
    acertado = True
    if num_balls_drawn >= len(contenido_prueba): num_balls_drawn = len(contenido_prueba)
    for i in range(0,num_balls_drawn):
      resultado.append(contenido_prueba.pop(random.randint(0,len(contenido_prueba)-1)))
    resultado_diccionario = dict()
    for v in resultado:
      resultado_diccionario[v] = resultado_diccionario.get(v,0)+1
    for (k,v) in expected_balls.items():
      if not (resultado_diccionario.get(k,0) >= v): 
        acertado = False
        break
    if acertado: casos_acertados += 1
  return casos_acertados/num_experiments

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)
expected = 0.272
print(expected)
print("---------------------------")


