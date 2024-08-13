from abc import ABC,abstractmethod
class Animal (ABC):

    @property
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):

    def __init__(self):
        self.nombre="firulais"
        

    def sonido(self):
        return(f"{self.nombre} hace giuau")

perro=Perro()
print(perro.sonido())