from funciones import Revisiones
import getpass
from funciones1 import *
from clientes.clientes import Clientes
from usuarios import usuario

def menu_principal():
    while True:    
        borrarPantalla()
        print("""
            
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="REGISTRO":
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ")
            apellidos=input("\t ¿Cuales son tus apellidos?: ")
            email=input("\t Ingresa tu email: ")
            password=getpass.getpass("\t Ingresa tu contraseña: ")
            obj_usurio=usuario(nombre,apellidos,email,password)
            resultado=obj_usurio.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registro correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor intentelo de nuevo, no fue posible insertar el registro ** ...")  
            esperarTecla()      
        elif opcion == '2' or opcion=="LOGIN":
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            #Agregar codigo 
            registro=usuario.Usuario.iniciar_sesion(email,password)
            if registro:
                menu_clientes(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t Email y/o contraseña incorrectas... vuelva a intentarlo ...")
                esperarTecla()    
        elif opcion == '3' or opcion=="SALIR":
            print("\n\t.. ¡Gracias Bye! ...")
            #opc=False
            break
            #exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()




def menu_clientes():
    while True:
        print("\nMenú de Opciones para Clientes:")
        print("1. Insertar Cliente")
        print("2. Consultar Cliente")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nif = int(input("NIF: "))
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            ciudad = input("Ciudad: ")
            tel = int(input("Teléfono: "))
            cliente = Clientes(nif, nombre, direccion, ciudad, tel)
            cliente.insertar()

        elif opcion == '2':
            nif = int(input("NIF a consultar: "))
            cliente = Clientes(nif, None, None, None, None)
            cliente.consultar()

        elif opcion == '3':
            nif = int(input("NIF a actualizar: "))
            nombre = input("Nuevo Nombre: ")
            direccion = input("Nueva Dirección: ")
            ciudad = input("Nueva Ciudad: ")
            tel = int(input("Nuevo Teléfono: "))
            cliente = Clientes(nif, nombre, direccion, ciudad, tel)
            cliente.actualizar()

        elif opcion == '4':
            nif = int(input("NIF a eliminar: "))
            cliente = Clientes(nif, None, None, None, None)
            cliente.eliminar()

        elif opcion == '5':
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_clientes()



def mostrar_revisiones():
    print("=== Menú de Revisiones ===")
    print("1. Insertar revisión")
    print("2. Consultar revisiones")
    print("3. Actualizar revisión")
    print("4. Eliminar revisión")
    print("5. Salir")

def ejecutar_menu():
    revisiones = Revisiones()

    while True:
        mostrar_revisiones()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            revisiones.insertar()
        elif opcion == '2':
            revisiones.consultar()
        elif opcion == '3':
            revisiones.actualizar()
        elif opcion == '4':
            revisiones.eliminar()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor selecciona otra.")

if __name__ == "__main__":
    ejecutar_menu()
