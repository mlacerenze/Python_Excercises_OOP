"""
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día 
calcular la cantidad de dinero que se ha depositado.

Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y 
los métodos __init__, depositar, extraer, mostrar_total.

La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.
"""

class Client:
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount 
    
  def deposit(self):
    amount_money = int(input(f'Hello, {self.name}. Enter money to deposit: '))
    self.amount = self.amount + amount_money 
    return('Your money has been deposited with exit!')
  
  def extract(self):
    extract_money = int(input('Enter money to extract: '))
    if extract_money > self.amount:
      return('You do not have enough money to extract!')
    else:
      self.amount = self.amount - extract_money
  
  def show_total(self):
    return('{}, your total is: {}'.format(self.name, self.amount))
  
  
mark = Client('Mark', 0)
print(mark.deposit())
print(mark.show_total())
print(mark.extract())
print(mark.show_total())
