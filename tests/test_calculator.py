import pytest
from decimal import Decimal
from core.calculator import Calculator



# ........................ Tests class -> Calculator ........................ 󰌠
# Módulo de tests unitarios para los métodos de la clase Calculator.
# Tests unitarios ejecutados a través de pytest. Config -> pyproject.toml.
# Total de test => 36

# ------------------------------------------------- Tests para Calculator.add()
class TestCalculatorAdd():
    """ Pruebas unitarias para el método Calculator.add() | suma """

    # NOTE: la clase debe instanciarse para poder usar el método
    calculator_instance: Calculator = Calculator()

    # NOTE: las funciones de prueba no requieren hints -> ya que usan
    # aserciones para éxitos o fracasos, no se toma en cuenta el valor

    def test_add_integers_positives(self):
        # suma dos enteros positivos.
        assert self.calculator_instance.add(
            Decimal('2'), Decimal('3')
        ) == Decimal('5')

    def test_add_integers_negatives(self):
        # suma dos enteros negativos.
        assert self.calculator_instance.add(
            Decimal('-2'), Decimal('-3')
        ) == Decimal('-5')

    def test_add_integers_positive_and_negative(self):
        # suma un entero positivo y un entero negativo.
        assert self.calculator_instance.add(
            Decimal('2'), Decimal('-3')
        ) == Decimal('-1')

    def test_add_floats_positives(self):
        # suma dos decimales positivos.
        assert self.calculator_instance.add(
            Decimal('2.5'), Decimal('3.5')
        ) == Decimal('6')

    def test_add_floats_positive_and_negative(self):
        # suma un decimal positivo y un decimal negativo.
        assert self.calculator_instance.add(
            Decimal('2.5'), Decimal('-3.5')
        ) == Decimal('-1')

    def test_add_integer_positive_and_cero(self):
        # suma un entero y valor cero.
        assert self.calculator_instance.add(
            Decimal('2'), Decimal('0')
        ) == Decimal('2')

    def test_add_integer_negative_and_cero(self):
        # suma un entero negativo y valor cero.
        assert self.calculator_instance.add(
            Decimal('-2'), Decimal('0')
        ) == Decimal('-2')

    def test_add_float_positive_and_cero(self):
        # suma un decimal positivo y valor cero.
        assert self.calculator_instance.add(
            Decimal('2.5'), Decimal('0')
        ) == Decimal('2.5')

    def test_add_float_negative_and_cero(self):
        # suma un decimal negativo y valor cero.
        assert self.calculator_instance.add(
            Decimal('-2.5'), Decimal('0')
        ) == Decimal('-2.5')



# --------------------------------------------- Test para Calculator.subtract()
class TestCalculatorSubtract():
    """ Pruebas unitarias para el método Calculator.subtract() | resta """

    calculator_instance: Calculator = Calculator()

    def test_subtract_integers_positives(self):
        # resta dos enteros positivos.
        assert self.calculator_instance.subtract(
            Decimal('3'), Decimal('2')
        ) == Decimal('1')

    def test_subtract_integers_negatives(self):
        # resta dos entero negativos.
        assert self.calculator_instance.subtract(
            Decimal('-3'), Decimal('-2')
        ) == Decimal('-1')

    def test_subtract_integer_positive_and_negative(self):
        # resta un entero positivo y un entero negativo.
        assert self.calculator_instance.subtract(
            Decimal('3'), Decimal('-2')
        ) == Decimal('5')

    def test_subtract_floats_positives(self):
        # resta dos decimales positivos.
        assert self.calculator_instance.subtract(
            Decimal('3.5'), Decimal('2.5')
        ) == Decimal('1')

    def test_subtract_float_positive_and_negative(self):
        # resta un decimal positivo y un decimal negativo.
        assert self.calculator_instance.subtract(
            Decimal('3.5'), Decimal('-2.5')
        ) == Decimal('6')

    def test_subtract_integer_positive_and_cero(self):
        # resta un entero positivo y valor cero.
        assert self.calculator_instance.subtract(
            Decimal('3'), Decimal('0')
        ) == Decimal('3')

    def test_subtract_integer_negative_and_cero(self):
        # resta un entero negativo y valor cero.
        assert self.calculator_instance.subtract(
            Decimal('-3'), Decimal('0')
        ) == Decimal('-3')

    def test_subtract_float_positive_and_cero(self):
        # resta un decimal positivo y valor cero.
        assert self.calculator_instance.subtract(
            Decimal('3.5'), Decimal('0')
        ) == Decimal('3.5')

    def test_subtract_float_negative_and_cero(self):
        # resta un decimal negativo y valor cero.
        assert self.calculator_instance.subtract(
            Decimal('-3.5'), Decimal('0')
        ) == Decimal('-3.5')



