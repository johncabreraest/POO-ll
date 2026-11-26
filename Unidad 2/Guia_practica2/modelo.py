import csv
from datetime import date


class TipoBicicleta:
    def __init__(self, codigo, tipo, tarifa_hora, disponibles):
        self.codigo = int(codigo)
        self.tipo = tipo
        self.tarifa_hora = float(tarifa_hora)
        self.disponibles = int(disponibles)

    def __str__(self):
        return (
            f"Código: {self.codigo}, Tipo: {self.tipo}, "
            f"Tarifa por hora: ${self.tarifa_hora:.2f}, "
            f"Disponibles: {self.disponibles}"
        )


class Alquiler:
    def __init__(self, numero, codigo_tipo, cantidad, horas, total, fecha, estado):
        self.numero = int(numero)
        self.codigo_tipo = int(codigo_tipo)
        self.cantidad = int(cantidad)
        self.horas = int(horas)
        self.total = float(total)
        self.fecha = fecha
        self.estado = estado

    def __str__(self):
        return (
            f"Número: {self.numero}, Código Tipo: {self.codigo_tipo}, "
            f"Cantidad: {self.cantidad}, Horas: {self.horas}, "
            f"Total: ${self.total:.2f}, Fecha: {self.fecha}, Estado: {self.estado}"
        )


