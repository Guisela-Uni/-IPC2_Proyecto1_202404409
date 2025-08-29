from model.CampoAgricola import Campo
from model.matriz import matriz
from model.SistemaOptimizacion import SistemaAgricola
import os

sistema = SistemaAgricola

def MenuPrincipal():
    print("------- Optimizador de sistemas de agricultura de precisión ---------")
    print("| Por favor, seleccione una opción:                                  |")
    print("| 1. Cargar archivo                                                  |")
    print("| 2. Procesar archivo                                                |")
    print("| 3. Escribir archivo de salida                                      |")
    print("| 4. Mostrar datos del estudiante                                    |")
    print("| 5. Generar grafica                                                 |")
    print("| 6. Salir                                                           |")
    print("---------------------------------------------------------------------")
    

def DatosEstudiante():
    print("----------------- Datos del Estudiante ------------------")
    print("| Nombre: Guisela Mishell Monroy Ovalle                   |")
    print("| Carnet: 202404409                                       |")
    print("| Introduccion a la programacion y computacion 2          |")
    print("| Seccion C                                               |")
    print("| 4to semestre                                            |")
    print("<<< Enlace a documentacion:                            >>>")
    print("----------------------------------------------------------")

# Bucle principal del menú
while True:
    os.system('cls')
    MenuPrincipal()
    opcion = input("Opcion elegida: ")

    if opcion == "1":
        os.system('cls') #limpia la consola
        print("----------- Cargar Archivo -------------")
        ruta = input("Ingrese la ruta del archivo: ")
        nombreArchivo = input("Ingrese el nombre del archivo: ")
        archivo = ruta + "/" + nombreArchivo if ruta else nombreArchivo
        sistema.Cargar_Archivo(archivo)

    elif opcion == "2":
        print("\nMostrar matrices:")
        sistema.listar_campos()
        IDcampo = input("Ingrese el ID del campo: ")
        sistema.mostrar_campo(IDcampo)
        

    elif opcion == "3":
        os.system('cls')
        print("Ha seleccionado la opción 3")
        

    elif opcion == "4":
        os.system('cls')
        DatosEstudiante()
        input("Presione Enter para continuar...")  
        
    
    elif opcion == "5":
        print("\nGraficar matrices con Graphviz:")
        sistema.listar_campos()
        IDcampo = input("Ingrese el ID del campo: ")

        # Buscar el campo y graficar
        actual = sistema.campos.primero
        encontrado = False
        while actual:
            Campo = actual.dato
            if Campo.id == IDcampo:
                Campo.matriz_suelo .generar_graphviz_tabla(
                    f"Matriz de Suelo - Campo {Campo.id}",
                    Campo.estacionBase,
                    Campo.sensores_suelo,
                    f"matriz_suelo_tabla_campo_{Campo.id}"
                )
                encontrado = True
                break
            actual = actual.siguiente
        if not encontrado:
            print(f"Campo {IDcampo} no encontrado")
        

    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Haz seleccionado una opcion invalida.")
