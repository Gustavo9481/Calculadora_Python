# MODULO: ui_inteface_creator.py
"""
Módulo encargado de la creación de la interfaz gráfica de la calculadora.
Este módulo implementa el patrón Factory para crear los componentes de la UI:
- Pantallas (valores y operadores)
- Botones (números y operaciones)
- Layout principal
Uso:
    interface = InterfaceCreator()
    interface.run()
"""
# pylint: disable=E0611,E0401
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
)
from .ui_screens_creators import ScreensCreator
from .ui_buttons_creator import ButtonsCreator


# --------------------------------------------------- class -> InterfaceCreator
class InterfaceCreator:
    """
    Clase que gestiona la creación y configuración de la interfaz gráfica.
    Implementa el patrón Factory para:
    - Crear y configurar pantallas usando ScreensCreator
    - Crear y configurar botones usando ButtonsCreator
    - Organizar el layout principal de la aplicación
    Attributes:
        app (QApplication): Instancia de la aplicación Qt
        main_window (QMainWindow): Ventana principal de la aplicación
        display_value_1 (QLabel): Pantalla para el primer valor
        display_value_2 (QLabel): Pantalla para el segundo valor
        display_operator (QLabel): Pantalla para el operador
        display_result (QLabel): Pantalla para el resultado
    """
    def __init__(self) -> None:
        """
        Inicializa la interfaz gráfica.
        Este método crea la aplicación Qt y la ventana principal, y configura
        la interfaz llamando a _setup_window().
        """
        self.app = QApplication([])
        self.main_window = QMainWindow()
        self._setup_window()

    def _setup_window(self) -> None:
        """
        Configura la ventana principal y sus componentes.
        Este método:
        1. Configura propiedades básicas de la ventana (título, tamaño, estilo)
        2. Crea el widget central y su layout principal
        3. Crea y configura las pantallas usando ScreensCreator
        4. Crea y configura los botones usando ButtonsCreator
        5. Organiza el layout final de la ventana
        """
        # Configuración de la ventana principal
        self.main_window.setWindowTitle("Proyecto Calculadora Python")
        self.main_window.setGeometry(100, 100, 290, 470)
        self.main_window.setStyleSheet("background-color: #0B0E14;")

        # Creación del widget central y su layout
        central_widget = QWidget()
        central_widget.setFixedSize(290, 470)
        main_layout = QVBoxLayout(central_widget)

        # Crear y obtener las pantallas usando ScreensCreator
        screens_creator = ScreensCreator(self.main_window)

        # HACK: desempaquetado de tupla
        (screens_layout,
            self.display_value_1,
            self.display_value_2,
            self.display_operator,
            self.display_result) = screens_creator.create_screens()

        main_layout.addLayout(screens_layout)

        # Crear y obtener los botones usando ButtonsCreator
        # NOTE: uso de los valores desempaquetados de la tupla.
        buttons_creator = ButtonsCreator(
            central_widget,
            self.display_value_1,
            self.display_value_2,
            self.display_operator,
            self.display_result
        )
        buttons_layout = buttons_creator.create_buttons()
        main_layout.addLayout(buttons_layout)

        self.main_window.setCentralWidget(central_widget)

    def run(self) -> None:
        """
        Inicia la aplicación.
        Este método:
        1. Muestra la ventana principal
        2. Inicia el bucle de eventos de Qt
        3. Espera a que el usuario cierre la aplicación
        """
        self.main_window.show()
        self.app.exec_()



# NOTE: agregar las notas del desempaquetado y su funcionamiento.
"""
El patrón Factory se utiliza aquí porque:
Encapsula la lógica de creación de objetos (pantallas y botones)
Permite crear diferentes tipos de objetos (pantallas con diferentes estilos)
Centraliza la creación de objetos en clases específicas
Facilita el mantenimiento y modificación del código
Hace el código más modular y reutilizable
"""
