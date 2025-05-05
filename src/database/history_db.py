# MODULO: history_db.py.
"""
Crea la entidad u objeto que contiene la información necesaria para realizar
nuevos registros en la base de datos, así como sus respectivas consultas.
"""
from decimal import Decimal
from pydantic import BaseModel


# --------------------------------------------------- class -> HistoryTableDB 
class HistoryTableDB(BaseModel):
    """
    Crea la instancia de la tabla history_table en la base de datos.
    atributos:
        - equation: str (equación de la operación)
        - result: Decimal (resultado de la ecuación, tipo Decimal)
    """
    equation: str = None
    result: Decimal = None

    def __str__(self):
        return f"{self.equation} = {self.result}"
