from mysql.connector import Error
import mysql.connector

try:  
 
    conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    db="gestor_cine"
    )

    if conexion.is_connected():
        print("Conexión exitosa")
        cursor = conexion.cursor()
except Error as ex:
        print("Error durante la conexión:", ex)


def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")