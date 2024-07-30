class Vehiculo:
    def __init__(self, marca, modelo, ligado = False):
        self.marca = marca
        self.modelo = modelo
        self._ligado =ligado
    
    def __str__(self):
        return (f'{self.marca} | {self.modelo} | {self._ligado}')
    
    