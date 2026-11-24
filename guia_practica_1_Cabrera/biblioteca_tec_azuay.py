from datetime import date

ARCHIVO_LIBROS = "libros.txt"
ARCHIVO_PRESTAMOS = "prestamos.txt"

LIBROS_INICIALES = [
    {"codigo": 1, "titulo": "Python para todos", "autor": "Charles Severance", "estado": "Disponible"},
    {"codigo": 2, "titulo": "Aprende Java", "autor": "Ana Torres", "estado": "Disponible"},
    {"codigo": 3, "titulo": "Bases de datos", "autor": "Carlos Mora", "estado": "Disponible"},
]


def guardar_libros(libros):
    with open(ARCHIVO_LIBROS, "w", encoding="utf-8") as archivo:
        for libro in libros:
            linea = f"{libro['codigo']},{libro['titulo']},"
            linea += f"{libro['autor']},{libro['estado']}\n"
            archivo.write(linea)


def cargar_libros():
    libros = []
    try:
        with open(ARCHIVO_LIBROS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip():
                    datos = linea.strip().split(",")
                    libros.append({
                        "codigo": int(datos[0]),
                        "titulo": datos[1],
                        "autor": datos[2],
                        "estado": datos[3]
                    })
    except FileNotFoundError:
        print("No se encontró libros.txt: se usan los libros iniciales.")
        for libro in LIBROS_INICIALES:
            libros.append(dict(libro))
        guardar_libros(libros)
    return libros


def guardar_prestamos(prestamos):
    with open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8") as archivo:
        for p in prestamos:
            linea = f"{p['numero']},{p['codigo_libro']},"
            linea += f"{p['estudiante']},{p['fecha']},{p['estado']}\n"
            archivo.write(linea)


def cargar_prestamos():
    prestamos = []
    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip():
                    datos = linea.strip().split(",")
                    prestamos.append({
                        "numero": int(datos[0]),
                        "codigo_libro": int(datos[1]),
                        "estudiante": datos[2],
                        "fecha": datos[3],
                        "estado": datos[4]
                    })
    except FileNotFoundError:
        guardar_prestamos(prestamos)
    return prestamos


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("ERROR: debe escribir un número entero.")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("ERROR: el texto no puede estar vacío.")
        elif "," in texto:
            print("ERROR: el texto no puede contener comas.")
        else:
            return texto


def buscar_por_codigo(libros, codigo):
    for libro in libros:
        if libro["codigo"] == codigo:
            return libro
    return None


def registrar_libro(libros):
    print("\n--- REGISTRAR LIBRO ---")
    titulo = leer_texto("Título del libro: ")
    autor = leer_texto("Autor del libro: ")

    mayor_codigo = 0
    for libro in libros:
        if libro["codigo"] > mayor_codigo:
            mayor_codigo = libro["codigo"]

    nuevo_libro = {
        "codigo": mayor_codigo + 1,
        "titulo": titulo,
        "autor": autor,
        "estado": "Disponible"
    }
    libros.append(nuevo_libro)
    guardar_libros(libros)
    print(f"Libro '{titulo}' registrado con código {nuevo_libro['codigo']}.")
    return nuevo_libro


def mostrar_libros(libros):
    print("\n--- CATÁLOGO DE LIBROS ---")
    if len(libros) == 0:
        print("No hay libros registrados.")
        return 0

    print(f"{'CÓDIGO':<8} {'TÍTULO':<30} {'AUTOR':<22} {'ESTADO':<12}")
    print("-" * 74)
    for libro in libros:
        print(f"{libro['codigo']:<8} {libro['titulo']:<30} {libro['autor']:<22} {libro['estado']:<12}")
    return len(libros)


def buscar_libro(libros):
    print("\n--- BUSCAR LIBRO ---")
    palabra = leer_texto("Ingrese una palabra del título: ").lower()
    encontrados = []

    for libro in libros:
        if palabra in libro["titulo"].lower():
            encontrados.append(libro)

    if len(encontrados) == 0:
        print("No se encontraron libros con esa palabra.")
        return 0

    print(f"\n{'CÓDIGO':<8} {'TÍTULO':<30} {'AUTOR':<22} {'ESTADO':<12}")
    print("-" * 74)
    for libro in encontrados:
        print(f"{libro['codigo']:<8} {libro['titulo']:<30} {libro['autor']:<22} {libro['estado']:<12}")
    return len(encontrados)


def prestar_libro(libros, prestamos):
    print("\n--- PRESTAR LIBRO ---")
    codigo = leer_entero("Ingrese el código del libro: ")
    libro = buscar_por_codigo(libros, codigo)

    if libro is None:
        print("ERROR: no existe un libro con ese código.")
        return False

    if libro["estado"] != "Disponible":
        print(f"ERROR: el libro '{libro['titulo']}' ya se encuentra prestado.")
        return False

    estudiante = leer_texto("Nombre del estudiante: ")
    numero_prestamo = len(prestamos) + 1

    nuevo_prestamo = {
        "numero": numero_prestamo,
        "codigo_libro": codigo,
        "estudiante": estudiante,
        "fecha": str(date.today()),
        "estado": "Activo"
    }
    prestamos.append(nuevo_prestamo)
    libro["estado"] = "Prestado"

    guardar_libros(libros)
    guardar_prestamos(prestamos)
    print(f"Préstamo #{numero_prestamo} registrado: '{libro['titulo']}' entregado a {estudiante}.")
    return True


def devolver_libro(libros, prestamos):
    print("\n--- DEVOLVER LIBRO ---")
    codigo = leer_entero("Ingrese el código del libro: ")
    libro = buscar_por_codigo(libros, codigo)

    if libro is None:
        print("Error: no existe un libro con ese código.")
        return False

    if libro["estado"] != "Prestado":
        print(f"Error: el libro '{libro['titulo']}' no está prestado.")
        return False

    libro["estado"] = "Disponible"
    for p in prestamos:
        if p["codigo_libro"] == codigo and p["estado"] == "Activo":
            p["estado"] = "Devuelto"
            break

    guardar_libros(libros)
    guardar_prestamos(prestamos)
    print(f"Libro '{libro['titulo']}' devuelto correctamente.")
    return True


def mostrar_prestamos(prestamos, libros):
    print("\n--- LISTADO DE PRÉSTAMOS ---")
    if len(prestamos) == 0:
        print("No existen préstamos registrados.")
        return 0

    print(f"{'N°':<5} {'TÍTULO DEL LIBRO':<28} {'ESTUDIANTE':<22} {'FECHA':<12} {'ESTADO':<10}")
    print("-" * 80)
    for p in prestamos:
        libro = buscar_por_codigo(libros, p["codigo_libro"])
        titulo = libro["titulo"] if libro is not None else "Desconocido"
        print(f"{p['numero']:<5} {titulo:<28} {p['estudiante']:<22} {p['fecha']:<12} {p['estado']:<10}")
    return len(prestamos)


def reporte_general(libros, prestamos):
    print("\n--- REPORTE GENERAL ---")
    total_libros = len(libros)
    disponibles = 0
    prestados = 0
    activos = 0

    for libro in libros:
        if libro["estado"] == "Disponible":
            disponibles += 1
        else:
            prestados += 1

    for p in prestamos:
        if p["estado"] == "Activo":
            activos += 1

    try:
        porcentaje = (prestados / total_libros) * 100
    except ZeroDivisionError:
        porcentaje = 0.0

    print(f"Total de libros       : {total_libros}")
    print(f"Libros disponibles    : {disponibles}")
    print(f"Libros prestados      : {prestados}")
    print(f"Préstamos registrados : {len(prestamos)}")
    print(f"Préstamos activos     : {activos}")
    print(f"Porcentaje prestados  : {porcentaje:.1f} %")
    return porcentaje


def main():
    libros = cargar_libros()
    prestamos = cargar_prestamos()
    opcion = 0
    while opcion != 8:
        print("""
==============================================
        BIBLIOTECA DIGITAL TEC AZUAY
==============================================
1. Registrar libro     5. Devolver libro
2. Mostrar libros      6. Mostrar préstamos
3. Buscar libro        7. Reporte general
4. Prestar libro       8. Salir""")
        opcion = leer_entero("Elija una opción: ")
        if opcion == 1:
            registrar_libro(libros)
        elif opcion == 2:
            mostrar_libros(libros)
        elif opcion == 3:
            buscar_libro(libros)
        elif opcion == 4:
            prestar_libro(libros, prestamos)
        elif opcion == 5:
            devolver_libro(libros, prestamos)
        elif opcion == 6:
            mostrar_prestamos(prestamos, libros)
        elif opcion == 7:
            reporte_general(libros, prestamos)
        elif opcion == 8:
            guardar_libros(libros)
            guardar_prestamos(prestamos)
            print("Datos guardados. Saliendo...")
        else:
            print("ERROR, debe elegir un numero del 1 al 8")


main()