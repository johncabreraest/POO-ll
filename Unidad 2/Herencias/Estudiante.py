from Persona import Persona
class Estudiante(Persona):
    def __init__(self, nombre, apellido, cedula, correo, edad, direccion, carrera, notas):
        super().__init__(nombre, apellido, cedula, correo, edad, direccion)
        self.carrera = carrera
        self.notas = notas

    def proemdio_notas(self):
        return sum(self.notas)/len(self.notas)

    def validar_edad(self):
        return f"{super().validar_edad()} Esta cursando la carrera de: {self.carrera}"

    def __str__(self):
        return f"{super().__str__()} Asiste a: {self.carrera} y tiene un promedio de: {self.proemdio_notas()}"
