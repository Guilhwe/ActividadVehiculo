from vehiculo.vehiculo_item import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca,modelo)
        self.tipo = tipo
    def __str__(self):
        return '{:<25} | {:<25} | {:<25}'.format(self.marca, self.modelo, self.tipo)