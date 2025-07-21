# MODULO: test_history_manager.py
"""
Pruebas unitarias para la clase HistoryManager -> history_manager_db.
Test totales => 4/41
"""
from decimal import Decimal
import pytest
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
    def history_manager(self, mocker):
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
        # Configura el mock para usar una base de datos en memoria
        mocker.patch.object(HistoryManager, '_db_path', ':memory:')
        # Crea una nueva instancia para cada prueba para asegurar aislamiento
        # Esto requiere resetear el singleton de alguna manera o instanciar una clase base
        # Para simplificar, vamos a re-instanciar, asumiendo que el estado no persiste entre tests
        # de una manera que los afecte negativamente gracias a la BD en memoria.
        HistoryManager._instance = None  # Forza la re-creación del singleton
        manager = HistoryManager()
        manager.create_table()  # Asegura que la tabla exista
        return manager

    def test_new_history_inserts_data(
            self,
            history_manager
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

        :note: Utiliza mocking para aislar la prueba de dependencias externas
               y valores simples para facilitar la verificación.
        """
        test_equation = "2+2"
        test_result = Decimal("4")
        
        history_manager.new_history(test_equation, test_result)
        
        records = history_manager.get_last_records(1)
        
        assert len(records) == 1
        assert records[0]['equation'] == test_equation
        assert records[0]['result'] == str(test_result)

    def test_get_last_records(
            self,
            history_manager
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

        :note: Se enfoca en verificación manual de la base de datos ya que
               el decorador podría no estar retornando valores directamente.
        """

        # Insertamos 10 registros para pruebas
        for i in range(1, 11):
            history_manager.new_history(f"{i}+{i}", Decimal(f"{i+i}"))

        # TEST: existen 10 registros.
        all_records = history_manager.get_last_records(10)
        assert len(all_records) == 10

        # TEST: get_last_records muestra información correcta.
        last_five = history_manager.get_last_records(5)
        assert len(last_five) == 5

        # TEST: el último registro es el esperado (10+10=20).
        assert last_five[0]['equation'] == "10+10"
        assert last_five[0]['result'] == "20"

    def test_delete_history(
        self,
        history_manager
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

        :raises AssertionError: Si los registros no se eliminan correctamente

        :note: Incluye pruebas de robustez para garantizar que el método
               es seguro de ejecutar múltiples veces.
        """
        # Insertamos algunos registros de prueba.
        history_manager.new_history("1+1", Decimal("2"))
        history_manager.new_history("3*4", Decimal("12"))

        # TEST: registros se insertar correctamente.
        records_before = history_manager.get_last_records(10)
        assert len(records_before) > 0

        # Act
        history_manager.delete_history()

        # Assert
        records_after = history_manager.get_last_records(10)
        assert len(records_after) == 0  # Verifica que no quedan registros

        # TEST: también funciona cuando la tabla está vacía. No debería lanzar
        # errores
        history_manager.delete_history()
        records_still_empty = history_manager.get_last_records(10)
        assert len(records_still_empty) == 0

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
        HistoryManager._instance = None # Resetea para la prueba
        instance1 = HistoryManager()
        instance2 = HistoryManager()

        # TEST: verifica que la instancia es el mismo objeto.
        assert instance1 is instance2
        # TEST: verifica que posee el mismo ID.
        assert id(instance1) == id(instance2)
