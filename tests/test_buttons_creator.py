# MODULO: tests/test_buttons_creator.py
""" Tests unitarios para la clase ButtonsCreator. -> ui_buttons_creator.py
Tests unitarios ejecutados a través de pytest. Config -> pyproject.toml.
Total tests => 1/41
"""
from src.ui.ui_buttons_creator import ButtonsCreator


# -------------------------------------------------------- class -> MockDisplay
class MockDisplay:
    """ Mock simple para simular el comportamiento de un QLabel """

    def __init__(self):
        self.text = ""

    def setText(self, text: str):
        """ Simula el método setText de QLabel estableciendo el texto.
        Args:
            text (str): El texto a establecer
        """
        self.text = text


def test_insert_value():
    """ Verifica que el método insert_value() actualice el valor correctamente
    y las pantallas QLabels.
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
