"""
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. Definir los 
atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. La clase CajaAhorro tendrá un 
método para heredar los datos y uno para mostrar la información.

La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método para obtener el importe del i
nterés (cantidad*interés/100) y otro método para mostrar la información, datos del titular plazo, interés y total de interés.

Crear al menos un objeto de cada subclase.
"""

class Account:
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount
    
  def show_info(self):
    print(f'{self.name} has {self.amount}')

class FixedTerm(Account):
  def __init__(self, name, amount, plazo, interest):
    super().__init__(name, amount)
    self.plazo = plazo
    self.interest = interest
    
  def get_interest(self):
    return self.amount * self.interest / 100
  
  def show_info(self):
    super().show_info()
    print(f'Plazo: {self.plazo}')
    print(f'Interest: {self.interest}')
    print(f'Interest amount: {self.get_interest()}') 

class SavingsBank(Account):
  def __init__(self, name, amount, interest):
    super().__init__(name, amount)
    self.interest = interest
    
  # def get_interest(self):
  #   return self.amount * self.interest / 100
  
  def show_info(self):
    super().show_info()
    print(f'Interest: {self.interest}')
    # print(f'Interest amount: {self.get_interest()}')
    
account1 = FixedTerm('Mark', 1000, 10, 5)
account1.show_info()

account2 = SavingsBank('John', 1000, 10)
account2.show_info()