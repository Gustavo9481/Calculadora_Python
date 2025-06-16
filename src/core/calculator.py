# MODULO: calculator.py
"""
Proporciona operaciones aritméticas básicas.

Este módulo implementa una calculadora de operaciones aritméticas fundamentales
(suma, resta, multiplicación, división y porcentaje), utilizando el tipo
Decimal para garantizar alta precisión en los cálculos.

Las operaciones son:
- Stateless (sin mantener estado)
- Thread-safe (seguras para uso concurrente)
- Optimizadas con caché para mejorar el rendimiento en cálculos repetitivos

La precisión decimal está configurada a 28 dígitos para mantener la exactitud
en cálculos financieros y científicos.
"""
from functools import lru_cache
from decimal import Decimal, getcontext


getcontext().prec = 28


# --------------------------------------------------------- class -> Calculator
class Calculator:
    """
    Calculadora de operaciones aritméticas básicas con alta precisión.

    Esta clase proporciona métodos estáticos para realizar operaciones
    aritméticas básicas utilizando el tipo Decimal del módulo decimal.
    Todos los métodos están decorados con ``lru_cache`` para optimizar cálculos
    repetitivos.

    :note: No mantiene estado interno; se espera que la lógica de flujo o
        manejo de datos se realice externamente.
    """

    @staticmethod
    @lru_cache(maxsize=1000)
    def add(value_1: Decimal, value_2: Decimal) -> Decimal:
        """
        Suma dos valores decimales.

        :param value_1: Primer valor a sumar.
        :type value_1: Decimal
        :param value_2: Segundo valor a sumar.
        :type value_2: Decimal
        :returns: Resultado de la suma.
        :rtype: Decimal
        """
        return value_1 + value_2

    @staticmethod
    @lru_cache(maxsize=1000)
    def subtract(value_1: Decimal, value_2: Decimal) -> Decimal:
        """
        Resta dos valores decimales.

        :param value_1: Minuendo.
        :type value_1: Decimal
        :param value_2: Sustraendo.
        :type value_2: Decimal
        :returns: Resultado de la resta.
        :rtype: Decimal
        """
        return value_1 - value_2

    @staticmethod
    @lru_cache(maxsize=1000)
    def multiply(value_1: Decimal, value_2: Decimal) -> Decimal:
        """
        Multiplica dos valores decimales.

        :param value_1: Primer factor.
        :type value_1: Decimal
        :param value_2: Segundo factor.
        :type value_2: Decimal
        :returns: Resultado de la multiplicación.
        :rtype: Decimal
        """
        return value_1 * value_2

    @staticmethod
    @lru_cache(maxsize=1000)
    def divide(value_1: Decimal, value_2: Decimal) -> Decimal:
        """
        Divide dos valores decimales.

        :param value_1: Dividendo.
        :type value_1: Decimal
        :param value_2: Divisor.
        :type value_2: Decimal
        :returns: Resultado de la división.
        :rtype: Decimal
        :raises ZeroDivisionError: Si el divisor es cero.
        """
        if value_2 == Decimal(0):
            raise ZeroDivisionError("No se puede dividir por cero")
        return value_1 / value_2

    @staticmethod
    @lru_cache(maxsize=1000)
    def percent(value_1: Decimal, value_2: Decimal) -> Decimal:
        """
        Calcula el porcentaje de un valor respecto a otro.

        :param value_1: Valor base.
        :type value_1: Decimal
        :param value_2: Porcentaje a aplicar.
        :type value_2: Decimal
        :returns: Resultado del porcentaje aplicado.
        :rtype: Decimal
        """
        return (value_1 * value_2) / Decimal(100)
