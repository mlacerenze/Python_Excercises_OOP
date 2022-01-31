"""Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si 
ha aprobado o no."""

class Alumn:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade
    
  def approve(self):
    if self.grade >= 7:
      return 'You are approved!'
    else:
      return 'You are fail.'
    
alumn = Alumn('Mark', 8)

print('Name:', alumn.name, '\nGrade:', alumn.grade , '\n', alumn.approve())