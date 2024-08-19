from conexion import *

class Cliente():
    def __init__(self, nif, nombre, direccion, ciudad, tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    @staticmethod
    def insertar(nif, nombre, direccion, ciudad, tel):
        sentencia = "INSERT INTO clientes (nif, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s)"
        valores = (nif, nombre, direccion, ciudad, tel)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Se ha registrado el cliente exitosamente.")

    @staticmethod
    def consultar(nif=None):
        if nif:
            cursor.execute("SELECT * FROM clientes WHERE nif = %s", (nif,))
        else:
            cursor.execute("SELECT * FROM clientes")
        
        resultados = cursor.fetchall()
        if resultados:
            for i in resultados:
                print(f"nif: {i[0]}, nombre: {i[1]}, direccion: {i[2]}, ciudad: {i[3]}, tel: {i[4]}")
        else:
            print("No se encontraron resultados.")
    

    @staticmethod
    def actualizar(nif):
        nombre = input("Nombre del cliente: ")
        direccion = input("Dirección del cliente: ")
        ciudad = input("Ciudad del cliente: ")
        tel = input("Teléfono del cliente: ")
        sentencia = "UPDATE clientes SET nombre = %s, direccion = %s, ciudad = %s, tel = %s WHERE nif = %s"
        valores = (nombre, direccion, ciudad, tel, nif)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("El registro del cliente ha sido actualizado exitosamente.")

    @staticmethod
    def eliminar(nif):
        cursor.execute("DELETE FROM clientes WHERE nif = %s", (nif,))
        conexion.commit()
        print("El cliente ha sido eliminado exitosamente.")

from conexion import conexion, cursor

class Cliente:
    def __init__(self, nif, nombre, direccion, ciudad, tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    @staticmethod
    def insertar(nif, nombre, direccion, ciudad, tel):
        sentencia = "INSERT INTO clientes (nif, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s)"
        valores = (nif, nombre, direccion, ciudad, tel)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Se ha registrado el cliente exitosamente.")

    @staticmethod
    def consultar(nif=None):
        if nif:
            cursor.execute("SELECT * FROM clientes WHERE nif = %s", (nif,))
        else:
            cursor.execute("SELECT * FROM clientes")
        
        resultados = cursor.fetchall()
        if resultados:
            for i in resultados:
                print(f"nif: {i[0]}, nombre: {i[1]}, direccion: {i[2]}, ciudad: {i[3]}, tel: {i[4]}")
        else:
            print("No se encontraron resultados.")
    
    @staticmethod
    def actualizar(nif):
        nombre = input("Nombre del cliente: ")
        direccion = input("Dirección del cliente: ")
        ciudad = input("Ciudad del cliente: ")
        tel = input("Teléfono del cliente: ")
        sentencia = "UPDATE clientes SET nombre = %s, direccion = %s, ciudad = %s, tel = %s WHERE nif = %s"
        valores = (nombre, direccion, ciudad, tel, nif)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("El registro del cliente ha sido actualizado exitosamente.")

    @staticmethod
    def eliminar(nif):
        cursor.execute("DELETE FROM clientes WHERE nif = %s", (nif,))
        conexion.commit()
        print("El cliente ha sido eliminado exitosamente.")
