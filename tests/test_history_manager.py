import sqlite3
import pytest
import database.history_manager_db as history_manager_module
from typing import Generator
from decimal import Decimal 
from database.history_manager_db import HistoryManager


class TestHistoryManager:
    """Pruebas unitarias para la clase HistoryManager"""

    @pytest.fixture
    def history_manager(self):
        """
        Proporciona una instancia de HistoryManager para las pruebas.

        Este fixture crea y devuelve una nueva instancia de HistoryManager que
        puede ser utilizada en las pruebas para gestionar el historial.
        """
        return HistoryManager()


    @pytest.fixture
    def memory_db_connection(self) -> Generator[sqlite3.Connection, None, None]:
        """Proporciona una conexión temporal a una base de datos SQLite en 
        memoria para pruebas.

        Este fixture crea una base de datos SQLite en memoria que:
        - Se inicializa antes de cada prueba
        - Se mantiene disponible durante la ejecución de la prueba
        - Se cierra y limpia automáticamente después de cada prueba

        Returns:
            Generator[sqlite3.Connection, None, None]: Un generador que produce 
            una conexión a la base de datos SQLite en memoria. El generador no 
            espera ningún valor de entrada (None) y no retorna ningún valor 
            final (None).
        """
        conn = sqlite3.connect(':memory:')
        yield conn
        conn.close()


    def test_new_history_inserts_data(
            self, history_manager, memory_db_connection, mocker
    ):
        """Verifica la inserción de un registro individual en la base de datos.

        Esta prueba unitaria valida el funcionamiento básico de new_history al:
        - Insertar una operación matemática simple (2+2)
        - Verificar la correcta conversión de tipos (Decimal a str)
        - Comprobar que el registro se guardó exactamente como se esperaba
        - Validar que solo existe un registro en la tabla

        Proceso de la prueba:
        1. Configura una base de datos en memoria con la tabla necesaria
        2. Realiza una inserción de prueba con valores conocidos
        3. Verifica que los datos se insertaron correctamente
        4. Comprueba que solo existe un registro en la tabla

        Notas:
        - Utiliza una base de datos en memoria para el testing
        - Hace uso de mocking para aislar la prueba
        - La ecuación y resultado son valores simples para facilitar la 
          verificación
        """

        test_equation = "2+2"
        test_result = Decimal("4")
        expected_result_str = "4"

        mocker.patch.object(
            history_manager_module, 'db_connect', memory_db_connection
        )
        
        history_manager.create_table()

        history_manager.new_history(test_equation, test_result)

        cursor = memory_db_connection.cursor()
        cursor.execute(
            "SELECT EQUATION, RESULT FROM history_results WHERE EQUATION = ?", 
            (test_equation,)
        )
        inserted_data = cursor.fetchone()
        cursor.close()

        assert inserted_data is not None
        assert inserted_data[0] == test_equation
        assert inserted_data[1] == expected_result_str

        cursor = memory_db_connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM history_results")
        count = cursor.fetchone()[0]
        cursor.close()
        assert count == 1

    def test_new_history_multiple_inserts(
            self, history_manager, memory_db_connection, mocker
    ):
        """Verifica la correcta inserción de múltiples registros en la base de 
        datos.

        Esta prueba valida que la función new_history:
        - Puede manejar múltiples inserciones consecutivas
        - Mantiene la integridad de todos los registros insertados
        - Gestiona correctamente diferentes tipos de operaciones y resultados
        """

        history_entries = [
            {"equation": "1+1", "result": Decimal("2")},
            {"equation": "10-5", "result": Decimal("5")},
            {"equation": "2*3", "result": Decimal("6.0")},
        ]
        expected_count = len(history_entries)

        mocker.patch.object(
            history_manager_module, 'db_connect', memory_db_connection
        )
        history_manager.create_table()

        # --- Act ---
        for entry in history_entries:
            history_manager.new_history(entry["equation"], entry["result"])

        # --- Assert ---
        cursor = memory_db_connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM history_results")
        count = cursor.fetchone()[0]
        assert count == expected_count

        cursor.execute(
            "SELECT EQUATION, RESULT FROM history_results ORDER BY ID"
        )
        results = cursor.fetchall()

        assert len(results) == expected_count
        for i, entry in enumerate(history_entries):
            assert results[i][0] == entry["equation"]
            assert results[i][1] == str(entry["result"])

        cursor.close()

    def test_singleton_pattern(self):
        """Verifica que HistoryManager implementa correctamente el patrón 
        Singleton.
        
        Esta prueba valida que:
        - Múltiples instanciaciones retornan el mismo objeto
        - La identidad de los objetos es la misma
        """

        instance1 = HistoryManager()
        instance2 = HistoryManager()
        
        assert instance1 is instance2        # Verifica que son el mismo objeto
        assert id(instance1) == id(instance2)    # Verifica que tienen mismo ID



# documentación

# memory_db_connection ->
# Esta función llamada memory_db_connection es lo que llamamos un "fixture" en pytest 
# (una herramienta para pruebas en Python). 
# Su propósito es crear una base de datos temporal para realizar pruebas.
# Veamos paso a paso lo que hace:
# 
# 1. El decorador @pytest.fixture indica que esta es una función especial que pytest usará 
# para preparar el ambiente de pruebas.
# 
# 2. La función crea una conexión a una base de datos SQLite que existe solo en la memoria 
# RAM (no en el disco duro) usando :memory:. Esto es perfecto para pruebas porque:
#     - Es muy rápida
#     - Se borra automáticamente cuando termina la prueba
#     - No deja archivos residuales en el sistema
# 
# 3. La palabra clave yield es muy importante aquí:
#     - Todo lo que está antes del yield se ejecuta antes de la prueba
#     - El yield conn proporciona la conexión a la base de datos a la prueba
#     - Todo lo que está después del yield se ejecuta después de que la prueba termina
# 
# 4. Al final, conn.close() se asegura de cerrar la conexión a la base de datos 
# limpiamente.
# 
# En resumen, es como crear una pequeña base de datos temporal que:
# - Se crea justo antes de cada prueba
# - Se usa durante la prueba
# - Se cierra y elimina automáticamente después de la prueba
# Esto es muy útil porque nos permite probar operaciones en la base de datos sin 
# preocuparnos por afectar datos reales o tener que limpiar después de cada prueba.
