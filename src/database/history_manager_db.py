# MODULO: history_manager_db.py
"""
Módulo encargad de gestionar el historial de operaciones
resgistradas enHISTORY_MANAGER -> la base de datos SQLite (calcyulator_db.db).
Usa el decorador gestor_database para manejar la conexión a la base de datos.
Implementa la clase HistoryManager que sigue el patrón Singleton para asegurar
una sola instancia de la base de datos.
"""
import sqlite3
from pathlib import Path
from decimal import Decimal
from typing import Callable, Any
from database.history_db import HistoryTableDB

db_path = Path(__file__).parent.parent / "database" / "calculator_db.db"
db_connect = sqlite3.connect(db_path)


# ------------------------------------------------------------- gestor_database
def gestor_database(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorador para manejar conexión a la base de datos SQLite y el cursor.
    Abre una conexión a la base de datos SQLite,crear un cursor, ejecutar
    función decorada con el cursor y luego cerrar el cursor.
    Maneja cualquier error de la base de datos que pueda ocurrir durante la
    ejecución de la función decorada.
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
        except sqlite3.Error:
            print("Ha ocurrido un error al acceder a la base de datos")

    return db_decorator


# ----------------------------------------------------- class -> HistoryManager
class HistoryManager:
    """
    Gestiona las operaciones create-read-delete en la base de datos.
    Esta clase implementa el patrón Singleton para asegurar una única
    instancia de conexión.
    """
    _instance = None

    def __new__(cls):
        """ Implementa el patrón Singleton. """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @gestor_database
    def create_table(self, cursor=None) -> None:
        """
        Verifica si la tabla ya existe, si no existe la crea.
        Args:
            cursor: conexión a base de datos proporcionado por el decorador.
        Returns:
            None.
        """
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS history_results (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                EQUATION CHAR(50),
                RESULT CHAR(50)
            );
        """
        cursor.execute(create_table_sql)

    @gestor_database
    def new_history(
            self,
            history_equation: str,
            history_result: Decimal,
            cursor=None) -> None:
        """
        Agrega un nuevo registro (ecuación y resultado) al historial (DB).
        Args:
            history_equation (str): La ecuación a guardar
            history_result (Decimal): El resultado de la ecuación
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

    @gestor_database
    def delete_history(self, cursor=None) -> None:
        """
        Elimina el historial de la base de datos.
        Args:
            cursor: Conexión a base de datos proporcionada por el decorador.
        """
        cursor.execute("DELETE FROM history_results")

    @gestor_database
    def get_last_records(self, limit=5, cursor=None) -> list:
        """
        Obtiene los últimos registros del historial.
        Args:
            limit: Número máximo de registros a obtener (por defecto 5).
            cursor: Conexión a base de datos proporcionada por el decorador.
        Returns:
            list: Lista de diccionarios con los registros del historial.
        """
        query = """
            SELECT ID, EQUATION, RESULT
            FROM history_results
            ORDER BY ID DESC
            LIMIT ?
        """
        cursor.execute(query, (limit,))

        records = [
            {"equation": i[1], "result": i[2]} for i in cursor.fetchall()
        ]

        return records


# TEST: pruebas simples de funcionamiento de base de datos. Teporales.
# instance = HistoryManager()
# instance.create_table()
# instance.new_history("2 + 5", Decimal(7))
# instance.get_last_records()
# instance.delete_history()
