# MODULO: test_buttons_creator.py
"""
Módulo de pruebas unitarias para los métodos de la clase Calculator.

Este archivo realiza pruebas a los métodos de la clase Calculator ubicada en
``src/core/calculator.py``. Las pruebas están escritas usando el framework
``pytest`` y están configuradas mediante ``pyproject.toml``.

Número total de pruebas: 36/41
"""
from decimal import Decimal
import pytest
from core.calculator import Calculator


# ------------------------------------------------- Tests para Calculator.add()
class TestCalculatorAdd():
    """
    Pruebas unitarias para el método ``Calculator.add()``.

    Verifica el correcto funcionamiento de la operación de suma entre valores
    decimales y enteros, incluyendo combinaciones con cero y números negativos.
    """

    # NOTE: la clase debe instanciarse para poder usar el método
    calculator_instance: Calculator = Calculator()

    # NOTE: las funciones de prueba no requieren hints -> ya que usan
    # aserciones para éxitos o fracasos, no se toma en cuenta el valor

    def test_add_integers_positives(self):
        """
        Verifica la suma dos enteros positivos.
        """
        assert self.calculator_instance.add(
            Decimal('2'), Decimal('3')
        ) == Decimal('5')

    def test_add_integers_negatives(self):
        """
        Verifica la suma dos enteros negativos.
        """
        assert self.calculator_instance.add(
            Decimal('-2'), Decimal('-3')
        ) == Decimal('-5')

    def test_add_integers_positive_and_negative(self):
        """
        Verifica la suma un entero positivo y un entero negativo.
        """
        assert self.calculator_instance.add(
            Decimal('2'), Decimal('-3')
        ) == Decimal('-1')

    def test_add_floats_positives(self):
        """
        Verifica la suma dos decimales positivos.
        """
        assert self.calculator_instance.add(
            Decimal('2.5'), Decimal('3.5')
        ) == Decimal('6')

    def test_add_floats_positive_and_negative(self):
        """
        Verifica la suma un decimal positivo y un decimal negativo.
        """
        assert self.calculator_instance.add(
            Decimal('2.5'), Decimal('-3.5')
        ) == Decimal('-1')

    def test_add_integer_positive_and_cero(self):
        """
        Verifica la suma un entero y valor cero.
        """
        assert self.calculator_instance.add(
            Decimal('2'), Decimal('0')
        ) == Decimal('2')

    def test_add_integer_negative_and_cero(self):
        """
        Verifica la suma un entero negativo y valor cero.
        """
        assert self.calculator_instance.add(
            Decimal('-2'), Decimal('0')
        ) == Decimal('-2')

    def test_add_float_positive_and_cero(self):
        """
        Verifica la suma un decimal positivo y valor cero.
        """
        assert self.calculator_instance.add(
            Decimal('2.5'), Decimal('0')
        ) == Decimal('2.5')

    def test_add_float_negative_and_cero(self):
        """
        Verifica la suma un decimal negativo y valor cero.
        """
        assert self.calculator_instance.add(
            Decimal('-2.5'), Decimal('0')
        ) == Decimal('-2.5')


# --------------------------------------------- Test para Calculator.subtract()
class TestCalculatorSubtract():
    """
    Pruebas unitarias para el método ``Calculator.subtract()``.

    Comprueba la operación de resta entre distintos valores numéricos.
    """

    calculator_instance: Calculator = Calculator()

    def test_subtract_integers_positives(self):
        """
        Verifica la resta dos enteros positivos.
        """
        assert self.calculator_instance.subtract(
            Decimal('3'), Decimal('2')
        ) == Decimal('1')

    def test_subtract_integers_negatives(self):
        """
        Verifica la resta dos entero negativos.
        """
        assert self.calculator_instance.subtract(
            Decimal('-3'), Decimal('-2')
        ) == Decimal('-1')

    def test_subtract_integer_positive_and_negative(self):
        """
        Verifica la resta un entero positivo y un entero negativo.
        """
        assert self.calculator_instance.subtract(
            Decimal('3'), Decimal('-2')
        ) == Decimal('5')

    def test_subtract_floats_positives(self):
        """
        Verifica la resta dos decimales positivos.
        """
        assert self.calculator_instance.subtract(
            Decimal('3.5'), Decimal('2.5')
        ) == Decimal('1')

    def test_subtract_float_positive_and_negative(self):
        """
        Verifica la resta un decimal positivo y un decimal negativo.
        """
        assert self.calculator_instance.subtract(
            Decimal('3.5'), Decimal('-2.5')
        ) == Decimal('6')

    def test_subtract_integer_positive_and_cero(self):
        """
        Verifica la resta un entero positivo y valor cero.
        """
        assert self.calculator_instance.subtract(
            Decimal('3'), Decimal('0')
        ) == Decimal('3')

    def test_subtract_integer_negative_and_cero(self):
        """
        Verifica la resta un entero negativo y valor cero.
        """
        assert self.calculator_instance.subtract(
            Decimal('-3'), Decimal('0')
        ) == Decimal('-3')

    def test_subtract_float_positive_and_cero(self):
        """
        Verifica la resta un decimal positivo y valor cero.
        """
        assert self.calculator_instance.subtract(
            Decimal('3.5'), Decimal('0')
        ) == Decimal('3.5')

    def test_subtract_float_negative_and_cero(self):
        """
        Verifica la resta un decimal negativo y valor cero.
        """
        assert self.calculator_instance.subtract(
            Decimal('-3.5'), Decimal('0')
        ) == Decimal('-3.5')


