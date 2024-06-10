

peso=input("Ingrese su peso en kilogramos: ")
altura=input("Ingrese la altura en centimetros: ")

cantidad_imc=1
respuesta=""

IMC=(altura*altura)/peso


if IMC<18.5:
    print("Peso inferior al normal")

elif IMC>=18.5 and IMC<=24.9:
    print("Normal")
elif IMC>=25.0 and IMC<=29.9:
    print("Peso superior al normal")
elif IMC>30.0:
    print("Obesidad")


