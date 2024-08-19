from conexion import *

class Autos:
    def __init__(self,matricula, marca, modelo,color,nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.nif = nif


    def insetar_auto(conexion,matricula, marca, modelo,color,nif):
        cursor = conexion.cursor()
        query = "INSERT INTO AUTOS (matricula, marca, modelo,color,nif) VALUES (%s, %s, %s)"
        valores = (matricula, marca, modelo,color,nif)
        cursor.execute(query, valores)
        conexion.commit()
        print("Auto insertado exitosamente")
    
    def consultar_autos(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM autos"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"Matricula: {fila[0]}, Marca: {fila[1]}, Modelo: {fila[2]}, Color: {fila[3]}, Nif: {fila[4]}")
            
    def actualizar_autos(conexion,matricula, marca, modelo,color,nif):
        cursor = conexion.cursor()
        query = "UPDATE autos SET marca = %s, modelo = %s, color = %s WHERE matricula = %s"
        valores = (conexion,matricula, marca, modelo,color,nif)
        cursor.execute(query, valores)
        conexion.commit()
        print("Auto actualizado exitosamente")

    def eliminar_autos(conexion, id):
        cursor = conexion.cursor()
        query = "DELETE FROM autos WHERE matricula = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        print("Auto eliminado exitosamente")
