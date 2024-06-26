# 3.- 

# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

def llenar_lista():
    lista = []

    if not lista:
        print("La lista está vacía. Puedes llenarla con palabras o frases.")
        
        while True:
            entrada = input("Ingrese una palabra o frase (o 'salir' para terminar): ")
            if entrada.lower() == 'salir':
                break
            lista.append(entrada)

    print("Contenido de la lista:")
    for elemento in lista:
        print(elemento.upper())


llenar_lista()
