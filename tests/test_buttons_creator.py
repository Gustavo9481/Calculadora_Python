import pytest
from src.ui.ui_buttons_creator import ButtonsCreator

class MockDisplay:
    """
    Un mock simple para simular el comportamiento de un QLabel.
    """
    def __init__(self):
        self.text = ""

    def setText(self, text):
        self.text = text

def test_insert_value():
    """
    Verifica que el método insert_value() actualice el valor correctamente.
    """
    # Arrange
    central_widget = None  # No necesitamos un widget central para este test
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
    assert calculator.state.value_1 == "5"
    assert display_value_1.text == "5"  # Verifica que el mock se haya actualizado
