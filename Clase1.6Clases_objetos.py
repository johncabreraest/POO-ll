class Libro:
    pass

libro1=Libro()
print(type(libro1))

class Libro:
    def __init__(self, titulo, autor, estado, lista_libros):
        self.titulo=titulo
        self.autor=autor
        self.estado=estado
        self.lista_libros=lista_libros

#MOSTRAR
    def mostrar(self):
        print("nombre del libro:", self.titulo," ","autor:", self.autor)

#CAMBIAR ESTADO
    def cambiar_estado(self, nuevo_estado):
        self.estado=nuevo_estado

#LISTA
    def mostrarlistas(self):
        for e in self.lista_libros:
            print(e)
            
#STRING RETURN
    def __str__(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Estado: {self.estado}"

libro2=Libro("El principito", "Antoine de Saint-Exupéry", "Disponible")
libro2.mostrar()
print(libro2)
libro2.cambiar_estado("Prestado")
print(libro2)
libro2.estado="Disponible"
print(libro2)
libro2.nombre="50 sombras de Grey"
print(libro2.nombre)

