from ListaSimple import ListaSimple

class Sensor:
    def __init__(self, id_Sensor, nombre):
        self.id = id_Sensor
        self.nombre = nombre
        self.frecuencias = ListaSimple()