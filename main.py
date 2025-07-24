# ....................... PROYECTO CALCULADORA PYTHON ....................... 󰌠
# MODULO: main.py -> módulo de inicio.
"""
Calculadora en python para escritorio, desarrollado para el repaso de conceptos
básicos como:

- Patrones de diseño.
- Testing unitario.
- Interfaces Gráficas PyQt.
- Documentación y formato de código con pylint y flake8.
- Modularización del proyecto y uso de módulos externos.
"""
from src.ui.ui_interface_creator import InterfaceCreator
from src.database.history_manager_db import HistoryManager


class AppCalculator:
    """
    Clase principal que inicia y gestiona la aplicación de la calculadora.

    Esta clase actúa como punto de entrada principal de la aplicación,
    inicializando interfaz gráfica y base de datos, gestionando su ejecución.
    Implementa un patrón de diseño simple con una única responsabilidad:
    iniciar la aplicación.

    :Attributes:
        interface (InterfaceCreator): Instancia de la interfaz gráfica de la
            calculadora.
        history_db (HistoryManager): Instancia del gestor de la base de datos 
            del historial.

    :Example:
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
        valor, su única responsabilidad es iniciar la ejecución de la interfaz
        gráfica y base de datos.

        :returns: None
        :rtype: None
        """
        self.history_db.create_table()
        self.interface.run()


if __name__ == "__main__":
    app = AppCalculator()
    app.main()
