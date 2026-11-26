from Estudiante import Estudiante
from Docente import Docente

lista_estudiantes=[]
estudiante1=Estudiante("John","Cabrera","0105180210","John@hotmail.com",24,"Cuenca","Ingenieria en Sistemas",[8,9,10,7,5])
print(estudiante1.validar_edad())
lista_estudiantes.append(estudiante1)

estudiante2= Estudiante("Samuel","Tobar","0106767676","Samuel@hotmail.com",18,"Cuenca","Ingenieria en Sistemas",[6,7,8,9,10])
print(estudiante2.validar_edad())
lista_estudiantes.append(estudiante2)

estudiante3= Estudiante("Santiago","Rubio","0108940210","Santiago@hotmail.com",24,"Cuenca","Ingenieria en Sistemas",[5,6,7,8,9])
print(estudiante3.validar_edad())
lista_estudiantes.append(estudiante3)

estudiante4= Estudiante("Diego","Rojas","0106350210","Diego@hotmail.com",20,"Cuenca","Ingenieria en Sistemas",[7,8,9,10,6])
print(estudiante4.validar_edad())
lista_estudiantes.append(estudiante4)

estudiante5= Estudiante("Daniel","Cabrera","1716698081","Daniel@hotmail.com",27,"Cuenca","Ingenieria en Sistemas",[9,10,8,7,6])
print(estudiante5.validar_edad())
lista_estudiantes.append(estudiante5)


lista_docentes=[]
docente1= Docente("Veronica", "Segarra", "0105184597", "Vero@hotmail.com", 35, "Cuenca", "BDD", 7)
docente1.calcular_salario()
print(docente1)
lista_docentes.append(docente1)

docente2= Docente("Dina", "Romero", "0105180210", "Diana@hotmail.com", 40, "Cuenca", "Estadistica", 4)
docente2.calcular_salario()
print(docente2) 
lista_docentes.append(docente2)

docente3= Docente("Veronica", "Chimbo", "0415189789", "Veronica@hotmail.com", 30, "Cuenca", "POO II", 7)
docente3.calcular_salario()
print(docente3)
lista_docentes.append(docente3)

docente4= Docente("Carmen", "Tacuri", "0516295123", "Carmen@hotmail.com", 45, "Cuenca", "apps Web", 7)
docente4.calcular_salario()
print(docente4)
lista_docentes.append(docente4)

docente5= Docente("Iliana","Tinoco", "0105945210", "Iliana@hotmail.com", 42, "Cuenca", "expresion", 1)
docente5.calcular_salario()
print(docente5)
lista_docentes.append(docente5)


