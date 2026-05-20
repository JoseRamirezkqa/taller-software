import math
import pytest
from areas import area_triangulo, area_cuadrado, area_circulo


# ─────────────────────────────────────────────
# Tests: Triángulo
# ─────────────────────────────────────────────

def test_area_triangulo_basico():
    assert area_triangulo(10, 5) == 25.0

def test_area_triangulo_valores_decimales():
    resultado = area_triangulo(3.5, 2.0)
    assert resultado == pytest.approx(3.5, rel=1e-6)

def test_area_triangulo_base_cero():
    with pytest.raises(ValueError):
        area_triangulo(0, 5)

def test_area_triangulo_altura_negativa():
    with pytest.raises(ValueError):
        area_triangulo(5, -3)


# ─────────────────────────────────────────────
# Tests: Cuadrado
# ─────────────────────────────────────────────

def test_area_cuadrado_basico():
    assert area_cuadrado(4) == 16.0

def test_area_cuadrado_decimal():
    assert area_cuadrado(2.5) == pytest.approx(6.25)

def test_area_cuadrado_lado_cero():
    with pytest.raises(ValueError):
        area_cuadrado(0)

def test_area_cuadrado_lado_negativo():
    with pytest.raises(ValueError):
        area_cuadrado(-7)


# ─────────────────────────────────────────────
# Tests: Círculo
# ─────────────────────────────────────────────

def test_area_circulo_basico():
    resultado = area_circulo(1)
    assert resultado == pytest.approx(math.pi)

def test_area_circulo_radio_5():
    resultado = area_circulo(5)
    assert resultado == pytest.approx(math.pi * 25)

def test_area_circulo_radio_cero():
    with pytest.raises(ValueError):
        area_circulo(0)

def test_area_circulo_radio_negativo():
    with pytest.raises(ValueError):
        area_circulo(-2)
