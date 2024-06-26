# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

lista = []

#Usando While
while len(lista) < 120:
    lista.append(len(lista) + 1)

print("Lista con valores agregados:")
for valor in lista:
    print(valor)

#Usando for
for i in range(120):
    lista.append(i + 1)
    
print("Lista con valores agregados:")
for valor in lista:
    print(valor)
