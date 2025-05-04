from functools import lru_cache
from decimal import Decimal, getcontext


getcontext().prec = 28


# --------------------------------------------------------- class -> Calculator
class Calculator:
    """
    Realiza operaciones aritméticas básicas utilizando el tipo Decimal para precisión.
    Esta versión es 'stateless' (sin estado) y solo ejecuta cálculos directos.
    El manejo de la secuencia de operaciones y el estado se hará externamente.
    """
    @lru_cache(maxsize=None)
    def add(self, value_1: Decimal, value_2: Decimal) -> Decimal:
        """
        Estrategia de suma
        # No hay necesidad de 'self' si el método no usa atributos de instancia,
        # pero lo mantenemos como método de instancia por convención.
        # Alternativamente, podrían ser @staticmethod.
        """
        return value_1 + value_2

    
    @lru_cache(maxsize=None)
    def subtract(self, value_1: Decimal, value_2: Decimal) -> Decimal:
        """
        Estrategia de resta
        """
        return value_1 - value_2

    
    @lru_cache(maxsize=None)
    def multiply(self, value_1: Decimal, value_2: Decimal) -> Decimal:
        """
        Estrategia de multiplicación
        """ 
        return value_1 * value_2


    @lru_cache(maxsize=None)
    def divide(self, value_1: Decimal, value_2: Decimal) -> Decimal:
        """
        Estrategia de división
        """
        if value_2 == Decimal(0):
            raise ZeroDivisionError("No se puede dividir por cero")
        return value_1 / value_2


    @lru_cache
    def percent(self, value_1: Decimal, value_2: Decimal) -> Decimal:
        """
        Estrategia de porcentaje
        """
        return (value_1 * value_2) / Decimal(100)
