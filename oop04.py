"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los 
resultados obtenidos. Llamar a la clase Calculadora.
"""

class Calculator:
  def __init__(self, n1, n2):
    self.n1 = n1
    self.n2 = n2 
    
  def add(self):
    return self.n1 + self.n2
  
  def substract(self):
    return self.n1 - self.n2
  
  def multiply(self):
    return self.n1 * self.n2
  
  def divide(self):
    return self.n1 / self.n2
  
calculator = Calculator(5, 2)
print(calculator.add())
print(calculator.substract())
print(calculator.multiply())
print(calculator.divide())