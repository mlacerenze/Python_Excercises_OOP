"""
Realizar un programa que tenga una clase Persona con las siguientes características. La clase 
tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar 
los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age 
    
  def show_info(self):
    print(f'Name: {self.name} \nAge: {self.age}')
    
  def adult(self):
    if self.age >= 18:
      print('You`re a adult!')
    else:
      print('You`re a baby')
      
person = Person('Mark', 17)

person.show_info()
person.adult()