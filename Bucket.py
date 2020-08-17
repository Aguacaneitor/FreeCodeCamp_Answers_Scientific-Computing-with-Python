class Category:

  def __init__(self, categoria):
    self.categoria = categoria
    self.ledger = []

  def check_funds(self,amount):
    fondos = [k["amount"] for k in self.ledger]
    dinero = sum(fondos)
    if (dinero - amount)>= 0:
      return True
    else:
      return False 

  def deposit(self,amount, description=""):
    deposito = {"amount": amount, "description": description}
    self.ledger.append(deposito)

  def withdraw(self,amount, description=""):
    if (self.check_funds(amount))> 0:
      retiro = {"amount": -amount, "description": description}
      self.ledger.append(retiro)
      return True
    else:
      return False

  def get_balance(self):
    fondos = [k["amount"] for k in self.ledger]
    dinero = sum(fondos)
    return dinero

  def transfer(self,amount, category):
    if (self.check_funds(amount))> 0:
      retiro = {"amount": -amount, "description": "Transfer to "+category.categoria}
      self.ledger.append(retiro)
      category.deposit(amount,"Transfer from "+self.categoria)
      return True
    else:
      return False

  def __repr__(self):
    total = 0
    largo_categoria = len(self.categoria)
    inicio_titulo = 15 - (largo_categoria //2)
    salida = ("*"*inicio_titulo) + self.categoria + ("*"*(30-inicio_titulo-largo_categoria)) + "\n"
    for transaccion in self.ledger:
      identificador = transaccion["description"]
      largo_identificador = len(identificador)
      if largo_identificador > 23:
        salida += identificador[0:23]
        largo_identificador = 23
      else:
        salida += identificador
      total += transaccion["amount"]
      longitud_de_cantidad = str("%.2f" % transaccion["amount"])
      espaciado = (" "*(23-largo_identificador)) + (" "*(7 - len(longitud_de_cantidad)))
      salida += espaciado + longitud_de_cantidad + "\n"
    salida +="Total: " + str("%.2f" % total)
    return salida

  def __str__(self):
    total = 0
    largo_categoria = len(self.categoria)
    inicio_titulo = 15 - (largo_categoria //2)
    salida = ("*"*inicio_titulo) + self.categoria + ("*"*(30-inicio_titulo-largo_categoria)) + "\n"
    for transaccion in self.ledger:
      identificador = transaccion["description"]
      largo_identificador = len(identificador)
      if largo_identificador > 23:
        salida += identificador[0:23]
        largo_identificador = 23
      else:
        salida += identificador
      total += transaccion["amount"]
      longitud_de_cantidad = str("%.2f" % transaccion["amount"])
      espaciado = (" "*(23-largo_identificador)) + (" "*(7 - len(longitud_de_cantidad)))
      salida += espaciado + longitud_de_cantidad + "\n"
    salida +="Total: " + str("%.2f" % total)
    return salida

  


def create_spend_chart(categories):
  salida = "Percentage spent by category\n"
  mayor_longitud = None
  gastos_totales = 0
  categorias_desordenadas = []
  #Recorro todos los objetos recibidos para obtener y poder ordenar los elementos
  for k in categories:
    fondos = sum(list(filter(lambda x: x >0,[J["amount"] for J in k.ledger])))
    gastos = sum(list(filter(lambda x: x <0,[J["amount"] for J in k.ledger])))
    if mayor_longitud is None or mayor_longitud < len(k.categoria):
      mayor_longitud = len(k.categoria)
    gastos_totales += gastos
    categorias_desordenadas.append({"nombre": k.categoria,"fondos": fondos, "porcentaje_gastos": gastos})
  for k in range(0,len(categorias_desordenadas)):
    categorias_desordenadas[k]["porcentaje_gastos"] = (categorias_desordenadas[k]["porcentaje_gastos"]/gastos_totales)*(100)
  contador = 100
  indice_nombres = 0
  while True:
    if contador >=0:
      salida += (" "*(3-len(str(contador)))) + str(contador) + "|"
      for k in range(0,len(categorias_desordenadas)):
        salida += " "
        if not (k == 0): salida += " "
        if (categorias_desordenadas[k]["porcentaje_gastos"] >= contador): salida += "o"
        else: salida += " "
      salida += "  \n"
    if contador == 0: salida += (" "*4)+("-"*10) +"\n"    
    if contador < 0: 
      salida += " "*4
      for k in range(0,len(categorias_desordenadas)):
        salida += " "
        if not (k == 0): salida += " "
        nombre = categorias_desordenadas[k]["nombre"]
        if len(nombre) > indice_nombres: salida += nombre[indice_nombres:(indice_nombres+1)]
        else: salida += " "
        #else: salida += " "
      indice_nombres += 1      
      if indice_nombres >= mayor_longitud: 
        salida += "  "
        break
      else: salida += "  \n"
    contador -= 10
  return salida

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])
expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
if actual == expected: print("bien")
else: 
  print("mal")
  print(actual)
  print("----------------------------------------------")
  print(expected)

