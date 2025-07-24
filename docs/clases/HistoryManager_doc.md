# Clase `HistoryManager`

La clase **`HistoryManager`** gestiona todas las operaciones de la base de datos para el historial de la calculadora. Implementa el patrón de diseño **Singleton** para garantizar que solo exista una única instancia de esta clase, evitando así múltiples conexiones a la base de datos.

---

## Funcionalidad

- **Patrón Singleton**: Asegura una única instancia de `HistoryManager` para toda la aplicación.
- **Gestión de la Base de Datos**: Maneja la creación de la tabla, la inserción de nuevos registros, la eliminación del historial y la consulta de los últimos registros.
- **Decorador `gestor_database`**: Simplifica el manejo de la conexión y el cursor de la base de datos, abriendo y cerrando la conexión automáticamente y manejando posibles errores.

---

## Atributos

| Atributo | Tipo | Descripción |
|---|---|---|
| `_instance` | `HistoryManager` | Almacena la única instancia de la clase (Singleton). |
| `_db_path` | `Path` | Ruta al archivo de la base de datos (`calculator_db.db`). |

---

## Métodos

### `__new__()`
Implementa el patrón Singleton. Si no existe una instancia de `HistoryManager`, crea una nueva; de lo contrario, devuelve la instancia existente.

### `create_table()`
Crea la tabla `history_results` en la base de datos si no existe. Esta tabla almacena la ecuación y el resultado de cada operación.

### `new_history(history_equation: str, history_result: Decimal)`
Agrega un nuevo registro al historial en la base de datos. Toma la ecuación y el resultado como parámetros.

### `delete_history()`
Elimina todos los registros de la tabla `history_results`.

### `get_last_records(limit: int = 5) -> list`
Obtiene los últimos registros del historial, ordenados de forma descendente. Por defecto, devuelve los últimos 5 registros.

---

## Diagrama UML

<p align="center">
    <img src="../clases_uml/uml_history_manager.svg" alt="Diagrama UML
        HistoryManager" width="400"/>
</p>

---

## Decorador `gestor_database`

Este decorador se encarga de la gestión de la conexión a la base de datos. Envuelve los métodos que interactúan con la base de datos y se encarga de:

1.  Abrir la conexión a la base de datos.
2.  Crear un cursor.
3.  Ejecutar la función decorada, pasándole el cursor.
4.  Cerrar el cursor y la conexión.
5.  Manejar cualquier `sqlite3.Error` que pueda ocurrir.
