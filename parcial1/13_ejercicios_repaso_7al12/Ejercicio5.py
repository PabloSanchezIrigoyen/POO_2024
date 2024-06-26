# Crear una lista y un diccionario con el contenido de esta tabla: 

#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION


#   imprimir la información

tabla_lista = [
    ["ACCION", "TERROR", "DEPORTES"],
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

def imprimir_lista(lista):
    print("")
    print("Contenido de la lista:")
    print("")
    for fila in lista:
        print(fila)

imprimir_lista(tabla_lista)

tabla_dict = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

def imprimir_diccionario(diccionario):
    print("")
    print("Contenido del diccionario:")
    print("")
    for categoria, peliculas in diccionario.items():
        print(f"{categoria}: {peliculas}")

imprimir_diccionario(tabla_dict)

