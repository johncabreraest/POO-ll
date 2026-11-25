class Paquete:
    def __init__(self, codigo: int, destino: str, precio: float, cupos: int):
        self.codigo = codigo
        self.destino = destino
        self.precio = precio
        self.cupos = cupos

    def reservar(self, cantidad: int) -> bool:
        if cantidad <= 0 or cantidad > self.cupos:
            return False
        self.cupos -= cantidad
        return True

    def __str__(self) -> str:
        return (
            f"[{self.codigo}] {self.destino} | "
            f"Precio: ${self.precio:.2f} | "
            f"Cupos disponibles: {self.cupos}"
        )


class ListaPaquetes:
    def __init__(self):
        self.listaPaquetes = []
        self.cargar_datos()

    def cargar_datos(self):
        datos = [
            Paquete(1, "Galápagos", 950.00, 20),
            Paquete(2, "Montañita", 180.00, 30),
        ]
        for p in datos:
            self.listaPaquetes.append(p)

    def registrar_paquete(self, destino: str, precio: float, cupos: int) -> int:
        nuevo_codigo = len(self.listaPaquetes) + 1
        nuevo = Paquete(nuevo_codigo, destino, precio, cupos)
        self.listaPaquetes.append(nuevo)
        return nuevo_codigo

    def buscar_paquete(self, codigo: int) -> Paquete | None:
        for paquete in self.listaPaquetes:
            if paquete.codigo == codigo:
                return paquete
        return None

    def mostrar_lista_paquetes(self) -> list:
        return self.listaPaquetes