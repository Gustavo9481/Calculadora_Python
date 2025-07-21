# MODULO: history_manager_db.py
"""
Módulo encargado de gestionar el historial de operaciones registradas en
HISTORY_MANAGER, es decir, la base de datos SQLite (calculator_db.db).

Este módulo incluye:

- El decorador gestor_database para manejar automáticamente la conexión a la
  base de datos.
- La clase HistoryManager que implementa el patrón Singleton para asegurar una
  sola instancia de conexión a la base de datos.
"""
import sqlite3
from pathlib import Path
from decimal import Decimal
from typing import Callable, Any
from .history_db import HistoryTableDB


# ------------------------------------------------------------- gestor_database
def gestor_database(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorador para manejar la conexión a la base de datos SQLite y el cursor.
    Abre una conexión a la base de datos SQLite, crea un cursor, ejecuta la
    función decorada pasando el cursor como argumento y luego cierra el cursor.
    Además, captura cualquier error de la base de datos que pueda ocurrir
    durante la ejecución de la función decorada.

    :param func: Función a decorar. Debe aceptar un argumento adicional cursor
            que será proporcionado automáticamente por el decorador.
    :type func: Callable[..., Any]

    :returns: La función decorada con manejo automático de la conexión a la
            base de datos.
    :rtype: Callable[..., Any]

    :raises sqlite3.Error: Si ocurre un error al acceder a la base de datos.
    """

    def db_decorator(self, *args: Any, **kwargs: Any) -> Any:
        try:
            with sqlite3.connect(self.db_path) as db_connect:
                cursor = db_connect.cursor()
                try:
                    return func(self, *args, cursor=cursor, **kwargs)
                finally:
                    cursor.close()
        except sqlite3.Error:
            print("Ha ocurrido un error al acceder a la base de datos")
            return None

    return db_decorator


# ----------------------------------------------------- class -> HistoryManager
class HistoryManager:
    """
    Gestiona las operaciones create-read-delete en la base de datos.
    Esta clase implementa el patrón Singleton para asegurar una única
    instancia de conexión.
    """

    _instance = None
    _db_path = None

    def __new__(cls):
        """
        Implementa el patrón Singleton.

        :returns: Instancia única de `HistoryManager`.
        :rtype: HistoryManager
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Obtener la ruta del directorio del proyecto
            project_dir = Path(__file__).parent.parent.parent
            cls._instance.db_path = project_dir / "calculator_db.db"
        return cls._instance

    @gestor_database
    def create_table(self, cursor=None) -> None:
        """
        Verifica si la tabla de historial existe; si no existe, la crea.

        :param cursor: Conexión a la base de datos proporcionada por el
            decorador.
        :type cursor: sqlite3.Cursor

        :returns: None
        :rtype: None
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
        Agrega un nuevo registro (ecuación y resultado) al historial en la base
        de datos.

        :param history_equation: La ecuación a guardar.
        :type history_equation: str

        :param history_result: El resultado de la ecuación.
        :type history_result: Decimal

        :param cursor: Conexión a la base de datos proporcionada por el
            decorador.
        :type cursor: sqlite3.Cursor

        :returns: None
        :rtype: None
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
        Elimina todos los registros del historial en la base de datos.

        :param cursor: Conexión a la base de datos proporcionada por el
            decorador.
        :type cursor: sqlite3.Cursor

        :returns: None
        :rtype: None
        """
        cursor.execute("DELETE FROM history_results")

    @gestor_database
    def get_last_records(self, limit=5, cursor=None) -> list:
        """
        Obtiene los últimos registros del historial, ordenados de forma
        descendente por ID.

        :param limit: Número máximo de registros a obtener (por defecto 5).
        :type limit: int

        :param cursor: Conexión a la base de datos proporcionada por el
            decorador.
        :type cursor: sqlite3.Cursor

        :returns: Lista de diccionarios, cada uno con los campos 'equation' y
            'result'.
        :rtype: list
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
