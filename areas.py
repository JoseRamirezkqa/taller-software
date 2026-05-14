import math


def area_triangulo(base: float, altura: float) -> float:
    """Calcula el área de un triángulo dado su base y altura."""
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero.")
    return (base * altura) / 2


def area_cuadrado(lado: float) -> float:
    """Calcula el área de un cuadrado dado el largo de su lado."""
    if lado <= 0:
        raise ValueError("El lado debe ser mayor que cero.")
    return lado ** 2


def area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    if radio <= 0:
        raise ValueError("El radio debe ser mayor que cero.")
    return math.pi * radio ** 2
