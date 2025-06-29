# Clase **ScreensCreator**

## Propósito y Responsabilidad

La clase `ScreensCreator` se encarga de construir y organizar las pantallas visuales de una calculadora (inputs, operador y resultado) utilizando PyQt5. Es responsable de mostrar los datos introducidos por el usuario y los resultados de las operaciones, mediante widgets `QLabel` con estilos personalizados.

### Características principales

- **Creación de pantallas**: Utiliza el patrón Factory para crear instancias de `QLabel` con estilos definidos previamente (ecuaciones y resultados).

- **Organización visual**: Inserta las pantallas en un layout vertical (`QVBoxLayout`) que puede integrarse fácilmente en la interfaz principal.

- **Gestión del estado visual**: Asocia internamente un modelo `ScreenState` que mantiene los valores mostrados por cada pantalla (`valor 1`, `valor 2`, `operador`, `resultado`).

### Patrón de Diseño aplicado

`ScreensCreator` implementa el patrón **Factory** de forma indirecta a través del uso de la clase auxiliar `ScreenFactory`, encargada de encapsular la lógica de creación de `QLabel` con configuración visual específica.

### Implementación del patrón
```python
eq_screen_factory = ScreenFactory(self.style_eq)
res_screen_factory = ScreenFactory(self.style_res)

self.display_value_1 = eq_screen_factory.create_screen()
self.display_operator = eq_screen_factory.create_screen()
self.display_value_2 = eq_screen_factory.create_screen()
self.display_result = res_screen_factory.create_screen()
```

#### Por qué este patrón y sus ventajas

- **Reutilización**: Permite crear múltiples pantallas con configuración homogénea sin duplicar código.
    
- **Flexibilidad**: La clase `ScreenFactory` centraliza las decisiones visuales (estilo, alineación), facilitando ajustes futuros.
    
- **Simplicidad**: Se reduce la complejidad del constructor de `ScreensCreator` al delegar la creación visual a una clase especializada.
    
---

## Diagrama UML

<figure markdown="span">
  ![ScreensCreator - UML](./clases_uml/uml_screen_creator.svg){ width="500" }
  <figcaption>Clase ScreensCreator</figcaption>
</figure>

---

## Métodos principales

python

CopiarEditar

`+ __init__(main_window: QMainWindow) + create_screens() -> tuple`

### Descripción de métodos clave

- `create_screens()`  
    Crea las cuatro pantallas necesarias para la calculadora (`valor 1`, `valor 2`, `operador`, `resultado`) y las organiza en un layout vertical (`QVBoxLayout`). Devuelve una tupla con el layout y las referencias a cada pantalla individual.
    

---

## Dependencias

|           |                                                  |
| --------- | ------------------------------------------------ |
| Python    | versión igual o mayor a 3.7                      |
| PyQt5     | Widgets: `QLabel`, `QVBoxLayout`, `QMainWindow`  |
| Pydantic  | Para validar y estructurar datos con `BaseModel` |
| ui_styles | Define los estilos `style_eq` y `style_res`      |

---

## Relaciones

|                 |                                                                          |
| --------------- | ------------------------------------------------------------------------ |
| `ScreenConfig`  | Clase auxiliar que define el estilo, alineación y política de tamaño.    |
| `ScreenFactory` | Factoría que crea instancias de `QLabel` usando un `ScreenConfig`.       |
| `ScreenState`   | Modelo que contiene los valores visuales actuales mostrados en pantalla. |
| `QLabel`        | Widget visual usado para mostrar información al usuario.                 |
| `QVBoxLayout`   | Layout vertical que organiza las pantallas en la interfaz.               |

---

## Ejemplo de uso

```python
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_screens_creators import ScreensCreator

app = QApplication([])

# Crear una ventana principal
main_window = QMainWindow()

# Instanciar la clase creadora de pantallas
creator = ScreensCreator(main_window)

# Crear pantallas y layout
layout, val1, val2, op, res = creator.create_screens()

# Asignar layout al widget principal
central_widget = main_window.centralWidget()
if central_widget:
    central_widget.setLayout(layout)

main_window.show()
app.exec_()
```

### Explicación del ejemplo

1. **Inicialización de PyQt5**  
    Se crea una aplicación Qt con una ventana principal.
    
2. **Instanciación de `ScreensCreator`**  
    Se pasa la ventana principal para generar y gestionar las pantallas.
    
3. **Creación de pantallas**  
    `create_screens()` construye el layout vertical y las pantallas de entrada y resultado.
    
4. **Renderizado**  
    El layout se inserta en el widget principal y se muestra en pantalla.
