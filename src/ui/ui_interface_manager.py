from ui_screens_creators import ScreensCreator

# manejo de interface


class InterfaceManager:

    def __init__(self, 
                 display_value_1,
                 display_value_2,
                 display_operator,
                 display_result
    ):
        # Inicializar el estado de la calculadora
        self.display_value_1 = display_value_1  # Referencia a la pantalla de ecuación
        self.display_value_2 = display_value_2  # Referencia a la pantalla de resultado
        self.display_operator = display_operator  # Referencia a la pantalla de
        self.display_result = display_result
        self.value_1: str = ""
        self.value_2: str = ""
        self.operator: str = ""

    def insert_value(self, value: str):
        print(f"Se hizo clic en el botón: {value}")
        self.value_1 += value
        self.display_value_1.setText(self.value_1) #modifico el label

    def insert_operator(self, operator: str):
        print(f"Se hizo clic en el botón: {operator}")
        self.operator = operator
        self.display_operator.setText(self.operator)


    def clear_screen(self):
        # Lógica para borrar las pantallas
        pass

    def delete_last_character(self):
        # Lógica para borrar el último carácter de la ecuación
        pass

    def calculate_result(self):
        # Lógica para calcular el resultado de la ecuación
        pass


