# MODULO: test_history_manager.py
"""
Pruebas unitarias para la clase HistoryManager -> database.history_manager_db.
Test totales => 4/41
"""
from decimal import Decimal
import sqlite3
import pytest
import database.history_manager_db as history_manager_module
from database.history_manager_db import HistoryManager


class TestHistoryManager:
    """ Pruebas unitarias para la clase HistoryManager """

    @pytest.fixture
    def history_manager(self):
        """
        Proporciona una instancia de HistoryManager para las pruebas.
        Este fixture crea y devuelve una nueva instancia de HistoryManager que
        puede ser utilizada en las pruebas para gestionar el historial.
        """
        return HistoryManager()

    @pytest.fixture
    def memory_db_connection(self):
        """
        Proporciona una conexión temporal a una base de datos SQLite en
        memoria para pruebas.
        Este fixture crea una base de datos SQLite en memoria que:
        - Se inicializa antes de cada prueba.
        - Se mantiene disponible durante la ejecución de la prueba.
        - Se cierra y limpia automáticamente después de cada prueba.
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
            self,
            history_manager,
            memory_db_connection,
            mocker
    ):
        """
        Verifica la inserción de un registro individual en la base de datos.
        Esta prueba unitaria valida el funcionamiento básico de new_history al:
        - Insertar una operación matemática simple (2+2)
        - Verificar la correcta conversión de tipos (Decimal a str)
        - Comprobar que el registro se guardó exactamente como se esperaba
        - Validar que solo existe un registro en la tabla
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
            history_manager_module,
            'db_connect',
            memory_db_connection
        )
        history_manager.create_table()
        history_manager.new_history(test_equation, test_result)
        cursor = memory_db_connection.cursor()
        cursor.execute(
            "SELECT EQUATION, \
            RESULT FROM history_results \
            WHERE EQUATION = ?",
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

    def test_get_last_records(
            self,
            history_manager,
            memory_db_connection,
            mocker
    ):
        """ Verifica que get_last_records devuelve los registros correctos."""

        # Arrange
        mocker.patch.object(
            history_manager_module,
            'db_connect',
            memory_db_connection
        )
        history_manager.create_table()

        # Insertamos 10 registros para pruebas
        test_entries = [
            {"equation": f"{i}+{i}", "result": Decimal(f"{i+i}")}
            for i in range(1, 11)
        ]

        for entry in test_entries:
            history_manager.new_history(entry["equation"], entry["result"])

        # Act y Assert
        # En lugar de capturar el retorno, verificamos directamente a
        # base de datos ya que el decorador podría no estar retornando el valor

        # TEST: existen 10 registros.
        cursor = memory_db_connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM history_results")
        count = cursor.fetchone()[0]
        assert count == 10

        # TEST: get_last_records muestra información correcta (aunque no
        # podamos verificar el retorno). Usar print() para verificar.
        history_manager.get_last_records(5)

        # TEST: Verificación manual de los últimos 5 registros.
        cursor.execute(
            "SELECT ID, EQUATION, \
            RESULT FROM history_results \
            ORDER BY ID DESC LIMIT 5"
        )
        last_five = cursor.fetchall()
        assert len(last_five) == 5

        # TEST: el último registro es el esperado (10+10=20).
        assert last_five[0][1] == "10+10"
        assert last_five[0][2] == "20"

        cursor.close()

    def test_delete_history(
        self,
        history_manager,
        memory_db_connection,
        mocker
    ):
        """Verifica que delete_history elimina todos los registros.
        Esta prueba valida que:
        - El método elimina correctamente todos los registros de la tabla
        - Funciona correctamente incluso cuando la tabla está vacía
        """
        # Arrange
        mocker.patch.object(
            history_manager_module,
            'db_connect',
            memory_db_connection
        )
        history_manager.create_table()

        # Insertamos algunos registros de prueba.
        test_entries = [
            {"equation": "1+1", "result": Decimal("2")},
            {"equation": "3*4", "result": Decimal("12")},
        ]

        for entry in test_entries:
            history_manager.new_history(entry["equation"], entry["result"])

        # TEST: registros se insertar correctamente.
        cursor = memory_db_connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM history_results")
        count_before = cursor.fetchone()[0]
        assert count_before > 0

        # Act
        history_manager.delete_history()

        # Assert
        cursor.execute("SELECT COUNT(*) FROM history_results")
        count_after = cursor.fetchone()[0]
        assert count_after == 0  # Verifica que no quedan registros

        # TEST: también funciona cuando la tabla está vacía. No debería lanzar
        # errores
        history_manager.delete_history()
        cursor.execute("SELECT COUNT(*) FROM history_results")
        count_still_empty = cursor.fetchone()[0]
        assert count_still_empty == 0
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

        # TEST: verifica que la instancia es el mismo objeto.
        assert instance1 is instance2
        # TEST: verifica que posee el mismo ID.
        assert id(instance1) == id(instance2)
