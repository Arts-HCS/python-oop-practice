# Diseñar un sistema de clases para diferentes tipos de vehículos, asegurando que cada tipo implemente su propio comportamiento.

class Vehiculo:
    instancias = []
    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        
        Vehiculo.instancias.append(self)
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self._marca}', '{self._modelo}', {self._anio})"


v1 = Vehiculo("Volvo","XC60",2010)
v2 = Vehiculo("Tesla","Modelo S",2014)
v3 = Vehiculo("Buick","Envision",2020)


print(Vehiculo.instancias)