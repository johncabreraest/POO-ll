class VistaAlquiler:
    def mostrar_menu(self):
        print("\n===== SISTEMA DE ALQUILER DE BICICLETAS =====")
        print("1. Registrar tipo de bicicleta")
        print("2. Mostrar tipos de bicicleta")
        print("3. Alquilar")
        print("4. Buscar por nombre")
        print("5. Devolver / anular")
        print("6. Mostrar alquileres")
        print("7. Reporte general")
        print("8. Salir (guarda los archivos)")

    def pedir_opcion(self):
        return input("Seleccione una opción: ").strip()

    def pedir_tipo(self):
        return input("Nombre del tipo: ").strip()

    def pedir_tarifa(self):
        texto = input("Tarifa por hora: ").strip()
        try:
            return float(texto)
        except ValueError:
            raise ValueError("El precio debe ser un número mayor que 0.")

    def pedir_disponibles(self):
        texto = input("Cantidad disponible: ").strip()
        try:
            return int(texto)
        except ValueError:
            raise ValueError("La cantidad debe ser mayor que 0.")

    def pedir_codigo(self):
        texto = input("Código: ").strip()
        try:
            return int(texto)
        except ValueError:
            raise ValueError("El código debe ser un número.")

    def pedir_cantidad(self):
        texto = input("Cantidad: ").strip()
        try:
            return int(texto)
        except ValueError:
            raise ValueError("La cantidad debe ser mayor que 0.")

    def pedir_horas(self):
        texto = input("Horas (1 a 8): ").strip()
        try:
            return int(texto)
        except ValueError:
            raise ValueError("Las horas deben estar entre 1 y 8.")

    def pedir_nombre_busqueda(self):
        return input("Nombre a buscar: ").strip()

    def pedir_numero_alquiler(self):
        texto = input("Número de alquiler: ").strip()
        try:
            return int(texto)
        except ValueError:
            raise ValueError("El número de alquiler debe ser válido.")

    def mostrar_tipos(self, tipos):
        print("\nCódigo  Tipo                 Tarifa/hora  Disponibles")
        print("-" * 58)
        if not tipos:
            print("No hay tipos registrados.")
            return
        for bicicleta in tipos:
            print(bicicleta)

    def mostrar_alquileres(self, alquileres):
        print("\nALQUILERES")
        print("-" * 70)
        if not alquileres:
            print("No hay alquileres registrados.")
            return
        for alquiler in alquileres:
            print(alquiler)

    def mostrar_reporte(self, reporte):
        print("\n===== REPORTE GENERAL =====")
        print(f"Tipos registrados: {reporte['tipos']}")
        print(f"Bicicletas disponibles: {reporte['disponibles']}")
        print(f"Alquileres activos: {reporte['activos']}")
        print(f"Alquileres anulados: {reporte['anulados']}")
        print(f"Ingresos activos: ${reporte['ingresos']:.2f}")
        print("Tipos agotados:")
        if reporte["agotados"]:
            for bicicleta in reporte["agotados"]:
                print(f"- {bicicleta.tipo}")
        else:
            print("- Ninguno")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_error(self, mensaje):
        print(f"Error: {mensaje}")


class VistaCompacta(VistaAlquiler):
    def mostrar_menu(self):
        print("\n1 TIPOS | 2 LISTAR | 3 ALQUILAR | 4 BUSCAR")
        print("5 ANULAR | 6 ALQUILERES | 7 REPORTE | 8 SALIR")
