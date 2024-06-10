veces=1


nombre_trabajador=input("Ingresa el nombre del trabajador: ")
horas_trabajadas=input("Ingrese las horas trabajadas: ")
dias_trabajados=input("Ingrese los dias trabajados: ")
sueldo_hora=input("Ingrese el sueldo por hora: ")

sueldo_semanal=sueldo_hora*dias_trabajados* horas_trabajadas
sueldo_mes=float(sueldo_semanal*4)

if sueldo_mes<=10000:
     print("Obrero tipo A")
if sueldo_mes >10000 and sueldo_mes<15000:
    print("Obrero tipo B")
else:
    print("Sin categoria")
 
