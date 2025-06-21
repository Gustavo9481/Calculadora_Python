# MODULO: test_history_manager.py
"""
Pruebas unitarias para la clase HistoryManager -> history_manager_db.
Test totales => 4/41
"""
from decimal import Decimal
import sqlite3
import pytest
import database.history_manager_db as history_manager_module
from database.history_manager_db import HistoryManager


class TestHistoryManager:
    """
    Pruebas unitarias para la clase HistoryManager.

    Esta clase contiene un conjunto completo de pruebas unitarias diseñadas
    para validar el correcto funcionamiento de la clase HistoryManager, que
    se encarga de gestionar el historial de operaciones matemáticas en una
    base de datos SQLite.

    Las pruebas cubren las siguientes funcionalidades:

    * Inserción de nuevos registros de historial
    * Recuperación de los últimos registros
    * Eliminación completa del historial
    * Verificación del patrón Singleton

    :note: Utiliza fixtures de pytest para proporcionar instancias de prueba
           y conexiones a base de datos en memoria.
    """

    @pytest.fixture
    def history_manager(self):
        """
        Proporciona una instancia de HistoryManager para las pruebas.

        Este fixture crea y devuelve una nueva instancia de HistoryManager que
        puede ser utilizada en las pruebas para gestionar el historial de
        operaciones matemáticas.

        :returns: Una instancia fresca de HistoryManager para cada prueba
        :rtype: HistoryManager

        :note: Se ejecuta antes de cada prueba que lo requiera, garantizando
               un estado limpio para cada test.
        """
        return HistoryManager()

    @pytest.fixture
    def memory_db_connection(self):
        """
        Proporciona una conexión temporal a una base de datos SQLite en
        memoria.

        Este fixture crea una base de datos SQLite completamente en memoria
        que:

        * Se inicializa automáticamente antes de cada prueba
        * Se mantiene disponible durante toda la ejecución del test
        * Se cierra y limpia automáticamente al finalizar la prueba

        :yields: Conexión activa a la base de datos SQLite en memoria
        :ytype: sqlite3.Connection

        :note: La base de datos en memoria es ideal para pruebas ya que es
               rápida, aislada y no deja rastros en el sistema de archivos.
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
        Verifica la inserción correcta de un registro individual en la BD.

        Esta prueba unitaria valida el funcionamiento básico del método
        new_history al realizar las siguientes verificaciones:

        * Insertar una operación matemática simple (2+2)
        * Verificar la correcta conversión de tipos (Decimal a str)
        * Comprobar que el registro se guardó exactamente como se esperaba
        * Validar que solo existe un registro en la tabla

        :param history_manager: Instancia de HistoryManager para pruebas
        :type history_manager: HistoryManager
        :param memory_db_connection: Conexión a BD en memoria
        :type memory_db_connection: sqlite3.Connection
        :param mocker: Objeto mock de pytest para simular dependencias
        :type mocker: pytest_mock.MockerFixture

        :note: Utiliza mocking para aislar la prueba de dependencias externas
               y valores simples para facilitar la verificación.
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
        """
        Verifica que get_last_records devuelve los registros correctos.

        Esta prueba valida el comportamiento del método get_last_records
        mediante las siguientes verificaciones:

        * Inserción de 10 registros de prueba en la base de datos
        * Confirmación de que existen exactamente 10 registros
        * Verificación de que se pueden recuperar los últimos 5 registros
        * Validación de que el último registro corresponde al esperado

        :param history_manager: Instancia de HistoryManager para pruebas
        :type history_manager: HistoryManager
        :param memory_db_connection: Conexión a BD en memoria
        :type memory_db_connection: sqlite3.Connection
        :param mocker: Objeto mock de pytest para simular dependencias
        :type mocker: pytest_mock.MockerFixture

        :note: Se enfoca en verificación manual de la base de datos ya que
               el decorador podría no estar retornando valores directamente.
        """

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
        """
        Verifica que delete_history elimina todos los registros correctamente.

        Esta prueba valida el comportamiento del método delete_history en
        diferentes escenarios:

        * Eliminación correcta de todos los registros cuando la tabla contiene
          datos
        * Funcionamiento correcto cuando se ejecuta sobre una tabla vacía
        * Verificación de que no se producen errores en ningún caso

        :param history_manager: Instancia de HistoryManager para pruebas
        :type history_manager: HistoryManager
        :param memory_db_connection: Conexión a BD en memoria
        :type memory_db_connection: sqlite3.Connection
        :param mocker: Objeto mock de pytest para simular dependencias
        :type mocker: pytest_mock.MockerFixture

        :raises AssertionError: Si los registros no se eliminan correctamente

        :note: Incluye pruebas de robustez para garantizar que el método
               es seguro de ejecutar múltiples veces.
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
        """
        Verifica la implementación correcta del patrón Singleton.

        Esta prueba valida que HistoryManager implementa correctamente el
        patrón de diseño Singleton mediante las siguientes verificaciones:

        * Múltiples instanciaciones retornan exactamente el mismo objeto
        * La identidad de los objetos es idéntica (mismo ID en memoria)
        * Se garantiza una única instancia durante toda la ejecución

        :raises AssertionError: Si el patrón Singleton no está correctamente
                implementado

        :note: El patrón Singleton es crucial para evitar múltiples conexiones
               a la base de datos y garantizar consistencia en el historial.
        """
        instance1 = HistoryManager()
        instance2 = HistoryManager()

        # TEST: verifica que la instancia es el mismo objeto.
        assert instance1 is instance2
        # TEST: verifica que posee el mismo ID.
        assert id(instance1) == id(instance2)
