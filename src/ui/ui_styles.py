# MODULO: ui_styles.py
"""
Almacena las variables de los estilos CSS para los elementos de la interfaz:
    - Pantallas (QLabel)
    - Botones (QPushButton)
"""

# ---------------------------------------------------- Estilos de las pantallas
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

# ---------------------------------------------------------- Estilos de botones

# Estilos para botones generales
general_buttons_style: str = """
    QPushButton {
        background-color: #12151B;
        color: #A8DADC;
        height: 50px;
        border: none;
        border-radius: 10px;
        font-size: 17px;
    }
    QPushButton:pressed {
        background-color: #0B0E14;
        color: #A8DADC;
        height: 50px;
        border: none;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
    }
"""

# Estilos para botón de borrar de signo "󰯲"
c_buttons_style: str = """
    QPushButton {
        background-color: #12151B;
        color: #E63946;
        font-weight: bold;
        height: 50px;
        border: none;
        border-radius: 10px;
        font-size: 25px;
    }
    QPushButton:pressed {
        background-color: #0B0E14;
        color: #E63946;
        font-weight: bold;
        height: 50px;
        border: none;
        border-radius: 10px;
        font-size: 28px;
        font-weight: bold;
    }
"""

# Estilos para botón de igual "="
equal_buttons_style: str = """
    QPushButton {
        background-color: #E63946;
        color: #A8DADC;
        height: 50px;
        border: none;
        border-radius: 10px;
        font-size: 17px;
    }
    QPushButton:pressed {
        background-color: #0B0E14;
        color: #A8DADC;
        height: 50px;
        border: none;
        border-radius: 10px;
        font-size: 17px;
        font-weight: bold;
    }
"""
