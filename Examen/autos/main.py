from modelos import Autos

def menu_autos():
    while True:
        print("\nMenú de Opciones para Autos:")
        print("1. Insertar Auto")
        print("2. Consultar Auto")
        print("3. Actualizar Auto")
        print("4. Eliminar Auto")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            matricula = input("Matrícula: ")
            marca = input("Marca: ")
            modelo = int(input("Modelo: "))
            color = input("Color: ")
            nif = int(input("NIF del Cliente: "))
            auto = Autos(matricula, marca, modelo, color, nif)
            auto.insertar()

        elif opcion == '2':
            matricula = input("Matrícula a consultar: ")
            auto = Autos(matricula, None, None, None, None)
            auto.consultar()

        elif opcion == '3':
            matricula = input("Matrícula a actualizar: ")
            marca = input("Nueva Marca: ")
            modelo = int(input("Nuevo Modelo: "))
            color = input("Nuevo Color: ")
            nif = int(input("Nuevo NIF del Cliente: "))
            auto = Autos(matricula, marca, modelo, color, nif)
            auto.actualizar()

        elif opcion == '4':
            matricula = input("Matrícula a eliminar: ")
            auto = Autos(matricula, None, None, None, None)
            auto.eliminar()

        elif opcion == '5':
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_autos()
