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
        self.matrizPatrones = None
        self.matrizReducida = None

    def crear_matrices(self):
        #Crea y llena las matrices de frecuencias para sensores de suelo y cultivo.

        
        n_estaciones = self.estacionesBase.tamano
        n_sensoresSuelo = self.sensoresSuelo.tamano
        n_sensoresCultivo = self.sensoresCultivo.tamano

        if n_estaciones == 0 or (n_sensoresSuelo == 0 and n_sensoresCultivo == 0):
            print("No hay se cuenta con suficientes datos para crear las matrices.")
            return

        self.matrizSuelo = matriz(n_estaciones, n_sensoresSuelo)
        self.matrizCultivo = matriz(n_estaciones, n_sensoresCultivo)

        for n_columna in range(n_sensoresSuelo):
            sensor = self.sensoresSuelo.obtener(n_columna)
            frecuenciaActual = sensor.frecuencias.primero
            while frecuenciaActual:
                frecuencia = frecuenciaActual.dato
                n_fila = self.estacionesBase.buscar(frecuencia.id_estacion)
                if n_fila != -1:
                    self.matrizSuelo.establecer(n_fila, n_columna, frecuencia)
                frecuenciaActual = frecuenciaActual.siguiente

        for n_columna in range(n_sensoresCultivo):
            sensor = self.sensoresCultivo.obtener(n_columna)
            frecuenciaActual = sensor.frecuencias.primero
            while frecuenciaActual:
                frecuencia = frecuenciaActual.dato
                n_fila = self.estacionesBase.buscar(frecuencia.id_estacion)
                if n_fila != -1:
                    self.matrizCultivo.establecer(n_fila, n_columna, frecuencia)
                frecuenciaActual = frecuenciaActual.siguiente

    def mostrar_matrices(self):
        #Muestra las matrices de suelo y cultivo en consola.
        
        if self.matrizSuelo:
            titulo_suelo = f"Matriz de Suelo - ID: {self.id}"
            self.matrizSuelo.mostrar(titulo_suelo, self.estacionesBase, self.sensoresSuelo)

        if self.matrizCultivo:
            titulo_cultivo = f"Matriz de Cultivo - ID: {self.id}"
            self.matrizCultivo.mostrar(titulo_cultivo, self.estacionesBase, self.sensoresCultivo)

    def visualizar_matrices_graphviz(self):
        #Genera visualizaciones Graphviz para las matrices de suelo y cultivo.
        
        if self.matrizSuelo:
            print("Generando visualización de matriz de suelo...")
            self.matrizSuelo.generar_graphviz(
                f"Matriz Suelo - Id: {self.id}",
                self.estacionesBase,
                self.sensoresSuelo,
                f"matriz_Suelo_campoAgricola_{self.id}"
            )

        if self.matrizCultivo:
            print("Generando visualización de matriz de cultivo...")
            self.matrizCultivo.generar_graphviz(
                f"Matriz Cultivo - Campo {self.id}",
                self.estacionesBase,
                self.sensoresCultivo,
                f"matriz_Cultivo_campoAgricola_{self.id}"
            )

    def generar_matriz_patrones(self):
        #Genera la matriz de patrones con las filas binarias
        if not self.matrizSuelo or not self.matrizCultivo:
            print("Las matrices originales no están creadas.")
            return

        filas = self.matrizSuelo.filas
        columnas = self.matrizSuelo.columnas + self.matrizCultivo.columnas
        self.matrizPatrones = matriz(filas, columnas)

        for i in range(filas):
            for j in range(self.matrizSuelo.columnas):
                valor = self.matrizSuelo.obtener(i, j)
                binario = 1 if valor != 0 and valor is not None else 0
                self.matrizPatrones.establecer(i, j, binario)

            for j in range(self.matrizCultivo.columnas):
                valor = self.matrizCultivo.obtener(i, j)
                binario = 1 if valor != 0 and valor is not None else 0
                self.matrizPatrones.establecer(i, j + self.matrizSuelo.columnas, binario)

    def generar_matriz_reducida(self):
        #Agrupa filas con el mismo patrón de 0 y 1 (binario)  y suma sus valores.
        
        if not self.matrizPatrones:
            print("La matriz de patrones no ha sido generada.")
            return

        patrones_dict = {}
        filas = self.matrizPatrones.filas
        columnas = self.matrizPatrones.columnas

        for i in range(filas):
            patron = tuple(self.matrizPatrones.obtener(i, j) for j in range(columnas))
            if patron not in patrones_dict:
                patrones_dict[patron] = [i]
            else:
                patrones_dict[patron].append(i)

        self.matrizReducida = matriz(len(patrones_dict), columnas)

        for idx, (patron, indices) in enumerate(patrones_dict.items()):
            suma_fila = [0] * columnas
            for i in indices:
                for j in range(columnas):
                    valor = self.matrizPatrones.obtener(i, j)
                    suma_fila[j] += valor if valor is not None else 0
            for j in range(columnas):
                self.matrizReducida.establecer(idx, j, suma_fila[j])

    def visualizar_matriz_reducida_graphviz(self):
        #Genera el Graphviz de la matriz ya reducida
        
        if self.matrizReducida:
            print("Generando visualización de matriz reducida...")
            self.matrizReducida.generar_graphviz(
                f"Matriz Reducida - Campo {self.id}",
                None,
                None,
                f"matriz_Reducida_campoAgricola_{self.id}"
            )
        else:
            print("La matriz reducida no ha sido generada.")