import mysql.connector
from conexionBD import *

class Autos:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif

    def insertar(self):
        connection = conectar()
        cursor = connection.cursor()
        query = "INSERT INTO autos (matricula, marca, modelo, color, nif) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (self.matricula, self.marca, self.modelo, self.color, self.nif))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"Auto con matrícula {self.matricula} insertado correctamente.")

    def consultar(self):
        connection = conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM autos WHERE matricula = %s"
        cursor.execute(query, (self.matricula,))
        auto = cursor.fetchone()
        cursor.close()
        connection.close()
        if auto:
            print(f"Datos del Auto - Matrícula: {auto[0]}, Marca: {auto[1]}, Modelo: {auto[2]}, Color: {auto[3]}, NIF: {auto[4]}")
        else:
            print("Auto no encontrado.")

    def actualizar(self):
        connection = conectar()
        cursor = connection.cursor()
        query = "UPDATE autos SET marca = %s, modelo = %s, color = %s, nif = %s WHERE matricula = %s"
        cursor.execute(query, (self.marca, self.modelo, self.color, self.nif, self.matricula))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"Auto con matrícula {self.matricula} actualizado correctamente.")

    def eliminar(self):
        connection = conectar()
        cursor = connection.cursor()
        query = "DELETE FROM autos WHERE matricula = %s"
        cursor.execute(query, (self.matricula,))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"Auto con matrícula {self.matricula} eliminado correctamente.")
