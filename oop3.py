"""
Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para 
inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es 
equilátero, isósceles o escaleno).
"""

class Triangle:
  def initialize(self):
    self.side1 = int(input('Enter a first value: '))
    self.side2 = int(input('Enter a second value: '))
    self.side3 = int(input('Enter a third value: '))
    
  def show_info(self):
    print('-- TRIANGLE INFO --')
    print(f'Side 1: {self.side1} \nSide 2: {self.side2} \nSide 3: {self.side3}')
    
  def major(self):
    print('The major side is: ')
    if self.side1 > self.side2 and self.side1 > self.side3:
      print(f'Side 1: {self.side1}')
    elif self.side2 > self.side3:
      print(f'Side 2: {self.side2}')
    else:
      print(f'Side 3: {self.side3}')
      
  """
  Triangle type:
    - equilatero: todos los lados son iguales
    - isoceles: dos lados iguales
    - escaleno: todos los lados desiguales
  """
  def type(self):
    if self.side1 == self.side2 and self.side1 == self.side3:
      print('The triangle is equilateral. All the sides are equals.')
    elif self.side1 != self.side2 and self.side1 != self.side3:
      print('The triangle is isosceles. Only two sides are equals.')
    else:
      print('The triangle is scalene. All the sides are unequal.')

triangle = Triangle()
triangle.initialize()
triangle.show_info()
triangle.major()
triangle.type()
      