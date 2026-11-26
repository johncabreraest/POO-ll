#Declaracion de funciones
def saludar():
    print("Hola John")
saludar()

#Funcion con parametros
def calcular_edad(ani_actual, anio_nacimiento):
    edad=ani_actual - anio_nacimiento
    print(f"tu edad es: {edad}")

anio=int(input("Ingrese año de nacimiento: "))
anio_act=int(input("Ingrese el año actual: "))
calcular_edad(anio_act, anio)

#Funcion con retorno
def calcular_iva(precio, iva= 1.15):
    total=precio* iva
    return total

precio= float(input("Ingrese el precio: "))
print(f"El precio con iva es: {calcular_iva(precio):.2f}")

#Listas
def par_impar(num):
    if num %2==0:
        return (f"{num} es par")
    else:
        return (f"{num} es impar")
    
lista=[1, 5, 12, 29, 100, 134533]
for num in lista:
    print(par_impar(num), end =",")

#diccionarios
def estudiantes(**lista_estudiantes):
    suma_edades=0 
    for nombre,edad in lista_estudiantes.items():
        print("el estudiante", nombre, "tienes",edad,"años")
        suma_edades+= edad
        print("La suma de todas las edades es:" ,suma_edades)
estudiantes(luis=15, anaya=19, miguel=20, dome=20, pepe=23, alan=18, jose=21)

"""menu de usuarios
1. Ingrese nombre
2. Menu de preguntas
3. Salir
"""