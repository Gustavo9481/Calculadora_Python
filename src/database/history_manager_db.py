# MODULO: history_manager_db.py
"""
HISTORY_MANAGER -> Se encarga de gestionar el historial de operaciones
resgistradas en la base de datos SQLite (calcyulator_db.db).
Usa el decorador gestor_database para manejar la conexión a la base de datos.
Implementa la clase HistoryManager que sigue el patrón Singleton para asegurar
una sola instancia de la base de datos.
"""
# TODO: agregar el método delete_history() para eliminar registros o limpiar
# toda la base de datos.

# TEST: probar funcionamiento de registro real en al base de datos para
# comprobar la nueva ruta.

import sqlite3
from pathlib import Path
from decimal import Decimal
from typing import Callable, Any
from database.history_db import HistoryTableDB


db_path = Path(__file__).parent.parent / "database" / "calculator_db.db"
db_connect = sqlite3.connect(db_path)


# TAG: -------------------------------------------------------- gestor_database
def gestor_database(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorador para manejar conexión a la base de datos SQLite y el cursor.
    Abre una conexión a la base de datos SQLite,crear un cursor, ejecutar
    función decorada con el cursor y luego cerrar el cursor.
    Maneja cualquier error de la base de datos que pueda ocurrir
    durante la ejecución de la función decorada.

    Args:
        func (Callable): función a decorar. Esta función debe aceptar un
                         argumento adicional `cursor` que será pasado
                         automáticamente por eldecorador.

    Returns:
        Callable: La función decorada con manejo automático de
        la conexión a la base de datos.

    Raises:
        sqlite3.Error: Si ocurre un error al acceder a la base de datos.
    """
    def db_decorator(*args: Any, **kwargs: Any) -> Any:
        try:
            with db_connect:
                cursor = db_connect.cursor()
                try:
                    func(*args, cursor=cursor, **kwargs)
                finally:
                    cursor.close()
        # pylint: disable=unused-variable.   # noqa: F841.
        except sqlite3.Error as e:
            print("Ha ocurrido un error al acceder a la base de datos")
    return db_decorator


# TAG: ------------------------------------------------ class -> HistoryManager
class HistoryManager:
    """
    Gestiona las operaciones de historial en la base de datos.
    Esta clase implementa el patrón Singleton para asegurar una única
    instancia de conexión a la base de datos.
    """
    _instance = None

    def __new__(cls):
        """Implementa el patrón Singleton."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @gestor_database
    def create_table(self, cursor=None) -> None:
        """
        Verifica si la tabla ya existe, si no existe la crea

        Args:
            cursor: conexión a base de datos sqlite proporcionado por
            el decorador gestor_database

        Returns:
            None.
        """
        create_table_sql = '''
            CREATE TABLE IF NOT EXISTS history_results (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                EQUATION CHAR(50),
                RESULT CHAR(50)
            );
        '''
        cursor.execute(create_table_sql)

    @gestor_database
    def new_history(
            self,
            history_equation: str,
            history_result: Decimal,
            cursor: sqlite3.Connection) -> None:
        """
        Agrega un nuevo registro al historial.

        Args:
            history_equation: La ecuación a guardar
            history_result: El resultado de la ecuación
            cursor: Conexión a base de datos proporcionada por el decorador
        """
        history_table_db_instance: HistoryTableDB = HistoryTableDB(
            equation=history_equation,
            result=history_result
        )

        if history_table_db_instance:
            equation_str = history_table_db_instance.equation
            result_str = str(history_table_db_instance.result)

            cursor.execute(
                "INSERT INTO history_results (EQUATION, RESULT) VALUES (?,?)",
                (equation_str, result_str)
            )
