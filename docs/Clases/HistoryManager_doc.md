# Clase **HistoryManager**

# Propósito y Responsabilidad
La clase HistoryManager gestiona el historial de operaciones matemáticas guardadas en una base de datos SQLite local. Esta clase centraliza la creación, lectura y eliminación de registros en la tabla history_results, manteniendo una sola instancia activa gracias al patrón Singleton.

### Características principales
- Gestión de base de datos SQLite: Ejecuta operaciones CREATE, INSERT, SELECT y DELETE sobre la tabla de historial.
- Uso de decorador: Emplea un decorador llamado @gestor_database que se encarga automáticamente de manejar el cursor y las conexiones.
- Simplicidad de uso: La interfaz de uso expone métodos directos y claros para interactuar con la base de datos.
- Encapsulamiento de lógica de persistencia: Aísla el acceso a datos para que otras capas (como la lógica de negocio o UI) no se preocupen de los detalles técnicos.

### Patrón de Diseño aplicado
Se utiliza el patrón Singleton para asegurar una única instancia de HistoryManager durante la ejecución del programa.

### Implementación del patrón
```python
class HistoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

#### Por qué este patrón y sus ventajas
- Evita múltiples conexiones innecesarias: Garantiza que todos los métodos accedan a la misma instancia de conexión.
- Eficiencia: Reduce el costo de instanciar objetos repetidamente y simplifica el mantenimiento del estado.
- Centralización del acceso: Toda interacción con el historial pasa por una única instancia coherente.

---
## Diagrama UML
![HistoryManager UML](uml/uml_history_manager.svg)

---
## Métodos principales

```python
+ __new__(cls): HistoryManager
+ create_table(): None
+ new_history(history_equation: str, history_result: Decimal): None
+ delete_history(): None
+ get_last_records(limit: int = 5): list
```

#### Descripción de métodos

- `__new__(cls)`  
    Implementación del patrón Singleton. Devuelve siempre la misma instancia.
    
- `create_table()`  
    Crea la tabla `history_results` si no existe. Define columnas para ID, ecuación y resultado.
    
- `new_history(equation, result)`  
    Inserta una nueva operación matemática en la tabla. Recibe la ecuación en formato `str` y el resultado en `Decimal`.
    
- `delete_history()`  
    Elimina todos los registros del historial.
    
- `get_last_records(limit=5)`  
    Retorna los últimos `limit` registros insertados, ordenados por ID descendente.
    
---
## Dependencias

|                |                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------- |
| Python         | versión igual o mayor a python3.7                                                        |
| sqlite3        | módulo estáandar                                                                         |
| decimal        | precisión numérica                                                                       |
| typing         | `Callable, Any, List, Dict`                                                              |
| HistoryTableDB | Clase auxiliar para validar y encapsular datos antes de insertarlos en la base de datos. |
  
---
## Relaciones

|                                                     |                                                                                                                                     |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Decorador externo                                   | Utiliza `@gestor_database` para envolver métodos que acceden a la base de datos, inyectando automáticamente el cursor de conexión.  |
| HistoryTableDB                                      | Se emplea para encapsular la ecuación y el resultado antes de insertarlos, actuando como objeto DTO.                                |
| Sistema externo de presentación o lógica de negocio | Este será responsable de invocar los métodos de `HistoryManager` según las acciones del usuario (como guardar o mostrar historial). |

---
## Ejemplo de uso
```python
from decimal import Decimal
from history_manager_db import HistoryManager

if __name__ == "__main__":
    manager = HistoryManager()

    # Crear la tabla si no existe
    manager.create_table()

    # Guardar operación
    manager.new_history("3 * (2 + 4)", Decimal(18))

    # Obtener últimos 3 registros
    ultimos = manager.get_last_records(limit=3)
    print(ultimos)

    # Borrar historial
    manager.delete_history()
```

### Explicación del ejemplo

1. **Instancia**:  
    `HistoryManager` se instancia usando el patrón Singleton. Siempre se reutiliza la misma instancia.
    
2. **Creación de tabla**:  
    Se asegura que la tabla `history_results` esté lista antes de insertar datos.
    
3. **Nuevo registro**:  
    Se guarda la ecuación y el resultado como un nuevo registro usando `Decimal` para evitar imprecisiones.
    
4. **Consulta del historial**:  
    Se recuperan los últimos 3 registros insertados para mostrarlos o procesarlos.
    
5. **Limpieza del historial**:  
    Se eliminan todos los registros con un solo comando.
