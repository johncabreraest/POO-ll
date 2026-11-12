#Recuperacion para un puntito en la lección

def saludar():
    usuario_nombre= input("Ingurese su nombre: ")
    print(f"\n¡Hola, {usuario_nombre}, diviertete.\n")

def pregunta_1():
    print("\nPregunta 1")
    print('Código: print("ab" * 3)')
    resultado = "ab" * 3
    print(f"Resultado de ejecución: {resultado}\n")

def pregunta_2():
    print("\nPregunta 2")
    print('Código: print(type(10.0))')
    resultado = type(10.0)
    print(f"Resultado de ejecución: {resultado}\n")

def pregunta_3():
    print("\nPregunta 3")
    print('Código: socio = {"nombre": "Ana", "saldo": 120}; print(socio.get("correo", "Sin correo"))')
    socio = {"nombre": "Ana", "saldo": 120}
    resultado = socio.get("correo", "Sin correo")
    print(f"Resultado de ejecución: {resultado}\n")

def pregunta_4():
    print("\nPregunta 4")
    print('Código: frase = "aprendo Python en TEC"; print(len(frase.split()))')
    frase = "aprendo Python en TEC"
    resultado = len(frase.split())
    print(f"Resultado de ejecución: {resultado}\n")

def pregunta_5():
    print("\nPregunta 5")
    print('Código: print(int(9.99))')
    resultado = int(9.99)
    print(f"Resultado de ejecución: {resultado}\n")

def pregunta_6():
    print("\nPregunta 6")
    print("Código analizado:")
    print("saldo = 350\nif saldo >= 1000:\n    print('Oro')\nelif saldo >= 100:\n    print('Plata')\nelse:\n    print('Básica')")
    saldo = 350
    print("Resultado de ejecución: ", end="")
    if saldo >= 1000:
        print("Oro")
    elif saldo >= 100:
        print("Plata")
    else:
        print("Básica")
    print()

def pregunta_7():
    print("\nPregunta 7")
    print("Código analizado:")
    print("for x in [2, 4, 6]:\n    if x == 7:\n        print('Encontrado')\n        break\n    else:\n        print('No encontrado')")
    print("Resultado de ejecución:")
    for x in [2, 4, 6]:
        if x == 7:
            print("Encontrado")
            break
        else:
            print("No encontrado")
    print()

def pregunta_8():
    print("\nPregunta 8")
    print("Código analizado:")
    print("for n in [1, 2, 3, 4]:\n    if n == 3:\n        break\n    print(n, end=' ')")
    print("Resultado de ejecución: ", end="")
    for n in [1, 2, 3, 4]:
        if n == 3:
            break
        print(n, end=" ")
    print("\n")

def pregunta_9():
    print("\nPregunta 9")
    print('Código: for i in range(1, 10, 3): print(i, end=" ")')
    print("Resultado de ejecución: ", end="")
    for i in range(1, 10, 3):
        print(i, end=" ")
    print("\n")

def pregunta_10():
    print("\nPregunta 10")
    print('Código: for i in range(3, 0, -1): print(i, end=" ")')
    print("Resultado de ejecución: ", end="")
    for i in range(3, 0, -1):
        print(i, end=" ")
    print("\n")

def pregunta_11():
    print("\nPregunta 11")
    print('Codigo: for i in range(1, 11): for j in range(1, 11): print(f"{i * j:4d}", end="") print()')
    print("Resultado de ejecución: ", end="")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4d}", end="")
    print()

#Menu  Preguntas
def menu_preguntas():
    while True:
        print("================================")
        print("       MENÚ DE PREGUNTAS        ")
        print("================================")
        print("1. Pregunta 1 (\"ab\" * 3)")
        print("2. Pregunta 2 (type(10.0))")
        print("3. Pregunta 3 (Diccionario get)")
        print("4. Pregunta 4 (len frase.split)")
        print("5. Pregunta 5 (int(9.99))")
        print("6. Pregunta 6 (Condicional saldo)")
        print("7. Pregunta 7 (For con else)")
        print("8. Pregunta 8 (For con break)")
        print("9. Pregunta 9 (Range con salto)")
        print("10. Pregunta 10 (Range descendente)")
        print("11. Pregunta 11(Tablas de multiplicar 1-5 y 1-10)")
        print("12. Ejecutar TODAS las preguntas")
        print("13. Volver al menú principal")
        
        opc = input("Seleccione una opción (1-13): ").strip()
        
        if opc == "1": pregunta_1()
        elif opc == "2": pregunta_2()
        elif opc == "3": pregunta_3()
        elif opc == "4": pregunta_4()
        elif opc == "4": pregunta_4()
        elif opc == "5": pregunta_5()
        elif opc == "6": pregunta_6()
        elif opc == "7": pregunta_7()
        elif opc == "8": pregunta_8()
        elif opc == "9": pregunta_9()
        elif opc == "10": pregunta_10()
        elif opc == "11": pregunta_11()
        elif opc == "12":
        
            pregunta_1()
            pregunta_2()
            pregunta_3()
            pregunta_4()
            pregunta_5()
            pregunta_6()
            pregunta_7()
            pregunta_8()
            pregunta_9()
            pregunta_10()
            pregunta_11()
        elif opc == "13":
            print("\n Volviendo al principio rey\n")
            break
        else:
            print("\n Vuelve a intentarlo :)\n")


#Menú

def main():
    while True:
        print("********************************")
        print("        MENÚ DE USUARIOS        ")
        print("********************************")
        print("1. Ingrese nombre")
        print("2. Menu de preguntas")
        print("3. Salir")
        
        opcion = input("Elija una opción (1-3): ").strip()
        
        if opcion == "1":
            saludar()
        elif opcion == "2":
            menu_preguntas()
        elif opcion == "3":
            print(f"\n Nos vimos el martes :)")
            break
        else:
            print("Por favor ingrese 1, 2 o 3, no otro numero.\n")

if __name__ == "__main__":
    main()