# -------------------------------------------- Tests para Calculator.multiply()
class TestCalculatorMultiply():
    """ Pruebas unitarias para el método Calculator.multiply() | multiplo """
    
    calculator_instance: Calculator = Calculator()
   
    def test_multiply_integers_positives(self):
        # multiplica dos enteros positivos.
        assert self.calculator_instance.multiply(
            Decimal('3'), Decimal('2')
        ) == Decimal('6')

    def test_multiply_integers_negatives(self):
        # multiplica dos enteros negativos.
        assert self.calculator_instance.multiply(
            Decimal('-3'), Decimal('-2')
        ) == Decimal('6')

    def  test_multiply_integers_positive_and_negative(self):
        # multiplica un entero positivo por un entero negativo.
        assert self.calculator_instance.multiply(
            Decimal('3'), Decimal('-2')
        ) == Decimal('-6')

    def test_multiply_floats_positives(self):
        # multiplica dos decimales positivos.
        assert self.calculator_instance.multiply(
            Decimal('3.5'), Decimal('2.5')
        ) == Decimal('8.75')

    def test_multiply_floats_positive_and_negative(self):
        # multiplica un decimal positivo y un decimal negativo.
        assert self.calculator_instance.multiply(
            Decimal('3.5'), Decimal('-2.5')
        ) == Decimal('-8.75')

    def test_multiply_integer_positive_and_cero(self):
        # multiplica un entero positivo por valor cero.
        assert self.calculator_instance.multiply(
            Decimal('3'), Decimal('0')
        ) == Decimal('0')

    def test_multiply_integer_negative_and_cero(self):
        # multiplica un entero negativo por valor cero.
        assert self.calculator_instance.multiply(
            Decimal('-3'), Decimal('0')
        ) == Decimal('0')

    def test_multiply_float_positive_and_cero(self):
        # multiplica un decimal positivo por valor cero.
        assert self.calculator_instance.multiply(
            Decimal('3.5'), Decimal('0')
        ) == Decimal('0')

    def test_multiply_float_negative_and_cero(self):
        # multiplica un decimal negativo por valor cero.
        assert self.calculator_instance.multiply(
            Decimal('-3.5'), Decimal('0')
        ) == Decimal('0')



# ----------------------------------------------- Test para Calculator.divide()
class TestCalculatorDivide():
    """ Pruebas unitarias para el método Calculator.divide() | división """

    calculator_instance: Calculator = Calculator()

    def test_divide_integers_positives(self):
        # divide dos enteros positivos.
        assert self.calculator_instance.divide(
            Decimal('6'), Decimal('2')
        ) == Decimal('3')

    def test_divide_integers_negatives(self):
        # divide dos enteros negativos.
        assert self.calculator_instance.divide(
            Decimal('-6'), Decimal('-2')
        ) == Decimal('3')

    def test_divide_integers_positive_and_negative(self):
        # divide un etero positivo y un entero negativo.
        assert self.calculator_instance.divide(
            Decimal('6'), Decimal('-2')
        ) == Decimal('-3')

    def test_divide_floats_positives(self):
        # divide dos decimales positivos.
        assert self.calculator_instance.divide(
            Decimal('6.5'), Decimal('2.5')
        ) == Decimal('2.6')

    def test_divide_floats_positive_and_negative(self):
        # divide un decimal positivo y un decimal negativo.
        assert self.calculator_instance.divide(
            Decimal('6.5'), Decimal('-2.5')
        ) == Decimal('-2.6')

    def test_divide_integer_positive_and_cero(self):
        # divide un entero positivo entre valor cero. -> raise error
        with pytest.raises(
                ZeroDivisionError,
                match = "No se puede dividir por cero"
        ):
            self.calculator_instance.divide(
                Decimal('3'), Decimal('0')
            )

    # NOTE: el str de match debe ser exacto al definido en Calculator.divide()
    
    def test_divide_integer_negative_and_cero(self):
        # divide un entero negativo entre valor cero.
        with pytest.raises(
                ZeroDivisionError,
                match = "No se puede dividir por cero"
        ):
            self.calculator_instance.divide(
                Decimal('-6'), Decimal('0')
            )

    def test_divide_float_positive_and_cero(self):
        # divide un decimal positivo entre valor cero.
        with pytest.raises(
                ZeroDivisionError,
                match = "No se puede dividir por cero"
        ):
            self.calculator_instance.divide(
                Decimal('-6.5'), Decimal('0')
            )

    def test_divide_float_negative_and_cero(self):
        # divide un decimal negativo entre valor cero.
        with pytest.raises(
                ZeroDivisionError,
                match = "No se puede dividir por cero"
        ): 
            self.calculator_instance.divide(
                Decimal('-6.5'), Decimal('0')
            )
