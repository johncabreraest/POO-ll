from modelo import Lista_Alquiler
from vista import VistaAlquiler


class ControladorAlquiler:
    def __init__(self, modelo=None, vista=None):
        self.modelo = modelo or Lista_Alquiler()
        self.vista = vista or VistaAlquiler()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()
            try:
                if opcion == "1":
                    tipo = self.vista.pedir_tipo()
                    tarifa = self.vista.pedir_tarifa()
                    disponibles = self.vista.pedir_disponibles()
                    bicicleta = self.modelo.registrar(
                        tipo, tarifa, disponibles
                    )
                    self.vista.mostrar_mensaje(
                        f"Tipo registrado con código {bicicleta.codigo}."
                    )
                elif opcion == "2":
                    self.vista.mostrar_tipos(self.modelo.tipoBicicleta)
                elif opcion == "3":
                    codigo = self.vista.pedir_codigo()
                    cantidad = self.vista.pedir_cantidad()
                    horas = self.vista.pedir_horas()
                    alquiler = self.modelo.alquilar(
                        codigo, cantidad, horas
                    )
                    self.vista.mostrar_mensaje(
                        f"Alquiler N.º {alquiler.numero} registrado. "
                        f"Total: ${alquiler.total:.2f}"
                    )
                elif opcion == "4":
                    nombre = self.vista.pedir_nombre_busqueda()
                    coincidencias = self.modelo.buscar(nombre)
                    self.vista.mostrar_tipos(coincidencias)
                elif opcion == "5":
                    numero = self.vista.pedir_numero_alquiler()
                    alquiler = self.modelo.anular(numero)
                    self.vista.mostrar_mensaje(
                        f"Alquiler N.º {alquiler.numero} anulado."
                    )
                elif opcion == "6":
                    self.vista.mostrar_alquileres(self.modelo.alquiler)
                elif opcion == "7":
                    self.vista.mostrar_reporte(self.modelo.reporte())
                elif opcion == "8":
                    self.modelo.guardar()
                    self.vista.mostrar_mensaje(
                        "Datos guardados. ¡Hasta luego!"
                    )
                    break
                else:
                    self.vista.mostrar_error(
                        "Opción inválida. Seleccione entre 1 y 8."
                    )
            except ValueError as error: 
                self.vista.mostrar_error(str(error))


if __name__ == "__main__":
    ControladorAlquiler().ejecutar()
