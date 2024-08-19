from conexion import conexion, cursor

class dulceria:
    def __init__(self, no_dulces, tipo_dulce, cantidad, precio_unitario, otros, codigo_producto):
        self.no_dulces = no_dulces
        self.tipo_dulce = tipo_dulce
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.otros = otros
        self.codigo_producto = codigo_producto

    @staticmethod
    def insertar(no_dulces, tipo_dulce, cantidad, precio_unitario, otros, codigo_producto):
        sentencia = "INSERT INTO dulceria (no_dulces, tipo_dulce, cantidad, precio_unitario, otros, codigo_producto) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (no_dulces, tipo_dulce, cantidad, precio_unitario, otros, codigo_producto)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Registro exitoso")

    @staticmethod
    def consultar():
        cursor.execute("SELECT * FROM dulceria")
        resultados = cursor.fetchall()
        for i in resultados:
            print(f"no_dulces: {i[0]}, tipo_dulce: {i[1]}, cantidad: {i[2]}, precio_unitario: {i[3]}, otros: {i[4]}, codigo_producto: {i[5]}\n")

    @staticmethod
    def actualizar(codigo_producto):
        no_dulces = input("Número de dulces: ")
        tipo_dulce = input("Tipo de dulce: ")
        cantidad = input("Cantidad: ")
        precio_unitario = input("Precio unitario: ")
        otros = input("Otros detalles: ")
        codigo_producto = input("Código de producto: ")
        sentencia = "UPDATE dulceria SET no_dulces = %s, tipo_dulce = %s, cantidad = %s, precio_unitario = %s, otros = %s WHERE codigo_producto = %s"
        valores = (no_dulces, tipo_dulce, cantidad, precio_unitario, otros, codigo_producto)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Actualización finalizada...")

    @staticmethod
    def eliminar(codigo_producto):
        cursor.execute("DELETE FROM dulceria WHERE codigo_producto = %s", (codigo_producto,))
        conexion.commit()
        print("Eliminado...")
