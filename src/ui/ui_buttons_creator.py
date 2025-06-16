# MODULO: ui_buttons_creator.py
"""
Crea los botones de la interfaz y sus métodos al ser presionados a través
de la clase ButtonsCreator, empleando un patrón de diseño de factory method.
"""
from decimal import Decimal
from functools import partial
from typing import Dict
from pydantic import BaseModel, Field
from PyQt5.QtWidgets import QPushButton, QGridLayout
from core.calculator import Calculator
from database.history_manager_db import HistoryManager

try:
    from ui_styles import (
        general_buttons_style, c_buttons_style, equal_buttons_style
    )
except ModuleNotFoundError:
    from .ui_styles import (
        general_buttons_style, c_buttons_style, equal_buttons_style
    )


# .. .................................................. class -> ButtonData ..󰌠
class ButtonData(BaseModel):
    """
    Modelo para validar los datos de un botón.

    :ivar text: Texto que muestra el botón en interfaz.
    :ivar value: Valor que posee el botón.
    :ivar style: Variable con estilos para el botón.
    :ivar row: Fila ubicación de botón.
    :ivar column: Columna ubicación de botón.
    :ivar func: Función que desencadena el botón.
    """
    text: str = Field(description="texto que muestra el botón en interfaz")
    value: str = Field(description="valor que posee el botón")
    style: str = Field(description="variable con estilos para el botón")
    row: int = Field(ge=0, lt=5, description="fila ubicación de botón")
    column: int = Field(ge=0, lt=4, description="columna ubicación de botón")
    func: str = Field(description="función que desencadena el botón")


# .. ............................................. class -> CalculatorState ..󰌠
class CalculatorState(BaseModel):
    """
    Modelo para validar el estado de la calculadora.

    :ivar value_1: 1° valor de la ecuación.
    :ivar value_2: 2° valor de la ecuación.
    :ivar current_operator: Operador actual.
    :ivar result: Almacén de resultado.
    """
    value_1: str = Field(default="", description="1° valor de la ecuación")
    value_2: str = Field(default="", description="2° valor de la ecuación")
    current_operator: str = Field(default="", description="operador actual")
    result: str = Field(default="", description="almacén de resultado")


