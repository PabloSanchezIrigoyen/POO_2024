from POO import *
from conexion import *


def menu():
    conexion = crear_conexion()
    if conexion:
        while True:
            print("\n--- Menú de Opciones ---")
            print("1. INSERTAR")
            print("2. CONSULTAR")
            print("3. ACTUALIZAR")
            print("4. ELIMINAR")
            print("5. SALIR")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                matricula = input("Matricula: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                color = input("Color: ")
                nif = input("Nif: ")
                Autos.insetar_autonsetar_auto(conexion,matricula, marca, modelo,color,nif)
            elif opcion == '2':
              Autos.consultar_autos(conexion)
            elif opcion == '3':
                matricula = str(input("Matricula del auto que desea actualizar: "))
                marca = str (input("Nueva Marca: "))
                modelo = int (input("Nuevo Modelo: "))
                color = str (input("Nuevo Color: "))
                nif = int(input("Nuevo Nif: "))
                Autos.actualizar_autos(conexion,matricula, marca, modelo,color,nif)
            elif opcion == '4':
                matricula = str(input("Matricula del auto a eliminar: ")) 
                Autos. eliminar_autos(conexion, id)
            elif opcion == '5':
                cerrar_conexion(conexion)
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
