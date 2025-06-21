# Clase **InterfaceCreator**

## Propósito y Responsabilidad

La clase `InterfaceCreator` se encarga de construir la ventana principal de la
calculadora y de organizar todos los componentes visuales usando PyQt5. Actúa
como un *ensamblador visual*, aplicando el patrón Factory para integrar las
pantallas y los botones generados por otras clases.

### Características principales

- Creación de ventana principal: Configura el `QMainWindow`, tamaño, título y
  estilo general.

- Integración modular: Llama a `ScreensCreator` para generar las pantallas y a
  `ButtonsCreator` para organizar los botones.

- Gestión del layout: Une todas las partes en un único `QVBoxLayout` que se
  asigna al widget central.

- Ejecución de la app: Expone un método `run()` que lanza el bucle principal de
  eventos de Qt.

### Patrón de Diseño aplicado

`InterfaceCreator` aplica el patrón Factory Method de forma explícita, ya que
orquesta la creación de componentes gráficos delegando dicha responsabilidad en
clases especializadas (`ScreensCreator`, `ButtonsCreator`), facilitando la
modularidad y reutilización.

### Implementación del patrón
```python
def _setup_window(self) -> None:
    screens_creator = ScreensCreator(self.main_window)
    (layout, val1, val2, op, res) = screens_creator.create_screens()

    buttons_creator = ButtonsCreator(
        central_widget, val1, val2, op, res
    )
    buttons_layout = buttons_creator.create_buttons()
```

#### Por qué este patrón y sus ventajas

- **Modularidad**: Permite modificar la lógica de pantallas o botones sin tocar  
    esta clase.
    
- **Reutilización**: Se pueden reutilizar las clases creadoras para otras UIs o  
    versiones.
    
- **Escalabilidad**: Es fácil extender la UI añadiendo más bloques funcionales  
    o visuales.
    

---

## Diagrama UML

![InterfaceCreator UML - Diagramade clase](./clases_uml/uml_interface_creator.svg)
---

## Métodos principales

```python
+ __init__() -> None
+ run() -> None
- _setup_window() -> None
```

### Descripción de métodos clave

- `__init__()`  
    Inicializa la instancia principal, configurando la app y llamando a  
    `_setup_window()`.
    
- `run()`  
    Lanza el bucle principal de la interfaz gráfica mostrando la ventana.
    
- `_setup_window()`  
    Método interno que arma y conecta toda la estructura visual, integrando  
    pantallas y botones.

---

## Dependencias

|                     |                                                                  |
| ------------------- | ---------------------------------------------------------------- |
| Python              | versión igual o mayor a Python 3.7                               |
| PyQt5               | Widgets: `QApplication`, `QMainWindow`, `QWidget`, `QVBoxLayout` |
| ui_screens_creators | Clase encargada de construir las pantallas de la calculadora     |
| ui_buttons_creator  | Clase encargada de construir los botones de la interfaz          |

---

## Relaciones

|                                     |                                                                 |
| ----------------------------------- | --------------------------------------------------------------- |
| ScreensCreator                      | Clase responsable de construir los QLabel usados como pantallas |
| ButtonsCreator                      | Clase que construye el conjunto de botones de la calculadora    |
| QMainWindow / QWidget / QVBoxLayout | Estructura base del layout y presentación visual                |

---

## Ejemplo de uso

```python
from ui_interface_creator import InterfaceCreator

if __name__ == "__main__":
    interface = InterfaceCreator()
    interface.run()
```

### Explicación del ejemplo

1. **Importación del módulo**  
    Se importa la clase `InterfaceCreator` desde su módulo correspondiente.
    
2. **Instanciación**  
    Se crea una instancia de la clase que inicializa la ventana y la estructura  
    visual.
    
3. **Ejecución de la aplicación**  
    Se invoca el método `run()` que muestra la interfaz y queda a la espera de  
    eventos del usuario.
