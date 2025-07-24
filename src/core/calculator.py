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
from functools import lru_cache, wraps
from decimal import Decimal, localcontext


def use_precision(precision: int):
    """
    Crea un decorador para ejecutar una función con precisión decimal local.

    Esta función actúa como una fábrica: se le proporciona un nivel de 
    precisión y devuelve un decorador.
    Este, al ser aplicado a una función, envuelve su ejecución en un 
    `localcontext` del módulo `decimal`.
    Esto asegura que los cálculos se realicen con la precisión especificada sin
    alterar el contexto de precisión global, evitando efectos secundarios.

    :param precision: El número de dígitos de precisión para el contexto local.
    :type precision: int
    :returns: Un decorador listo para ser aplicado a una función.
    :rtype: Callable
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with localcontext() as ctx:
                ctx.prec = precision
                return func(*args, **kwargs)
        return wrapper
    return decorator


# --------------------------------------------------------- class -> Calculator
class Calculator:
    """
    Calculadora de operaciones aritméticas básicas con alta precisión.

    Esta clase proporciona métodos estáticos para realizar operaciones
    aritméticas básicas utilizando el tipo Decimal del módulo decimal.
    Todos los métodos están decorados con ``lru_cache`` para optimizar cálculos
    repetitivos y con ``use_precision`` para dar precision al cálculo.

    :cvar _PRECISION: La precisión decimal (número de dígitos) utilizada
        para todos los cálculos de la clase.

    :vartype _PRECISION: int
    """

    _PRECISION = 28

    @staticmethod
    @lru_cache(maxsize=1000)
    @use_precision(_PRECISION)
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
    @use_precision(_PRECISION)
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
    @use_precision(_PRECISION)
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
    @use_precision(_PRECISION)
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
    @use_precision(_PRECISION)
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