# -------------------------------------------- Tests para Calculator.multiply()
class TestCalculatorMultiply():
    """
    Pruebas unitarias para el método ``Calculator.multiply()``.

    Evalúa la multiplicación entre diferentes combinaciones de enteros y
    decimales, incluyendo el cero.
    """

    calculator_instance: Calculator = Calculator()

    def test_multiply_integers_positives(self):
        """
        Verifica la multiplicación de dos enteros positivos.
        """
        assert self.calculator_instance.multiply(
            Decimal('3'), Decimal('2')
        ) == Decimal('6')

    def test_multiply_integers_negatives(self):
        """
        Verifica la multiplicación de dos enteros negativos.
        """
        assert self.calculator_instance.multiply(
            Decimal('-3'), Decimal('-2')
        ) == Decimal('6')

    def test_multiply_integers_positive_and_negative(self):
        """
        Verifica la multiplicación de un entero positivo por un entero
        negativo.
        """
        assert self.calculator_instance.multiply(
            Decimal('3'), Decimal('-2')
        ) == Decimal('-6')

    def test_multiply_floats_positives(self):
        """
        Verifica la multiplicación de dos decimales positivos.
        """
        assert self.calculator_instance.multiply(
            Decimal('3.5'), Decimal('2.5')
        ) == Decimal('8.75')

    def test_multiply_floats_positive_and_negative(self):
        """
        Verifica la multiplicación de un decimal positivo y un decimal
        negativo.
        """
        assert self.calculator_instance.multiply(
            Decimal('3.5'), Decimal('-2.5')
        ) == Decimal('-8.75')

    def test_multiply_integer_positive_and_cero(self):
        """
        Verifica la multiplicación de un entero positivo por valor cero.
        """
        assert self.calculator_instance.multiply(
            Decimal('3'), Decimal('0')
        ) == Decimal('0')

    def test_multiply_integer_negative_and_cero(self):
        """
        Verifica la multiplicación de un entero negativo por valor cero.
        """
        assert self.calculator_instance.multiply(
            Decimal('-3'), Decimal('0')
        ) == Decimal('0')

    def test_multiply_float_positive_and_cero(self):
        """
        Verifica la multiplicación de un decimal positivo por valor cero.
        """
        assert self.calculator_instance.multiply(
            Decimal('3.5'), Decimal('0')
        ) == Decimal('0')

    def test_multiply_float_negative_and_cero(self):
        """
        Verifica la multiplicación de un decimal negativo por valor cero.
        """
        assert self.calculator_instance.multiply(
            Decimal('-3.5'), Decimal('0')
        ) == Decimal('0')


# ----------------------------------------------- Test para Calculator.divide()
class TestCalculatorDivide():
    """
    Pruebas unitarias para el método ``Calculator.divide()``.

    Evalúa la operación de división en diversos casos, incluyendo divisiones
    por cero (esperando excepciones).
    """

    calculator_instance: Calculator = Calculator()

    def test_divide_integers_positives(self):
        """
        Verifica la división de dos enteros positivos.
        """
        assert self.calculator_instance.divide(
            Decimal('6'), Decimal('2')
        ) == Decimal('3')

    def test_divide_integers_negatives(self):
        """
        Verifica la división de dos enteros negativos.
        """
        assert self.calculator_instance.divide(
            Decimal('-6'), Decimal('-2')
        ) == Decimal('3')

    def test_divide_integers_positive_and_negative(self):
        """
        Verifica la división de un etero positivo y un entero negativo.
        """
        assert self.calculator_instance.divide(
            Decimal('6'), Decimal('-2')
        ) == Decimal('-3')

    def test_divide_floats_positives(self):
        """
        Verifica la división de dos decimales positivos.
        """
        assert self.calculator_instance.divide(
            Decimal('6.5'), Decimal('2.5')
        ) == Decimal('2.6')

    def test_divide_floats_positive_and_negative(self):
        """
        Verifica la división de un decimal positivo y un decimal negativo.
        """
        assert self.calculator_instance.divide(
            Decimal('6.5'), Decimal('-2.5')
        ) == Decimal('-2.6')

    def test_divide_integer_positive_and_cero(self):
        """
        Verifica la división de un entero positivo entre valor cero.
        -> raise error.
        """
        with pytest.raises(
                ZeroDivisionError,
                match="No se puede dividir por cero"
        ):
            self.calculator_instance.divide(Decimal('3'), Decimal('0'))

    # NOTE: el str de match debe ser exacto al definido en Calculator.divide().

    def test_divide_integer_negative_and_cero(self):
        """
        Verifica la división de un entero negativo entre valor cero.
        """
        with pytest.raises(
                ZeroDivisionError,
                match="No se puede dividir por cero"
        ):
            self.calculator_instance.divide(Decimal('-6'), Decimal('0'))

    def test_divide_float_positive_and_cero(self):
        """
        Verifica la división de un decimal positivo entre valor cero.
        """
        with pytest.raises(
                ZeroDivisionError,
                match="No se puede dividir por cero"
        ):
            self.calculator_instance.divide(Decimal('-6.5'), Decimal('0'))

    def test_divide_float_negative_and_cero(self):
        """
        Verifica la división de un decimal negativo entre valor cero.
        """
        with pytest.raises(
                ZeroDivisionError,
                match="No se puede dividir por cero"
        ):
            self.calculator_instance.divide(Decimal('-6.5'), Decimal('0'))
