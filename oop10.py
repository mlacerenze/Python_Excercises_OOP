"""
Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un 
mensaje que diga "Hola...". Luego, crear una clase Pulpo() que herede Marino, pero 
modificar el mensaje de hablar por "Soy un Pulpo". Por ultimo, crear una clase Foca(), 
heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese 
mesjae como parametro
"""

class SeaAnimal:
  def talk(self):
    print("Hello...")
    
class Octopus(SeaAnimal):
  def talk(self):
    print("I`m a octopus!")
    
class Seal(SeaAnimal):
  def talk(self, message):
    self.message = message
    print(self.message)
    
octopus = Octopus()
octopus.talk()

seal = Seal()
seal.talk("I`m a seal!")