class Lista_Alquiler:
    def __init__(self, ruta_bicicletas="bicicletas.txt",
                 ruta_alquileres="alquileres.txt"):
        self.tipoBicicleta = []
        self.alquiler = []
        self.ruta_bicicletas = ruta_bicicletas
        self.ruta_alquileres = ruta_alquileres
        self.cargar()

    def registrar(self, tipo, tarifa_hora, disponibles):
        if not isinstance(tipo, str) or not tipo.strip():
            raise ValueError("El nombre es obligatorio.")
        tipo = tipo.strip()
        if "," in tipo:
            raise ValueError("El nombre no puede contener comas.")

        try:
            tarifa_hora = float(tarifa_hora)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser mayor que 0.")
        if tarifa_hora <= 0:
            raise ValueError("El precio debe ser mayor que 0.")

        try:
            disponibles = int(disponibles)
        except (TypeError, ValueError):
            raise ValueError("La cantidad debe ser mayor que 0.")
        if disponibles <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")

        nuevo_codigo = max(
            (bicicleta.codigo for bicicleta in self.tipoBicicleta),
            default=0
        ) + 1
        bicicleta = TipoBicicleta(
            nuevo_codigo, tipo, tarifa_hora, disponibles
        )
        self.tipoBicicleta.append(bicicleta)
        return bicicleta

    def buscar_por_codigo(self, codigo):
        try:
            codigo = int(codigo)
        except (TypeError, ValueError):
            raise ValueError("El código debe ser un número.")
        for bicicleta in self.tipoBicicleta:
            if bicicleta.codigo == codigo:
                return bicicleta
        raise ValueError("No existe ese código.")

    def buscar(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Ingrese un nombre para buscar.")
        nombre = nombre.strip().lower()
        coincidencias = [
            bicicleta for bicicleta in self.tipoBicicleta
            if nombre in bicicleta.tipo.lower()
        ]
        if not coincidencias:
            raise ValueError("No se encontraron tipos de bicicleta.")
        return coincidencias

    def alquilar(self, codigo, cantidad, horas):
        bicicleta = self.buscar_por_codigo(codigo)
        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError):
            raise ValueError("La cantidad debe ser mayor que 0.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")

        try:
            horas = int(horas)
        except (TypeError, ValueError):
            raise ValueError("Las horas deben estar entre 1 y 8.")
        if horas < 1 or horas > 8:
            raise ValueError("Las horas deben estar entre 1 y 8.")

        if cantidad > bicicleta.disponibles:
            raise ValueError("No hay suficientes bicicletas disponibles.")

        total = cantidad * horas * bicicleta.tarifa_hora
        numero = max(
            (alquiler.numero for alquiler in self.alquiler),
            default=0
        ) + 1
        alquiler = Alquiler(
            numero, bicicleta.codigo, cantidad, horas, total,
            date.today().isoformat(), "Activo"
        )
        self.alquiler.append(alquiler)
        bicicleta.disponibles -= cantidad
        return alquiler

    def anular(self, numero):
        try:
            numero = int(numero)
        except (TypeError, ValueError):
            raise ValueError("El número de alquiler debe ser válido.")

        alquiler = next(
            (item for item in self.alquiler if item.numero == numero),
            None
        )
        if alquiler is None:
            raise ValueError("No existe ese alquiler.")
        if alquiler.estado.lower() == "anulado":
            raise ValueError("El alquiler ya está anulado.")

        bicicleta = self.buscar_por_codigo(alquiler.codigo_tipo)
        bicicleta.disponibles += alquiler.cantidad
        alquiler.estado = "Anulado"
        return alquiler

    def reporte(self):
        activos = sum(
            alquiler.estado.lower() == "activo"
            for alquiler in self.alquiler
        )
        anulados = sum(
            alquiler.estado.lower() == "anulado"
            for alquiler in self.alquiler
        )
        ingresos = sum(
            alquiler.total for alquiler in self.alquiler
            if alquiler.estado.lower() == "activo"
        )
        agotados = [
            bicicleta for bicicleta in self.tipoBicicleta
            if bicicleta.disponibles == 0
        ]
        disponibles = sum(
            bicicleta.disponibles for bicicleta in self.tipoBicicleta
        )
        return {
            "tipos": len(self.tipoBicicleta),
            "disponibles": disponibles,
            "activos": activos,
            "anulados": anulados,
            "ingresos": ingresos,
            "agotados": agotados,
        }

    def guardar(self):
        with open(
            self.ruta_bicicletas, "w", newline="", encoding="utf-8"
        ) as archivo:
            escritor = csv.writer(archivo)
            for bicicleta in self.tipoBicicleta:
                escritor.writerow([
                    bicicleta.codigo,
                    bicicleta.tipo,
                    f"{bicicleta.tarifa_hora:.2f}",
                    bicicleta.disponibles,
                ])

        with open(
            self.ruta_alquileres, "w", newline="", encoding="utf-8"
        ) as archivo:
            escritor = csv.writer(archivo)
            for alquiler in self.alquiler:
                escritor.writerow([
                    alquiler.numero,
                    alquiler.codigo_tipo,
                    alquiler.cantidad,
                    alquiler.horas,
                    f"{alquiler.total:.2f}",
                    alquiler.fecha,
                    alquiler.estado,
                ])

    def cargar(self):
        try:
            with open(
                self.ruta_bicicletas, "r", newline="", encoding="utf-8"
            ) as archivo:
                filas = list(csv.reader(archivo))
            if filas:
                self.tipoBicicleta = [
                    TipoBicicleta(codigo, tipo, tarifa, disponibles)
                    for codigo, tipo, tarifa, disponibles in filas
                ]
            else:
                self._cargar_iniciales()
        except (FileNotFoundError, OSError):
            self._cargar_iniciales()

        try:
            with open(
                self.ruta_alquileres, "r", newline="", encoding="utf-8"
            ) as archivo:
                self.alquiler = [
                    Alquiler(
                        numero, codigo, cantidad, horas, total, fecha, estado
                    )
                    for numero, codigo, cantidad, horas, total, fecha, estado
                    in csv.reader(archivo)
                ]
        except (FileNotFoundError, OSError):
            self.alquiler = []

    def _cargar_iniciales(self):
        self.tipoBicicleta = [
            TipoBicicleta(1, "Urbana", 2.00, 10),
            TipoBicicleta(2, "Montañera", 3.00, 6),
            TipoBicicleta(3, "Tándem", 5.00, 2),
        ]
