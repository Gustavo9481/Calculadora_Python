from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QSizePolicy
)

# ........................... ui_screens_creators ........................... 󰌠
# Módulo encargado de la creación de pantallas de la inetrfaz


# ------------------------------------------------------------- ScreenFactory 
class ScreenFactory:
    """
    Clase (Factoría) para crear y configurar pantallas de la interfaz.
    # pattern-> Factory
    """

    def __init__(self, style: str) -> None:
        """
        Inicializa el factoría de pantallas.

        Args:
            style (str): Estilo CSS para las pantallas
        """
        self.style = style


    def create_screen(self) -> QLabel:
        """
        Crea y configura una pantalla (QLabel) con estilo y alineación 
        especificados.

        Returns:
            QLabel: Objeto QLabel configurado con estilo y alineación
        """
        label = QLabel()
        label.setAlignment(Qt.AlignRight)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        label.setStyleSheet(self.style)
        return label


# ------------------------------------------------------------ ScreensCreator 
class ScreensCreator:
    """
    Clase para crear y gestionar las pantallas de la calculadora.

    Esta clase se encarga de crear las diferentes pantallas de 
    la calculadora:
    - Pantalla valor 1
    - Pantalla operador
    - Pantalla valor 2
    - Pantalla resultado

    Las pantallas son objetos QLabel con estilos y alineación a la derecha.

    Atributos de clase:
        style_eq (str): CSS pantallas de entrada (valor 1, operador y valor 2)
        style_res (str): CSS pantalla de resultado
    """

    # Estilos para las pantallas.
    style_eq: str = """
        QLabel {
            font-size: 20px;
            color: #A8DADC;
        }
    """

    style_res: str = """
        QLabel {
            font-size: 40px;
            color: #A8DADC;
        }
    """

    def __init__(self, main_window: QMainWindow):
        """
        Inicializa el creador de pantallas.

        Args:
            main_window (QMainWindow): Ventana principal de la aplicación
        """
        self.main_window = main_window
        self.display_value_1 = None
        self.display_operator = None
        self.display_value_2 = None
        self.display_result = None

    def create_screens(self) -> tuple:
        """
        Crea y configura todas las pantallas de la calculadora.

        Returns:
            tuple: Una tupla que contiene:
                - main_layout: Layout vertical que contiene todas las pantallas
                - display_value_1: Pantalla para mostrar el primer valor
                - display_value_2: Pantalla para mostrar el segundo valor
                - display_operator: Pantalla para mostrar el operador
                - display_result: Pantalla para mostrar el resultado
        """
        main_layout = QVBoxLayout()

        # Factorías de pantallas para diferentes estilos de pantalla.
        # note->  acá se pasa argumento style al constructor de ScreenFactory.
        eq_screen_factory = ScreenFactory(self.style_eq)
        res_screen_factory = ScreenFactory(self.style_res)


        self.display_value_1 = eq_screen_factory.create_screen()
        self.display_operator = eq_screen_factory.create_screen()
        self.display_value_2 = eq_screen_factory.create_screen()
        self.display_result = res_screen_factory.create_screen()

        # Adición de las pantallas al layout.
        for widget in [
            self.display_value_1, 
            self.display_operator, 
            self.display_value_2, 
            self.display_result
            ]:
            main_layout.addWidget(widget)

        # note-> tupla a ser desempaquetada en InterfaceCreator.
        # valores necesarios para instanciar ButtonsCreator.
        return (
            main_layout, 
            self.display_value_1, 
            self.display_value_2, 
            self.display_operator, 
            self.display_result
            )