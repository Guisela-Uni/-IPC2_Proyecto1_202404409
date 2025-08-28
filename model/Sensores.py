from ListaSimple import ListaSimple

class Sensor:
    def __init__(self, IDsensor, nombreSensor):
        self.id = IDsensor
        self.nombreSensor = nombreSensor
        self.frecuencia = ListaSimple()