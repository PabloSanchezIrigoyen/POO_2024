#formas de concatenar en python

nombre="Pablo Sanchez"
Especialidad="Area de SW Multiplataforma"
carrera="Ingenieria en Gestion y Desarrollo de SW"

#1er forma
print("mi nombre es"+nombre+"estoy en la especialidad de"+Especialidad+"y estudio la carrera de "+carrera)

print("\n")

#2da forma 
print("mi nombre es",nombre,"estoy en la especialidad de",Especialidad,"y estudio la carrera de ",carrera)

print("\n")

#3er forma MAS COMUN EN PYTHON
print(f"Mi nombre es ,{nombre}, estoy en la especialidad de ,{Especialidad}, y estudio la carrera de ,{carrera}")

print("\n")

#4ta forma 
print("Mi nombre es ,{}, estoy en la especialidad de ,{}, y estudio la carrera de ,{}".format(nombre,Especialidad,carrera))

print("\n")

#5ta forma
print('Mi nombre es '+nombre+' estoy en la especialidad de'+Especialidad+' y estudio la carrera de '+carrera)

print("\n")
