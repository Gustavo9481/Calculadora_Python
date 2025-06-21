# Clase **ButtonsCreator**

## Propósito y Responsabilidad

La clase ButtonsCreator se encarga de construir, organizar y conectar los botones de una calculadora en una interfaz gráfica desarrollada con PyQt5. Representa la lógica de presentación y control asociada a los eventos que ocurren cuando un usuario interactúa con la interfaz (por ejemplo, al presionar botones numéricos u operadores).

### Características principales

- Gestión visual de botones: Crea dinámicamente los botones en un layout de tipo QGridLayout y los coloca dentro del widget central de la interfaz.

- Conexión de eventos: Cada botón queda vinculado a una función interna que determina su comportamiento al ser presionado (insert_value, calculate_result, etc.).

- Manipulación del estado: Actualiza internamente el estado de la calculadora a través de un modelo llamado CalculatorState.

- Integración con base de datos: Almacena el resultado de cada operación utilizando la clase HistoryManager, que sigue el patrón Singleton.

- Soporte para temas: Permite alternar entre modos de color (por ahora solo cambia un valor de control interno: "dark"/"light").

### Patrón de Diseño aplicado

ButtonsCreator aplica el patrón Factory Method indirectamente, al encargarse de la creación dinámica de botones dentro del método create_buttons. También puede verse como una implementación parcial del patrón MVC, donde esta clase actúa como "Controlador + Vista" para los botones.

### Implementación del patrón
```python
def create_buttons(self) -> QGridLayout:
    button_data = [
        ("7", 1, 0, general_buttons_style, "7", self.insert_value),
        # ...
    ]

    for text, row, col, style, value, func in button_data:
        button = QPushButton(text)
        button.setParent(self.central_widget)
        button.setStyleSheet(style)
        self.buttons[text] = button
        button.clicked.connect(partial(func, value))
```

#### Por qué este patrón y sus ventajas

- **Desacoplamiento**: Se separa la definición de cada botón de su creación, lo cual facilita su modificación o extensión sin cambiar el resto de la lógica.
    
- **Claridad**: Agrupar la definición de botones en una estructura (`button_data`) mejora la legibilidad del código.
    
- **Escalabilidad**: Añadir nuevos botones es tan simple como agregar una tupla más al array `button_data`

---
## Diagrama UML
![ButtonsCreator UML - Diagrama de clase](./clases_uml/uml_buttons_creator.svg)

---
## Métodos principales

```python
+ __init__(central_widget, display_value_1, display_value_2, display_operator, display_result)
+ create_buttons() -> QGridLayout
+ get_buttons() -> dict
+ insert_value(value: str) -> None
+ insert_operator(operator: str) -> None
+ clear_screen(value: str) -> None
+ delete_last_char(value: str) -> None
+ calculate_result(value: str) -> None
+ theme_toggle(*args, **kwargs) -> str
```

### Descripción de métodos clave

- `create_buttons()`  
    Crea y organiza los botones en la interfaz, conectándolos con su función respectiva.
    
- `insert_value(value)`  
    Añade un número o punto decimal al valor que el usuario está introduciendo.
    
- `insert_operator(operator)`  
    Registra el operador aritmético actual y, si corresponde, realiza un cálculo inmediato.
    
- `calculate_result(value)`  
    Ejecuta el cálculo utilizando `Decimal` y delega el almacenamiento del resultado a `HistoryManager`.
    
- `theme_toggle()`  
    Alterna entre dos temas visuales predefinidos (solo actualiza el estado actual del tema).
    

---

## Dependencias

|                                            |                                                               |     |
| ------------------------------------------ | ------------------------------------------------------------- | --- |
| Python                                     | versión igual mayor a python3.7                               |     |
| PyQT5                                      | Widgets: `QPushButton, QGridLayout, QLabel, QWidget`          |     |
| decimal                                    | Precisión de los resultados usando `Decimal`                  |     |
| pydantic                                   | Para las clases auxiliares `CalculatorState` y `ButtonData`   |     |
| core.calculator.Calculator                 | Proporciona métodos matemáticos para realizar las operaciones |     |
| database.history_manager_db.HistoryManager | Guarda cada operación matemática en la base de datos SQLite   |     |

---
## Relaciones

    
|                                              |                                                                                                  |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| CalculatorState                              | Modelo interno que gestiona los valores de entrada, el operador actual y el resultado calculado. |
| HistoryManager                               | Clase Singleton que persiste en base de datos el historial de operaciones matemáticas.           |
| QPushButton / QLabel / QGridLayout / QWidget | Widgets de PyQt5 usados para construir y actualizar la interfaz visual.                          |

---
## Ejemplo de uso

```python
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from ui_buttons_creator import ButtonsCreator

app = QApplication([])

# Crear elementos simulados
central = QWidget()
val1 = QLabel()
val2 = QLabel()
op = QLabel()
res = QLabel()

# Instanciar clase creadora de botones
creator = ButtonsCreator(central, val1, val2, op, res)

# Crear y obtener layout con botones
layout = creator.create_buttons()

# Mostrar el widget (en una app real)
central.setLayout(layout)
central.show()

app.exec_()
```

### Explicación del ejemplo

1. **Inicialización de PyQt5**  
    Se crea una aplicación Qt estándar con widgets simulados para mostrar los valores de la calculadora.
    
2. **Instanciación de `ButtonsCreator`**  
    Se pasa el widget principal (`central`) y las etiquetas (`QLabel`) que mostrarán los valores.
    
3. **Creación de botones**  
    Se invoca `create_buttons()` para generar el layout completo con los botones conectados.
    
4. **Renderizado**  
    El layout generado se asigna al widget central y se muestra en pantalla usando `.show()` y `exec_()`.
