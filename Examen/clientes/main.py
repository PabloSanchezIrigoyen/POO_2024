from clientes import Clientes

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
