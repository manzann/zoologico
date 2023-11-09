# Herencia básica: Crear una clase base llamada "Animal" con atributos como "nombre"
#y "edad". Luego, crear dos subclases, "Perro" y "Gato", que hereden de la clase base
#"Animal" y agreguen atributos específicos para cada uno, como "raza" y "color".

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre, edad, peso, comida, raza, color,cuidador):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.comida = comida
        self.comida = raza
        self.comida = color
        self.cuidador = cuidador

    def saludar (self):
        print(f"Hola soy {self.nombre},el rey del Zoologico.")




## Método común: Agrega un método común llamado "hacer_sonido" a la clase base
#"Animal". Luego, implementa este método en las subclases "Perro" y "Gato" para que
#cada uno haga un sonido diferente cuando se llama.

    @abstractmethod
    def hacerSonido (self):
        pass

class Perro (Animal):
    def hacerSonido (self):
        print ("GUAU")

class Gato (Animal):
    def hacerSonido(self):
        print("miau")

potro = Perro ("potro",45,12,"De todo", "Golden", "Marron","Juan")
tokio = Gato ("tokio",45,12,"De todo", "Golden", "Marron","Juan")

print("hola soy el Perro y me llamo",{potro.nombre})
potro.hacerSonido()
print("hola soy el Gato y me llamo",{tokio.nombre})
tokio.hacerSonido()

#Polimorfismo: Crear una función que tome una lista de objetos "Animal" y llame al
#método "hacer_sonido" en cada uno de ellos. Esto demostrará el concepto de
#polimorfismo, ya que cada objeto "Animal" ejecutará su propia implementación del
#método "hacer_sonido".

animales = [potro, tokio]
