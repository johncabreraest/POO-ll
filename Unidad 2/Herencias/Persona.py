class Persona:
    def __init__(self, nombre, apellido, cedula, correo, edad, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo
        self.edad = edad
        self.direccion = direccion

    def validar_edad(self):
        if self.edad>=18:
            return "Eres un adulto responsable."
        else:
            return "Eres un niño anda a ver pocoyo."

    def __str__(self):
        return f"Nombre: {self.nombre}|Apellido: {self.apellido}| Cédula: {self.cedula}| Correo: {self.correo}| Edad: {self.edad}| Dirección: {self.direccion}"

