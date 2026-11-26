from Persona import Persona
class Docente(Persona):
    def __init__(self, nombre, apellido, cedula, correo, edad, direccion, asignatura, horas):
        super().__init__(nombre, apellido, cedula, correo, edad, direccion)
        self.asignatura = asignatura
        self.horas = horas
        self.salario=0
        self.valor_hora=20

    def calcular_salario(self):
        self.salario = self.horas * self.valor_hora

    def __str__(self):
        return f"{super().__str__()} Asignatura: {self.asignatura} y tiene un salario de: {self.salario}"

    