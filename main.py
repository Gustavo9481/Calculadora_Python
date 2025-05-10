# ....................... PROYECTO CALCULADORA PYTHON ....................... 󰌠
# MODULO: main.py -> módulo de inicio.
"""
Calculadora en python para escritorio, desarrollado para el repaso de
conceptos básicos como:
* Patrones de diseño.
* Testing unitario.
* Interfaces Gráficas PyQt.
* Documentación y formato de código con pylint y flake8.
* Modularización del proyecto y uso de módulos externos
"""
# pylint: disable=E0401
from src.ui.ui_interface_creator import InterfaceCreator
from src.database.history_manager_db import HistoryManager

# pylint: disable=R0903
class AppCalculator:
    """
    Clase principal que inicia y gestiona la aplicación de la calculadora.

    Esta clase actúa como punto de entrada principal de la aplicación,
    inicializando la interfaz gráfica y gestionando su ejecución. Implementa
    un patrón de diseño simple con una única responsabilidad: iniciar la
    aplicación.

    Attributes:
        interface (InterfaceCreator): Instancia de la interfaz gráfica
            de la calculadora.

    Example:
        Para iniciar la aplicación:
        >>> app = AppCalculator()
        >>> app.main()
    """

    interface = InterfaceCreator()
    history_db = HistoryManager()

    def main(self) -> None:
        """
        Método principal que inicia la ejecución de la aplicación.

        Este método es el punto de entrada principal que inicia la interfaz
        gráfica de la calculadora. No recibe parámetros y no retorna ningún
        valor, su única responsabilidad es iniciar la ejecución de la
        interfaz gráfica.

        Returns:
            None
        """
        self.interface.run()
        self.history_db.create_table()


if __name__ == "__main__":
    app = AppCalculator()
    app.main()