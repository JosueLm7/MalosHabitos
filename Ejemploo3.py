# Función para calcular el área de un rectángulo
def AreaRectangulo(Largo, Ancho):

    AreaRec = Largo * Ancho
    return AreaRec

# Función para calcular el área de un triángulo
def AreaTriangulo(Base, Altura):

    AreaTri = 0.5 * Base * Altura
    return AreaTri

# Función principal
def Principal():

    Largo = 4
    Ancho = 6

    print(f"Área del rectángulo: {AreaRectangulo(Largo, Ancho)}")

    Base = 5
    Altura = 8

    print(f"Área del triángulo : {AreaTriangulo(Base, Altura)}")

Principal()