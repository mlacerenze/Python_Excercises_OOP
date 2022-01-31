"""
Crear un programa con tres clases Universidad, con atributos nombre 
(Donde se almacena el nombre de la Universidad). Otra llamada Carerra, 
con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
El programa debe imprimir la especialidad, edad, nombre y universidad de dicho 
estudiante con un objeto llamado persona.
"""

class University:
  def __init__(self, university_name):
    self.university_name = university_name
    
class Career:
  def __init__(self, specialty):
    self.specialty = specialty
    
class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show_info(self):
    # Aquí uso pasaje por referencia para que el objeto que se crea en el
    print(f'{self.name} is {self.age} years old and studies {self.specialty} at {self.university_name}')
    
person = Student('Mark', 20)
person.university_name = 'Harvard'
person.specialty = 'Computer Science'
person.show_info()

