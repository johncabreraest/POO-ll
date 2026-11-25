class Vista:
    def menu(self) -> str:
        print("\n--- AGENCIA DE VIAJES ---")
        print("1. Registrar paquete")
        print("2. Mostrar paquetes")
        print("3. Reservar cupos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        return opcion

    def solicitar_datos(self):
        destino = input("Destino: ").strip()
        try:
            precio = float(input("Precio: ").strip())
            cupos = int(input("Cupos: ").strip())
        except ValueError:
            self.error("Error: ingrese valores numéricos válidos.")
            return None
        return destino, precio, cupos

    def solicitar_reserva(self):
        try:
            codigo = int(input("Código del paquete: ").strip())
            cantidad = int(input("Cantidad de cupos: ").strip())
        except ValueError:
            self.error("Error: ingrese valores numéricos válidos.")
            return None
        return codigo, cantidad

    def mostrar_paquetes(self, paquetes: list) -> None:
        for paquete in paquetes:
            print(paquete)

    def mensaje(self, texto: str) -> None:
        print(texto)

    def error(self, texto: str) -> None:
        print(texto)
