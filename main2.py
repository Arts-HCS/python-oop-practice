#Vas a crear un sistema para gestionar diferentes tipos de vehículos. Cada vehículo tiene ciertas características básicas, pero algunos tienen particularidades adicionales.

#Nota: después de usar la función super para agregar los atributos de la clase padre, es necesario inicialiar los nuevos atributos que se quieren usar como si fuera en la clase padre, es decir, con self. 
class Vehiculo:
    def __init__(self, marca:str, modelo:str, anio:int, kilometraje:float):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio 
        self.kilometraje = kilometraje
    
    def descripcion(self):
        return f"Este vehículo es de marca {self.marca}, modelo {self.modelo}, del año {self.anio} y cuenta con {self.kilometraje} km"
    
    def conducir(self, km):
        self.kilometraje += km
        return f"El vehículo ha recorrido {km} kilómetros y ahora su kilometraje total es de {self.kilometraje} km"
    
    @staticmethod
    def es_vehiculo_antiguo(ann):
        return ann > 20
    
    @classmethod
    def crear_desde_cadena(cls, cadena):
        marca, modelo, anio, kilometraje = cadena.replace(" ","").split(",")
        return cls(marca, modelo, int(anio), float(kilometraje))
    
    def __str__(self):
        return f"Vehiculo: Marca:{self.marca}, Modelo:{self.modelo}, Año: {self.anio}, Kilometraje: {self.kilometraje}"
    

class Automovil(Vehiculo):
    def __init__(self, marca:str, modelo:str, anio:int, kilometraje:float, puertas:int):
        super().__init__(
            marca, modelo, anio, kilometraje
        )
        self.puertas = puertas
    def descripcion(self):
        return super().descripcion() + f" y tiene {self.puertas} puertas"
        
class Motocicleta(Vehiculo):
    def __init__(self, marca:str, modelo:str, anio:int, kilometraje:float, tipo:str):
        super().__init__(
            marca, modelo, anio, kilometraje
        )
        self.tipo = tipo
    def descripcion(self):
        return super().descripcion()+ f" y es de tipo {self.tipo}"
    
class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, kilometraje, capacidad_carga:float):
        super().__init__(marca, modelo, anio, kilometraje)
        self.capacidad_carga = capacidad_carga
    
    def conducir(self, km):
        return super().conducir(km)
    
obj1 = Vehiculo("Volvo","XC30",2010, 50)

print(obj1.crear_desde_cadena("Mazda, modelo1,1990, 100"))