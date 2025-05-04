from decimal import Decimal
from functools import partial
from PyQt5.QtWidgets import (
    QPushButton,
    QGridLayout,
    QWidget
)
from PyQt5.QtCore import Qt
from core.calculator import Calculator
try:
    from ui_data import general_buttons_style, c_buttons_style, equal_buttons_style
except ModuleNotFoundError:
    from .ui_data import general_buttons_style, c_buttons_style, equal_buttons_style



class ButtonsCreator:
    """
    Clase para crear y gestionar los botones de la calculadora.
    """
    def __init__(self, central_widget,  display_value_1, display_value_2, display_operator, display_result):
        """
        Constructor de la clase ButtonsCreator.

        Args:
            central_widget (QWidget): Widget central donde se colocarán los botones.
            display_value_1 (QLabel): Label para mostrar el primer valor.
            display_value_2 (QLabel): Label para mostrar el segundo valor.
            display_operator (QLabel): Label para mostrar el operador.
            display_result (QLabel): Label para mostrar el resultado.
        """
        self.central_widget = central_widget
        self.buttons = {}
        self.display_value_1 = display_value_1
        self.display_value_2 = display_value_2
        self.display_operator = display_operator
        self.display_result = display_result
        self.value_1 = ""
        self.value_2 = ""
        self.current_operator = ""

    def create_buttons(self):
        """
        Crea los botones de la calculadora y establece la conexión con las funciones correspondientes.

        Returns:
            QGridLayout: Layout que contiene los botones.
        """
        buttons_layout = QGridLayout()

        button_data = [
            ("󰯲", 0, 0, c_buttons_style, "C", self.clear_screen),
            ("%", 0, 1, general_buttons_style, "%", self.insert_operator),
            ("", 0, 2, general_buttons_style, "D", self.delete_last_character),
            ("󰇔", 0, 3, general_buttons_style, "/", self.insert_operator),
            ("7", 1, 0, general_buttons_style, "7", self.insert_value),
            ("8", 1, 1, general_buttons_style, "8", self.insert_value),
            ("9", 1, 2, general_buttons_style, "9", self.insert_value),
            ("", 1, 3, general_buttons_style, "*", self.insert_operator),
            ("4", 2, 0, general_buttons_style, "4", self.insert_value),
            ("5", 2, 1, general_buttons_style, "5", self.insert_value),
            ("6", 2, 2, general_buttons_style, "6", self.insert_value),
            ("", 2, 3, general_buttons_style, "-", self.insert_operator),
            ("1", 3, 0, general_buttons_style, "1", self.insert_value),
            ("2", 3, 1, general_buttons_style, "2", self.insert_value),
            ("3", 3, 2, general_buttons_style, "3", self.insert_value),
            ("", 3, 3, general_buttons_style, "+", self.insert_operator),
            ("󰔎", 4, 0, general_buttons_style, "T", self.insert_operator),
            ("0", 4, 1, general_buttons_style, "0", self.insert_value),
            (".", 4, 2, general_buttons_style, ".", self.insert_value),
            (" ", 4, 3, equal_buttons_style, "=", self.calculate_result),
        ]

        for text, row, column, style, value, func in button_data:
            button = QPushButton(text)
            button.setParent(self.central_widget)
            button.setStyleSheet(style)
            buttons_layout.addWidget(button, row, column)
            self.buttons[text] = button
            button.clicked.connect(partial(func, value))
        return buttons_layout

    def get_buttons(self):
        """
        Obtiene el diccionario de botones creados.

        Returns:
            dict: Diccionario donde las claves son los textos de los botones
                  y los valores son los objetos QPushButton correspondientes.
        """
        return self.buttons

    def insert_value(self, value):
        """Inserta un número en la pantalla."""
        if self.current_operator == "":
            self.value_1 += value
            self.display_value_1.setText(self.value_1)
        else:
            self.value_2 += value
            self.display_value_2.setText(self.value_2)

    def insert_operator(self, operator):
        """Inserta un operador."""
        if self.value_1 != "" and self.value_2 == "":
            self.current_operator = operator
            self.display_operator.setText(self.current_operator)
        elif self.value_1 != "" and self.value_2 != "":
            self.calculate_result("=")
            self.current_operator = operator
            self.display_operator.setText(self.current_operator)

    def clear_screen(self, value):
        """Limpia las pantallas."""
        self.display_value_1.clear()
        self.display_value_2.clear()
        self.display_operator.clear()
        self.display_result.clear()
        self.value_1 = ""
        self.value_2 = ""
        self.current_operator = ""

    def delete_last_character(self, value):
        """Borra el último carácter de la entrada actual."""
        if self.current_operator == "":
            self.value_1 = self.value_1[:-1]
            self.display_value_1.setText(self.value_1)
        else:
            self.value_2 = self.value_2[:-1]
            self.display_value_2.setText(self.value_2)

    def calculate_result(self, value):
        """Realiza el cálculo y muestra el resultado."""
        
        if "" not in (self.value_1, self.value_2, self.current_operator):

            try:

                calculator = Calculator()

                num1, num2 = Decimal(self.value_1), Decimal(self.value_2)
                operations: dict = {
                "+": calculator.add,
                "-": calculator.subtract,
                "*": calculator.multiply,
                "/": calculator.divide,
                "%": calculator.percent
                }

                if self.current_operator in operations:
                    result = operations[self.current_operator](num1, num2)
                    self.display_result.setText(str(result))
                    self.value_1 = str(result)
                    self.value_2 = ""
                    self.current_operator = ""
                else:
                    self.display_result.setText("Error: Invalid Operator")

            except Exception as e:
                self.display_result.setText(f"Error: {e}")
                self.value_1 = ""
                self.value_2 = ""
                self.current_operator = ""

