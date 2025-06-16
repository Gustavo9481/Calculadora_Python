# MODULO: history_db.py.
"""
Módulo que crea la entidad u objeto que contiene la información necesaria para
realizar nuevos registros en la base de datos, así como sus respectivas
consultas.
"""
from decimal import Decimal
from pydantic import BaseModel


# --------------------------------------------------- class -> HistoryTableDB 
class HistoryTableDB(BaseModel):
    """
    Crea la instancia de la tabla `history_table` en la base de datos.

    :ivar equation: Ecuación de la operación.
    :vartype equation: str
    :ivar result: Resultado de la ecuación, de tipo Decimal.
    :vartype result: Decimal
    """
    equation: str = None
    result: Decimal = None

    def __str__(self) -> str:
        """
        Devuelve la representación en cadena de la operación.

        :returns: Cadena con el formato "<ecuación> = <resultado>".
        :rtype: str
        """
        return f"{self.equation} = {self.result}"
