import mysql.connector
from conexionBD import conectar

class Clientes:
    def __init__(self, nif, nombre, direccion, ciudad, tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    def insertar(self):
        connection = conectar()
        cursor = connection.cursor()
        query = "INSERT INTO clientes (nif, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (self.nif, self.nombre, self.direccion, self.ciudad, self.tel))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"Cliente con NIF {self.nif} insertado correctamente.")

    def consultar(self):
        connection = conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM clientes WHERE nif = %s"
        cursor.execute(query, (self.nif,))
        cliente = cursor.fetchone()
        cursor.close()
        connection.close()
        if cliente:
            print(f"Datos del Cliente - NIF: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Ciudad: {cliente[3]}, Tel: {cliente[4]}")
        else:
            print("Cliente no encontrado.")

    def actualizar(self):
        connection = conectar()
        cursor = connection.cursor()
        query = "UPDATE clientes SET nombre = %s, direccion = %s, ciudad = %s, tel = %s WHERE nif = %s"
        cursor.execute(query, (self.nombre, self.direccion, self.ciudad, self.tel, self.nif))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"Cliente con NIF {self.nif} actualizado correctamente.")

    def eliminar(self):
        connection = conectar()
        cursor = connection.cursor()
        query = "DELETE FROM clientes WHERE nif = %s"
        cursor.execute(query, (self.nif,))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"Cliente con NIF {self.nif} eliminado correctamente.")