# .. .............................................. class -> ButtonsCreator ..󰌠
class ButtonsCreator:
    """
    Clase para crear y gestionar los botones de la calculadora.

    :ivar central_widget: Widget central donde estarán los botones.
    :ivar display_value_1: Label para mostrar el primer valor.
    :ivar display_value_2: Label para mostrar el segundo valor.
    :ivar display_operator: Label para mostrar el operador.
    :ivar display_result: Label para mostrar el resultado.
    :ivar state: Estado actual de la calculadora.
    :ivar buttons: Diccionario de botones creados.
    :ivar history_manager: Instancia de HistoryManager para gestión de
        registros en base de datos.
    """

    def __init__(
        self,
        central_widget,
        display_value_1,
        display_value_2,
        display_operator,
        display_result,
    ):
        """
        Constructor de la clase ButtonsCreator.

        :param central_widget: Widget central donde estarán los botones.
        :param display_value_1: Label para mostrar el primer valor.
        :param display_value_2: Label para mostrar el segundo valor.
        :param display_operator: Label para mostrar el operador.
        :param display_result: Label para mostrar el resultado.
        """
        self.central_widget = central_widget
        self.display_value_1 = display_value_1
        self.display_value_2 = display_value_2
        self.display_operator = display_operator
        self.display_result = display_result
        self.state = CalculatorState()
        self.buttons: Dict[str, QPushButton] = {}
        self.history_manager = HistoryManager()
        self.current_theme = "dark"

    def create_buttons(self) -> QGridLayout:
        """
        Crea los botones de la calculadora y establece la conexión con las
        funciones correspondientes.

        :returns: Layout que contiene los botones.
        :rtype: QGridLayout
        """
        buttons_layout = QGridLayout()

        button_data = [
            ("󰯲", 0, 0, c_buttons_style, "C", self.clear_screen),
            ("%", 0, 1, general_buttons_style, "%", self.insert_operator),
            ("", 0, 2, general_buttons_style, "D", self.delete_last_char),
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
            ("󰔎", 4, 0, general_buttons_style, "T", self.theme_toggle),
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

    def get_buttons(self) -> dict:
        """
        Obtiene el diccionario de botones creados.

        :returns: Diccionario donde las claves son los textos de los botones y
            los valores son los objetos QPushButton correspondientes.
        :rtype: dict
        """
        return self.buttons

    def insert_value(self, value: str) -> None:
        """
        Inserta un valor numérico o un punto decimal en la pantalla.
        Solo permite un punto decimal por número.

        :param value: Valor numérico o punto a insertar.
        :type value: str
        """
        # Validar punto decimal
        if value == ".":
            if self.state.current_operator == "":
                # Verificar si ya existe un punto en value_1
                if self.state.value_1.count(".") > 0:
                    return
            else:
                # Verificar si ya existe un punto en value_2
                if self.state.value_2.count(".") > 0:
                    return

        # Insertar el valor si es válido
        if self.state.current_operator == "":
            self.state.value_1 += value
            self.display_value_1.setText(self.state.value_1)
        else:
            self.state.value_2 += value
            self.display_value_2.setText(self.state.value_2)

    def insert_operator(self, operator: str) -> None:
        """
        Inserta un operador en la pantalla correspondiente.

        :param operator: Operador correspondiente a la ecuación.
        :type operator: str
        """
        if self.state.value_1 != "" and self.state.value_2 == "":
            self.state.current_operator = operator
            self.display_operator.setText(self.state.current_operator)

        elif self.state.value_1 != "" and self.state.value_2 != "":
            self.calculate_result("=")
            self.display_value_1.setText(str(self.state.result))
            self.state.current_operator = operator
            self.display_operator.setText(self.state.current_operator)
            self.state = CalculatorState(value_1=str(self.state.result))
            self.state.value_1 = str(self.display_value_1.text())
            self.state.current_operator = str(self.display_operator.text())
            self.display_value_2.clear()
            self.display_result.clear()

    def clear_screen(self, vlaue: str) -> None:
        """
        Limpia las pantallas al presionar botón C.

        :param vlaue: No se utiliza, se mantiene por compatibilidad con la
            señal.
        :type vlaue: str
        """
        self.display_value_1.clear()
        self.display_value_2.clear()
        self.display_operator.clear()
        self.display_result.clear()
        self.state = CalculatorState()

    def delete_last_char(self, value: str) -> None:
        """
        Borra el último carácter de la entrada actual al presionar <-

        :param value: No se utiliza, se mantiene por compatibilidad con la
            señal.
        :type value: str
        """
        if self.state.current_operator == "":
            self.state.value_1 = self.state.value_1[:-1]
            self.display_value_1.setText(self.state.value_1)
        else:
            self.state.value_2 = self.state.value_2[:-1]
            self.display_value_2.setText(self.state.value_2)

    def calculate_result(self, value: str) -> None:
        """
        Convierte los valores a tipo Decimal, realiza el cálculo
        correspondiente al operador y muestra el resultado.
        Crea un nuevo registro en la base de datos con la ecuación y el
        resultado usando la clase HistoryManager (Singleton).

        :param value: No se utiliza, se mantiene por compatibilidad con la
            señal.
        :type value: str
        """
        if "" not in (
            self.state.value_1,
            self.state.value_2,
            self.state.current_operator,
        ):
            try:
                calculator = Calculator()
                num1 = Decimal(self.state.value_1)
                num2 = Decimal(self.state.value_2)
                operations: dict = {
                    "+": calculator.add,
                    "-": calculator.subtract,
                    "*": calculator.multiply,
                    "/": calculator.divide,
                    "%": calculator.percent,
                }

                if self.state.current_operator in operations:
                    op = self.state.current_operator
                    self.state.result = operations[op](num1, num2)
                    self.state.result = self.state.result.quantize(
                        Decimal("0.00"))
                    self.display_result.setText(str(self.state.result))
                    equation: str = f"{num1} {
                        str(self.state.current_operator)} {num2}"
                    self.history_manager.new_history(
                        equation, Decimal(self.state.result)
                    )

                else:
                    self.display_result.setText("Error: Invalid Operator")
                    self.state = CalculatorState()

            except Exception as e:
                self.display_result.setText(f"Error: {e}")
                self.state = CalculatorState()

    # TODO: método por desarrollar. Función futura para cambiar tema.
    def theme_toggle(self, *args, **kwargs):
        """
        Alterna entre los dos temas de la app [dark | light].

        :return: El nuevo tema aplicado.
        :rtype: str
        """
        if self.current_theme == "dark":
            self.current_theme = "light"
        else:
            self.current_theme = "dark"

        print(self.current_theme)
        return self.current_theme
