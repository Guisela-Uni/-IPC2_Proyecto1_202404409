class InfoNodo(): #clase generica, que me permite heredar a clases hijas, estructura de mis objetos informacion
    def desplegar():
        pass
    
    def EsIgualALLave():
        pass

class Nodo: 
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,dato):
        self.info = dato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente


class ListaSimple: 

    def __init__(self): 
        self.primero = None
        self.tamano = 0

    def estaVacia(self):
        return self.primero == None

    def agregar(self,item): 
        nuevo = Nodo(item)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.asignarSiguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamano +=1
    
    def obtener(self, indice):
        if indice < 0 or indice >= self.longitud:
            return None
        actual = self.primero
        for i in range(indice):
            actual = actual.siguiente
        return actual.dato

    def tamano(self):
        actual = self.primero
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        return contador

    def desplegar(self):
        actual = self.primero
        while actual != None:
            actual.obtenerDato().desplegar() 
            actual = actual.obtenerSiguiente() 

    def buscar(self,idBuscar):
        # Busca el índice de un elemento por su id
        actual = self.primero
        indice = 0
        while actual:
            if hasattr(actual.dato, 'id') and actual.dato.id == idBuscar:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1

    def eliminar(self,item):
        actual = self.primero
        previo = None 
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato().EsIgualALLave(item):
                encontrado = True 
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            if self.primero != None:
                self.primero = actual.obtenerSiguiente()
                print("Eliminado")
        else:
            if encontrado:
                previo.asignarSiguiente(actual.obtenerSiguiente())
                print("Eliminado")
            else:
                print("no encontrado")