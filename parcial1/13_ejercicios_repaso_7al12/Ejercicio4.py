# 4.- 

#  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

lista = ["gato", "perro", "hamster"]
cadena = "Tengo 19 años y estudio en la UTD"
entero = 100
logico = True

def tipo_dato(variable):
    if isinstance(variable, bool):
        return "Es un valor logico."
    elif isinstance(variable, list):
        return "Es una lista."
    elif isinstance(variable, str):
        return "Es una cadena."
    elif isinstance(variable, int):
        return "Es un entero."
    else:
        return "Tipo de dato desconocido."

print(tipo_dato(lista))  
print(tipo_dato(cadena))  
print(tipo_dato(entero))  
print(tipo_dato(logico))  
