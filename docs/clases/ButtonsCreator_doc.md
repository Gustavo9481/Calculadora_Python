# Clase `ButtonsCreator`

La clase **`ButtonsCreator`** es responsable de crear y gestionar todos los botones de la interfaz de la calculadora. Utiliza un enfoque similar al patrón **Factory Method** para generar los botones y asignarles su funcionalidad correspondiente.

---

## Funcionalidad

- **Creación de Botones**: Genera todos los botones de la calculadora (números, operadores, funciones especiales) y los organiza en un `QGridLayout`.
- **Asignación de Funciones**: Conecta cada botón a su función correspondiente (por ejemplo, `insert_value`, `insert_operator`, `calculate_result`).
- **Gestión del Estado**: Mantiene el estado actual de la calculadora a través de la clase `CalculatorState`, que almacena los valores, el operador y el resultado.
- **Interacción con la Base de Datos**: Utiliza una instancia de `HistoryManager` para guardar el historial de cálculos en la base de datos.

---

## Atributos

| Atributo | Tipo | Descripción |
|---|---|---|
| `central_widget` | `QWidget` | Widget central donde se colocan los botones. |
| `display_value_1` | `QLabel` | Pantalla para el primer valor. |
| `display_value_2` | `QLabel` | Pantalla para el segundo valor. |
| `display_operator` | `QLabel` | Pantalla para el operador. |
| `display_result` | `QLabel` | Pantalla para el resultado. |
| `state` | `CalculatorState` | Estado actual de la calculadora. |
| `buttons` | `Dict[str, QPushButton]` | Diccionario de los botones creados. |
| `history_manager` | `HistoryManager` | Instancia para gestionar el historial. |

---

## Métodos Principales

### `create_buttons() -> QGridLayout`
Crea y configura todos los botones de la calculadora, los añade a un layout de rejilla y conecta sus señales `clicked` a las funciones correspondientes.

### `insert_value(value: str)`
Inserta un valor numérico o un punto decimal en la pantalla. Se encarga de validar que no se inserte más de un punto decimal por número.

### `insert_operator(operator: str)`
Inserta un operador en la pantalla. Si ya hay una operación en curso, calcula el resultado antes de insertar el nuevo operador.

### `calculate_result(value: str)`
Realiza el cálculo utilizando la clase `Calculator`, muestra el resultado en la pantalla y guarda la operación en el historial de la base de datos.

### `clear_screen(value: str)`
Limpia todas las pantallas y reinicia el estado de la calculadora.

### `delete_last_char(value: str)`
Elimina el último carácter de la entrada actual.

---

## Diagrama UML

<p align="center">
    <img src="../clases_uml/uml_buttons_creator.svg" alt="Diagrama UML
        ButtonsCreator" width="400"/>
</p>
