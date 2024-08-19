from conexionBD import conectar

class Revisiones:
    def __init__(self):
        self.conexion = conectar()

    def verificar_matricula(self, matricula):
        cursor = self.conexion.cursor()
        sql = "SELECT matricula FROM autos WHERE matricula = %s"
        cursor.execute(sql, (matricula,))
        resultado = cursor.fetchone()
        return resultado is not None

    def insertar(self):
        cursor = self.conexion.cursor()
        no_revision = int(input("Ingrese el número de revisión: "))
        cambiofiltro = input("¿Se cambió el filtro? (S/N): ")
        cambioaceite = input("¿Se cambió el aceite? (S/N): ")
        cambiofrenos = input("¿Se cambiaron los frenos? (S/N): ")
        otros = input("Otros detalles: ")
        matricula = input("Ingrese la matrícula: ")

        if not self.verificar_matricula(matricula):
            print(f"La matrícula {matricula} no existe en la base de datos. Por favor, intente nuevamente.")
            return

        sql = """INSERT INTO revisiones (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
        cursor.execute(sql, valores)
        self.conexion.commit()

        print("Revisión insertada con éxito.")

    def consultar(self):
        cursor = self.conexion.cursor()
        no_revision = int(input("Ingrese el número de revisión a consultar: "))
        sql = "SELECT * FROM revisiones WHERE no_revision = %s"
        cursor.execute(sql, (no_revision,))
        resultado = cursor.fetchone()

        if resultado:
            print(f"No. Revisión: {resultado[0]}")
            print(f"Cambio de Filtro: {resultado[1]}")
            print(f"Cambio de Aceite: {resultado[2]}")
            print(f"Cambio de Frenos: {resultado[3]}")
            print(f"Otros: {resultado[4]}")
            print(f"Matrícula: {resultado[5]}")
        else:
            print("Revisión no encontrada.")

    def actualizar(self):
        cursor = self.conexion.cursor()
        no_revision = int(input("Ingrese el número de revisión a actualizar: "))
        sql = "SELECT * FROM revisiones WHERE no_revision = %s"
        cursor.execute(sql, (no_revision,))
        resultado = cursor.fetchone()

        if resultado:
            cambiofiltro = input("¿Se cambió el filtro? (S/N): ")
            cambioaceite = input("¿Se cambió el aceite? (S/N): ")
            cambiofrenos = input("¿Se cambiaron los frenos? (S/N): ")
            otros = input("Otros detalles: ")
            matricula = input("Ingrese la nueva matrícula: ")

            if not self.verificar_matricula(matricula):
                print(f"La matrícula {matricula} no existe en la base de datos. Por favor, regístrala primero en la tabla 'autos'.")
                return

            sql_update = """UPDATE revisiones
                            SET cambiofiltro = %s, cambioaceite = %s, cambiofrenos = %s, otros = %s, matricula = %s
                            WHERE no_revision = %s"""
            valores = (cambiofiltro, cambioaceite, cambiofrenos, otros, matricula, no_revision)
            cursor.execute(sql_update, valores)
            self.conexion.commit()

            print("Revisión actualizada con éxito.")
        else:
            print("Revisión no encontrada.")

    def eliminar(self):
        cursor = self.conexion.cursor()
        no_revision = int(input("Ingrese el número de revisión a eliminar: "))
        sql = "DELETE FROM revisiones WHERE no_revision = %s"
        cursor.execute(sql, (no_revision,))
        self.conexion.commit()

        if cursor.rowcount > 0:
            print("Revisión eliminada con éxito.")
        else:
            print("Revisión no encontrada.")


