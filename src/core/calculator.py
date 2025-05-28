# MODULO: calculator.py
"""
Proporciona operaciones aritméticas básicas.
implementa una calculadora con operaciones aritméticas fundamentales
(suma, resta, multiplicación, división y porcentaje) utilizando el tipo Decimal
para garantizar alta precisión en los cálculos. Las operaciones son
implementadas de manera stateless y thread-safe, optimizadas con caché para
mejorar el rendimiento en cálculos repetitivos.
La precisión decimal está configurada a 28 dígitos para mantener la exactitud
en cálculos financieros y científicos.
"""
from functools import lru_cache
from decimal import Decimal, getcontext


getcontext().prec = 28


# --------------------------------------------------------- class -> Calculator
class Calculator:
    """
    Realiza operaciones aritméticas básicas utilizando el tipo Decimal para
    precisión.
    El manejo de la secuencia de operaciones y el estado se hará externamente.
    Métodos: Sin uso de 'self' si el método no usa atributos de instancia pero
    lo mantenemos como método de instancia por convención.
    Alternativamente, podrían ser @staticmethod.
    """
    @staticmethod
    @lru_cache(maxsize=1000)
    def add(value_1: Decimal, value_2: Decimal) -> Decimal:
        """ Estrategia de suma """
        return value_1 + value_2

    @staticmethod
    @lru_cache(maxsize=1000)
    def subtract(value_1: Decimal, value_2: Decimal) -> Decimal:
        """ Estrategia de resta """
        return value_1 - value_2

    @staticmethod
    @lru_cache(maxsize=1000)
    def multiply(value_1: Decimal, value_2: Decimal) -> Decimal:
        """ Estrategia de multiplicación """
        return value_1 * value_2

    @staticmethod
    @lru_cache(maxsize=1000)
    def divide(value_1: Decimal, value_2: Decimal) -> Decimal:
        """ Estrategia de división """
        if value_2 == Decimal(0):
            raise ZeroDivisionError("No se puede dividir por cero")
        return value_1 / value_2

    @staticmethod
    @lru_cache(maxsize=1000)
    def percent(value_1: Decimal, value_2: Decimal) -> Decimal:
        """ Estrategia de porcentaje """
        return (value_1 * value_2) / Decimal(100)
