from CampoAgricola import Campo
from Frecuencia import FrecuenciaLinea
from ListaSimple import ListaSimple
from matriz import matriz
from EstacionesBase import EstacionBase
from Sensores import Sensor
from xml.dom.minidom import parse

class SistemaAgricola:
    def __init__(self):
        self.campos = ListaSimple()
    
    def Cargar_Archivo(self, ruta):
        # Carga los datos desde un arch
        # ivo XML
        try:
            dom = parse(ruta)
            campos_XML = dom.getElementsByTagName('campo')
            
            for campo_XML in campos_XML: 
                # Crea el campo
                IDcampo = campo_XML.getAttribute('id')
                nombre_campo = campo_XML.getAttribute('nombre')
                campo = Campo(IDcampo, nombre_campo)
                
                print(f"Cargando campo agricola {IDcampo}")
                
                # Cargar estaciones base
                estaciones_xml = campo_XML.getElementsByTagName('estacion')
                for estacion_xml in estaciones_xml:
                    IDestacion = estacion_xml.getAttribute('id')
                    nombre_estacion = estacion_xml.getAttribute('nombre')
                    estacion = EstacionBase(IDestacion, nombre_estacion)
                    campo.estacionesBase.insertar(estacion)
                    print(f"Creando estacion base {IDestacion}")
                
                # Cargar sensores de suelo
                sensores_suelo_xml = campo_XML.getElementsByTagName('sensorS')
                for sensor_xml in sensores_suelo_xml:
                    IDsensor = sensor_xml.getAttribute('id')
                    nombre_sensor = sensor_xml.getAttribute('nombre')
                    sensor = Sensor(IDsensor, nombre_sensor)
                    
                    # Cargar frecuencias
                    frecuencias_xml = sensor_xml.getElementsByTagName('frecuencia')
                    for freq_xml in frecuencias_xml:
                        id_estacion = freq_xml.getAttribute('idEstacion')
                        valor = freq_xml.firstChild.data
                        frecuencia = FrecuenciaLinea(id_estacion, valor)
                        sensor.frecuencias.insertar(frecuencia)
                    
                    campo.sensores_suelo.insertar(sensor)
                    print(f"Creando sensor de suelo {IDsensor}")
                
                # Cargar sensores de cultivo
                sensores_cultivo_xml = campo_XML.getElementsByTagName('sensorTierra')
                for sensor_xml in sensores_cultivo_xml:
                    IDsensor = sensor_xml.getAttribute('id')
                    nombre_sensor = sensor_xml.getAttribute('nombre')
                    sensor = Sensor(IDsensor, nombre_sensor)
                    
                    # Cargar frecuencias
                    frecuencias_xml = sensor_xml.getElementsByTagName('frecuencia')
                    for freq_xml in frecuencias_xml:
                        id_estacion = freq_xml.getAttribute('idEstacion')
                        valor = freq_xml.firstChild.data
                        frecuencia = FrecuenciaLinea(id_estacion, valor)
                        sensor.frecuencias.insertar(frecuencia)
                    
                    campo.sensoresCultivo.insertar(sensor)
                    print(f"Creando sensor de cultivo {IDsensor}")
                
                # Crear matrices y agregar campo
                campo.crear_matrices()
                self.campos.agregar(campo)
                
            print("Archivo se cargó exitosamente")
            
        except Exception as e:
            print(f"Ocurrio un error al cargar archivo: {e}")
    
    def listar_campos(self):
        # Muestra la lista de campos disponibles
        print("\nCampos Disponibles:")
        print("-" * 25)
        actual = self.campos.primero
        while actual:
            campo = actual.dato
            print(f"ID: {campo.id} - {campo.nombre}")
            actual = actual.siguiente
    
    def mostrar_campo(self, id_campo):
        # Muestra las matrices de un campo especifico
        actual = self.campos.primero
        while actual:
            campo = actual.dato
            if campo.id == id_campo:
                campo.mostrar_matrices()
                return
            actual = actual.siguiente
        print(f"Campo {id_campo} no encontrado")