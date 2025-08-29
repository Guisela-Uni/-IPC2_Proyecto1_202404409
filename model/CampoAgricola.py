from ListaSimple import ListaSimple
from matriz import matriz

class Campo:
    def __init__(self, IDcampo, NombreCampo):
        self.id = IDcampo
        self.nombre = NombreCampo
        self.estacionesBase = ListaSimple() 
        self.sensoresSuelo = ListaSimple()
        self.sensoresCultivo = ListaSimple()
        self.matrizSuelo = None
        self.matrizCultivo = None
    
    def crear_matrices(self):
        # Crea y llena las matrices de frecuencias
        n_estaciones = self.estacionesBase.tamano
        n_sensoresSuelo = self.sensoresSuelo.tamano
        n_sensoresCultivo = self.sensoresCultivo.tamano
        
        # Creando matrices
        self.matriz_suelo = matriz(n_estaciones, n_sensoresSuelo) #recibe por parametro las estaciones y los sensores de suelo
        self.matriz_cultivo = matriz(n_estaciones, n_sensoresCultivo) #recibe por parametro las estaciones y sensores de cultivo
        
        # Llenando matriz de SUELO F[n,s] nxs
        for n_columna in range(n_sensoresSuelo):
            sensor = self.sensoresSuelo.obtener(n_columna)
            frecuenciaActual = sensor.frecuencias.primero
            while frecuenciaActual:
                frecuencia = frecuenciaActual.dato
                n_fila = self.estaciones.buscar(frecuencia.id_estacion)
                if n_fila != -1:
                    self.matriz_suelo.establecer(n_fila, n_columna, frecuencia)
                frecuenciaActual = frecuenciaActual.siguiente
        
        # Llenando matriz de CULTIVO F[n,t] nx1
        for n_columna in range(n_sensoresCultivo):
            sensor = self.sensoresCultivo.obtener(n_columna)
            frecuenciaActual = sensor.frecuencias.primero
            while frecuenciaActual:
                frecuencia = frecuenciaActual.dato
                n_fila = self.estaciones.buscar(frecuencia.id_estacion)
                if n_fila != -1:
                    self.matriz_cultivo.establecer(n_fila, n_columna, frecuencia)
                frecuenciaActual = frecuenciaActual.siguiente
    
    def mostrar_matrices(self):
        if self.matriz_suelo:
            titulo_suelo = f"Matriz de Suelo ID:  {self.id}"
            self.matriz_suelo.mostrar(titulo_suelo, self.estacionesBase, self.sensoresSuelo)
        
        if self.matriz_cultivo:
            titulo_cultivo = f"Matriz de Cultivo - ID:  {self.id}"
            self.matriz_cultivo.mostrar(titulo_cultivo, self.estacionesBase, self.sensoresCultivo)

    def visualizar_matrices_graphviz(self):
        #Genera visualizaciones de matriz suelo y matriz cultivo
        if self.matriz_suelo:
            print("Generando visualización de matriz de suelo...")
            self.matriz_suelo.generar_graphviz(
                f"Matriz Suelo - Id: {self.id}",
                self.estacionesBase,
                self.sensoresSuelo,
                f"matriz_Suelo_campoAgricola_{self.id}"
            )

        if self.matriz_cultivo:
            print("Generando visualización de matriz de cultivo...")
            self.matriz_cultivo.generar_graphviz(
                f"Matriz Cultivo - Campo {self.id}",
                self.estacionesBase,
                self.sensoresCultivo,
                f"matriz_Cultivo_campoAgricola_{self.id}"
            )