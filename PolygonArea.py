
#Clase figura de la cual heredarán las demás clases
class figura:

    base = 0
    altura =0
    
    #Metodo que variará dependiendo la clase que lo llame
    def obtenerArea():
        pass


class cuadrado(figura):

    def __init__(self, b: float):

        self.b = b

    #Para obtener el area de el cuadrado : base^2
    def obtenerArea(b):

        Area = b**2

        return (Area)

class rectangulo(figura):

    #Para crear un objeto de esta clase se deberá proveer la base y la altura
    def __init__(self, base,  altura):

        self.base = base

        self.altura = altura

    #Para obtener el area del rectangulo : base*altura
    def obtenerArea(base, altura):

        Area = base* altura

        return Area
        

rect = rectangulo(4, 5)
print(rectangulo.obtenerArea())
