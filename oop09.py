"""
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos 
clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la 
cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada 
clase y mostrar por pantalla los atributos de cada uno
"""

class Factory:
  def __init__(self, tires, color, price):
    self.tires = tires
    self.color = color
    self.price = price 
    
class Motorcycle(Factory):
  def __init__(self, tires, color, price):
    super().__init__(tires, color, price)
    
  def show_tires(self):
    print(f"This motorcycle has {self.tires} tires")
    
  def show_color(self):
    print(f"This motorcycle is {self.color}")
    
  def show_price(self):
    print(f"This motorcycle costs {self.price}")
    
class Car(Factory):
  def __init__(self, tires, color, price):
    super().__init__(tires, color, price)
  
  def show_tires(self):
    print(f'This car has {self.tires} tires')
    
  def show_color(self):
    print(f'This car is {self.color}')
    
  def show_price(self):
    print(f'This car costs {self.price}')
    
motorcycle = Motorcycle(2, 'red', '$100')
car = Car(4, 'black', '$200')

motorcycle.show_tires()
motorcycle.show_color()
motorcycle.show_price()
print('\n')
car.show_tires()
car.show_color()
car.show_price()