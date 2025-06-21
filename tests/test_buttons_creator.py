# MODULO: tests/test_buttons_creator.py
"""
Tests unitarios para la clase ButtonsCreator del módulo ui_buttons_creator.py.

Estos tests se ejecutan utilizando pytest. La configuración de pytest se
encuentra en pyproject.toml.

Total tests definidos: 1 de un total esperado de 41.
"""
from src.ui.ui_buttons_creator import ButtonsCreator


# -------------------------------------------------------- class -> MockDisplay
class MockDisplay:
    """
    Mock simple para simular el comportamiento de un QLabel.

    :ivar text: Contiene el texto actual del QLabel simulado.
    :vartype text: str
    """

    def __init__(self):
        """
        Inicializa el mock con un texto vacío.
        """
        self.text = ""

    def setText(self, text: str):
        """
        Simula el método setText de QLabel, asignando el texto al atributo.

        :param text: El texto a establecer en el QLabel simulado.
        :type text: str
        """
        self.text = text


def test_insert_value():
    """
    Verifica que el método insert_value() de ButtonsCreator actualice el valor
    correctamente y modifique las pantallas simuladas (QLabels).

    Este test:
    - Crea una instancia de ButtonsCreator con objetos mock.
    - Inserta el valor "5".
    - Verifica que el estado interno y el QLabel simulado sean correctos.
    """
    # Arrange
    central_widget = None
    display_value_1 = MockDisplay()
    display_value_2 = MockDisplay()
    display_operator = MockDisplay()
    display_result = MockDisplay()
    calculator = ButtonsCreator(
        central_widget,
        display_value_1,
        display_value_2,
        display_operator,
        display_result
    )

    # Act
    calculator.insert_value("5")

    # Assert
    # TEST: Verifica el valor correcto.
    assert calculator.state.value_1 == "5"
    # TEST: Verifica actualización del mock: pantallas QLabels.
    assert display_value_1.text == "5"
