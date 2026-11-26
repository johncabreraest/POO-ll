class Paquete:
    def __init__(self, codigo, destino, precio, cupos):
        self.codigo = codigo
        self.destino = destino
        self.precio = precio
        self.cupos = cupos

    def reservar(self, cantidad):
        if cantidad <= 0 or cantidad > self.cupos:
            print(f"Error: solo hay {self.cupos} cupos.")
            return False
        self.cupos -= cantidad
        print(f"Listo. Quedan {self.cupos} cupos.")
        return True

    def __str__(self):
        return f"Código: {self.codigo} | Destino: {self.destino} | Precio: {self.precio:.2f} | Cupos: {self.cupos}"


def buscar_por_codigo(paquetes, codigo):
    for p in paquetes:
        if p.codigo == codigo:
            return p
    return None


def main():
    paquetes = [
        Paquete(1, "Galápagos", 950.00, 20),
        Paquete(2, "Montañita", 180.00, 30),
    ]

    while True:
        print("1. Registrar paquete")
        print("2. Mostrar paquetes")
        print("3. Reservar cupos")
        print("4. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            destino = input("Destino: ").strip()
            precio = float(input("Precio: "))
            cupos = int(input("Cupos: "))
            nuevo_codigo = len(paquetes) + 1
            paquetes.append(Paquete(nuevo_codigo, destino, precio, cupos))
            print(f"Registrado con el código {nuevo_codigo}.")

        elif opcion == "2":
            for p in paquetes:
                print(p)

        elif opcion == "3":
            codigo = int(input("Código del paquete: "))
            paquete = buscar_por_codigo(paquetes, codigo)
            if paquete is None:
                print("Error: no existe ese código.")
            else:
                cantidad = int(input("Cantidad de cupos: "))
                paquete.reservar(cantidad)

        elif opcion == "4":
            break

        else:
            print("Opción no válida.")


main()