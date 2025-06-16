# MODULO: ui_themes_colors.py
# WARN: módulo no implementado
"""
Contenedor de colores para los temas de la interfaz
Temas dark y light.
"""
from collections import namedtuple


ColorTheme = namedtuple("ColorTheme",
                        ["background", "foreground", "button_1", "button_2"])

dark_theme = ColorTheme(
    background="#000",
    foreground="#fff",
    button_1="#000fff",
    button_2="#fff000"
)

light_theme = ColorTheme(
    background="#fff",
    foreground="#000",
    button_1="#000fff",
    button_2="#fff000"
)
