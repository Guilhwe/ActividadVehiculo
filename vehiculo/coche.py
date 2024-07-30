from vehiculo.vehiculo_item import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas=0 ):
        super().__init__(marca,modelo)
        self.puertas = puertas

    def __str__(self):
        
       return 'vehiculo {:<25} | modelo {:<25} | puertas {:<25}'.format(self.marca, self.modelo, self.puertas)