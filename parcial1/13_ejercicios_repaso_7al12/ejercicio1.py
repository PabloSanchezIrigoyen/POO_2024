# 1.- 

#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla °
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla °
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

numeros = [20, 7, 13, 32, 6, 62, 42, 14]

# a.- Recorrer la lista y mostrarla
print("Lista de números:")

for numero in numeros:
    print(numero)

#b.- hacer una funcion que recorra la lista de numeros y devuelva un string

def lista_string(lista):
    return ', '.join(map(str, lista))

# c.- Ordenar la lista y mostrarla
numeros.sort()
print("Lista ordenada:")
print(numeros)

# d.- Mostrar su longitud
longitud = len(numeros)
print("\nLongitud de la lista:")
print(longitud)

# e.- Buscar algún elemento que el usuario pida por teclado
num_buscar = int(input("Introduce el número que quieres buscar en la lista: "))
if num_buscar in numeros:
    print(f"El número {num_buscar} está en la lista.")
else:
    print(f"El número {num_buscar} no está en la lista.")
