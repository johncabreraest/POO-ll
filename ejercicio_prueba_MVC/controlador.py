from modelo import ListaPaquetes
from vista import Vista


class ControladorAgencia:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutor(self):
        opcion = ""
        while opcion != "4":
            opcion = self.vista.menu()

            if opcion == "1":
                datos = self.vista.solicitar_datos()
                if datos is not None:
                    destino, precio, cupos = datos
                    nuevo_codigo = self.modelo.registrar_paquete(destino, precio, cupos)
                    self.vista.mensaje(f"Registrado con el código {nuevo_codigo}.")

            elif opcion == "2":
                self.vista.mostrar_paquetes(self.modelo.listaPaquetes)

            elif opcion == "3":
                reserva = self.vista.solicitar_reserva()
                if reserva is not None:
                    codigo, cantidad = reserva
                    paquete = self.modelo.buscar_paquete(codigo)

                    if paquete is None:
                        self.vista.error("Error: no existe ese código.")
                    else:
                        if paquete.reservar(cantidad):
                            self.vista.mensaje(f"Listo. Quedan {paquete.cupos} cupos.")
                        else:
                            self.vista.error(f"Error: solo hay {paquete.cupos} cupos.")

            elif opcion == "4":
                self.vista.mensaje("Adioooosssss...")

            else:
                self.vista.error("Opción no válida.")