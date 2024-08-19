from conexion import conexion, cursor

class peliculas:
    def __init__(self, num_pelicula, nombre_pelicula, genero, duracion, año):
        self.num_pelicula = num_pelicula
        self.nombre_pelicula = nombre_pelicula
        self.genero = genero
        self.duracion = duracion
        self.año = año

    @staticmethod
    def insertar(num_pelicula, nombre_pelicula, genero, duracion, año):
        sentencia = "INSERT INTO peliculas (num_pelicula, nombre_pelicula, genero, duracion, año) VALUES (%s, %s, %s, %s, %s)"
        valores = (num_pelicula, nombre_pelicula, genero, duracion, año)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Registro exitoso")
    
    @staticmethod
    def consultar(num_pelicula):
        cursor.execute("SELECT * FROM peliculas WHERE num_pelicula = %s", (num_pelicula,))
        resultados = cursor.fetchall()
        for i in resultados:
            print(f"num_pelicula: {i[0]}, nombre_pelicula: {i[1]}, genero: {i[2]}, duracion: {i[3]}, año: {i[4]}")

    @staticmethod
    def actualizar(num_pelicula): 
        nombre_pelicula = input("Nombre de la película: ")
        genero = input("Género de la película: ")
        duracion = input("Duración de la película: ")
        año = input("Año de estreno: ")
        sentencia = "UPDATE peliculas SET nombre_pelicula = %s, genero = %s, duracion = %s, año = %s WHERE num_pelicula = %s"
        valores = (nombre_pelicula, genero, duracion, año, num_pelicula)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Actualización finalizada...")

    @staticmethod
    def eliminar(num_pelicula):
        cursor.execute("DELETE FROM peliculas WHERE num_pelicula = %s", (num_pelicula,))
        conexion.commit()
        print("Eliminado...")
