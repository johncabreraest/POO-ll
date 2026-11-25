from controlador import ControladorAgencia
from modelo import ListaPaquetes
from vista import Vista

def main():
    modelo = ListaPaquetes()
    vista = Vista()
    controlador = ControladorAgencia(modelo, vista)
    controlador.ejecutor()

    main()