from pydantic import BaseModel
from decimal import Decimal


class HistoryTableDB(BaseModel):
    equation: str
    result: Decimal

    def __str__(self):
        return f"{equation} = {result}"
