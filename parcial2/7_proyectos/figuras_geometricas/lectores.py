class Lectores:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel

    def reservar(self):
        print(f"{self.nombre} se ha reservado un libro.")

    def entregar(self):
        print(f"{self.nombre} se ha entregado el un libro.")


class Estudiantes(Lectores):
    def __init__(self, nombre, direccion, tel, carrera, matricula):
        super().__init__(nombre, direccion, tel)
        self.carrera = carrera
        self.matricula = matricula


class Docentes(Lectores):
    def __init__(self, nombre, direccion, tel, modalidad, num_empleado):
        super().__init__(nombre, direccion, tel)
        self.modalidad = modalidad
        self.num_empleado = num_empleado

estudiante1 = Estudiantes(nombre="Ana Torres Guzman", direccion="Col. Cerro 1500 o/p", tel=8181234567, carrera="MECA", matricula=2235678)
docente1 = Docentes(nombre="Daniel Fuentes Loera", direccion="Fracc. D. Arneta 1400 nte", tel=6183335678, modalidad="TT", num_empleado=123)


estudiante1.reservar()
estudiante1.entregar()

docente1.reservar()
docente1.entregar()