from ListaSimple import ListaSimple
from Frecuencia import FrecuenciaLinea
import graphviz

class matriz:
    def __init__(self, n_filas, n_columnas):
        self.n_filas = n_filas
        self.n_columnas = n_columnas
        self.matriz = ListaSimple()
        
        # Crear matriz 
        for i in range(n_filas):
            fila = ListaSimple()
            for j in range(n_columnas):
                frec = FrecuenciaLinea("", "0")
                fila.insertar(frec)
            self.matriz.insertar(fila)
    
    def establecer(self, n_fila, n_columnas, frec):
        # Establece un dato en posicion [fila, columna]
        fila = self.matriz.obtener(n_fila)
        if fila:
            columna = fila.primero #busca el nodo en "Columna"
            for i in range(n_columnas):
                if columna:
                    columna = columna.siguiente
            if columna:
                columna.dato = frec
    
    def obtener(self, n_fila, n_columnas):
        # Obtiene el dato en posicion [fila, columna]
        fila = self.matriz.obtener(n_fila)
        if fila:
            return fila.obtener(n_columnas)
        return None
    
    def mostrar(self, titulo, headers_fila, headers_columna):
        # Muestra la matriz en forma de tabla
        print(f"\n{titulo}")
        print("-" * 40)
        
        # Encabezados de la tabla
        print("Estacion Base\\Sensor", end="\t")
        for j in range(self.n_columnas):
            sensor = headers_columna.obtener(j)
            print(f"{sensor.id}", end="\t")
        print()
        
        # Filas 
        for i in range(self.n_filas):
            estacion = headers_fila.obtener(i)
            print(f"{estacion.id}", end="\t\t")
            for j in range(self.n_columnas):
                frec = self.obtener(i, j)
                print(f"{frec.valor}", end="\t")
            print()

    # funcion para graficar las matrices generadas
    def generar_graphvizMatriz(self, titulo, headers_fila, headers_columna, nombreArchivo="matriz_tabla"):

        def esc(s):
          return str(s).replace('"', '\\"')
        # Construye columnas
        th_cols = '<td border="1" bgcolor="#f5f7fa"></td>'  
        for j in range(self.n_columnas):
            sensor = headers_columna.obtener(j)
            th_cols += f'<td border="1" bgcolor="#f5f7fa"><b>{esc(sensor.id)}</b></td>'

        # Construye filas
        filas_html = ""
        for i in range(self.n_filas):
           estacion = headers_fila.obtener(i)
           filas_html += f'<tr><td border="1" bgcolor="#f5f7fa"><b>{esc(estacion.id)}</b></td>'
        for j in range(self.num_columnas):
            frecuencia = self.obtener(i, j)
            valor = esc(frecuencia.valor)
            # Color de celda según valor
            bg = "#ffffff" if valor == "0" else "#ffd6d6"  
            filas_html += f'<td border="1" bgcolor="{bg}">{valor}</td>'
        filas_html += '</tr>'

        # Armar tabla HTML-like
        tabla = f'''
          <<table BORDER="0" CELLBORDER="0" CELLSPACING="0">
          <tr><td>
          <table BORDER="1" CELLBORDER="1" CELLSPACING="0">
          <tr>{th_cols}</tr>
              {filas_html}
          </table>
          </td></tr>
          </table>>
        '''

        dot = graphviz.Digraph(comment=str(titulo))
        dot.attr(rankdir='LR')
        dot.node('matriz_tabla', label=tabla, shape='plain')

        dot.node('titulo', label=str(titulo), shape='box', style='filled', fillcolor='lightgreen')
        dot.edge('titulo', 'matriz_tabla', style='invis')  

         # Guarda el DOT en UTF-8
        with open(f'{nombreArchivo}.dot', 'w', encoding='utf-8') as f:
             f.write(dot.source)

        print(f"Se genero el achivo DOT: {nombreArchivo}.dot")
        print(f"Para generar PNG: dot -Tpng {nombreArchivo}.dot -o {nombreArchivo}.png")
        return dot.source
