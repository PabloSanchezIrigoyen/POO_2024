#los errorres de ejecucion en un lenguaje de programacion ocurren cuando existe una anomalia dentro de laejecucion de codigolo cual provoca que se detenga la ejecucion del SW con el control de manejo de excepciones sera posible minimizar o evitar la interrupcion 

#ejemlo 1  cuando una variable no se genera 
try:
    nombre=input("introduce el nombre completo de la persona ")
    if len(nombre)>0:
        nombre_usuario="el nombre completo de la persona es:" +nombre

    print(nombre_usuario)

except:
 print("Es necesario introducir un nombre de usuario...verifica por favor")


x=3+4
print("el valor de x es: " +str(x))

#Ejemplo 2 cuando se solicita un numero y se ingresa otra cosa
try:
    numero=int(input("ingrese un numero entero"))

    if numero>0:
      print("Soy un numero entero positivo")
    elif numero==0:
        print("soy un numero entero neutro") 
    else:
     print("soy un numero entero negativo")
except ValueError:
   print("introduce un valor numerico")

#ejemplo 3 genera multiples excepciones
try:    
    numero=int(input("introduce un numero"))

    print("El cuadrado del numero es:" +str(numero*numero))
except ValueError:
    print("Introduce un valor entero numerico")    
except TypeError:
   print("Se debe convertir a numero entero ") 
else:
   print("no se presentaron errores de ejecucion") 
finally:
   print("Termino la ejecucion")     
