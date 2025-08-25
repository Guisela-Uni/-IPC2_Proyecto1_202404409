class InfoNodo(): #clase generica, que me permite heredar a clases hijas, estructura de mis objetos informacion
    def desplegar():
        pass
    
    def EsIgualALLave():
        pass

class Nodo: 
    def __init__(self,info):
        self.info = info
        self.siguiente = None

    def obtenerDato(self):
        return self.info

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,info):
        self.info = info

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente


class ListaSimple: 

    def __init__(self): 
        self.primero = None

    def estaVacia(self):
        return self.primero == None

    def agregar(self,item): 
        nuevo = Nodo(item)
        nuevo.asignarSiguiente(self.primero)
        self.primero = nuevo 

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

    def buscar(self,item):
        actual = self.primero
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato().EsIgualALLave(item):
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado

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