# Clase **HistoryTableDB**

## Propósito y Responsabilidad

La clase `HistoryTableDB` tiene como responsabilidad principal encapsular la información necesaria para registrar operaciones matemáticas (ecuación y resultado) en la base de datos. Actúa como un **Data Transfer Object (DTO)** validado por Pydantic, asegurando que cada instancia cumpla con el esquema definido antes de ser utilizada en otros componentes.

### Características principales

- **Validación de datos**: Hereda de `BaseModel` de Pydantic, lo que garantiza que los atributos `equation` y `result` respeten los tipos esperados (`str` y `Decimal`).
    
- **Representación clara**: Incluye el método `__str__` para mostrar la ecuación junto con su resultado en un formato legible ("`<ecuación> = <resultado>`").
    
- **Ligereza**: No contiene lógica de negocio ni acceso directo a la base de datos; solo almacena y valida datos.
    
### Patrón de Diseño aplicado

Se aplica el patrón **DTO (Data Transfer Object)** o **Value Object**:

- **DTO (Data Transfer Object)**: Se utiliza para transportar datos entre capas de la aplicación (por ejemplo, desde la capa de cálculo hasta la capa de persistencia), sin exponer lógica de negocio.
    
- **Value Object**: Objetos inmutables (en este caso, controlados por Pydantic), cuyo estado se define en el momento de la creación y no cambia a lo largo de su ciclo de vida.

### Implementación del patrón

```python
from decimal import Decimal
from pydantic import BaseModel


class HistoryTableDB(BaseModel):

    equation: str = None
    result: Decimal = None

    def __str__(self) -> str:
        
        return f"{self.equation} = {self.result}"
```
#### Por qué este patrón y sus ventajas

- **Separación de responsabilidades**: El DTO desacopla la validación y el transporte de datos de la lógica de negocio y del acceso a la base de datos. Así, cada capa (presentación, negocio, persistencia) se mantiene independiente.
    
- **Validación automática**: Al heredar de `BaseModel`, Pydantic valida tipos y formatos al instanciar, reduciendo errores tempranos por datos inválidos.
    
- **Inmutabilidad controlada**: Aunque Pydantic permite mutación, el diseño de DTO fomenta tratar instancias como valores inmutables una vez creadas, lo que facilita pruebas y depuración.
    
- **Claridad en el contrato de datos**: La definición explícita de atributos (`equation: str`, `result: Decimal`) sirve como documentación viva, clarificando qué campos son obligatorios y sus tipos.

---
### Diagrama UML

<figure markdown="span">
  ![HistoryTableDB - UML](./clases_uml/uml_history_db.svg){ width="400" }
  <figcaption>Clase HistoryTableDB</figcaption>
</figure>


---
## Métodos principales

- `__init__(self, equation: str, result: Decimal)`:  
    Constructor generado por Pydantic. Recibe la ecuación y el resultado; valida tipos automáticamente.
    
- `__str__(self) -> str`:  
    Retorna la representación en cadena de la operación, útil para mostrar o registrar logs.

```python
def __str__(self) -> str:
    """
    Devuelve la representación en cadena de la operación.

    :returns: Cadena con el formato "<ecuación> = <resultado>".
    :rtype: str
    """
    return f"{self.equation} = {self.result}"
```

## Dependencias

- **Python ≥ 3.7**
- **pydantic**
    - Para validación de modelos y generación automática del constructor.
    - Instalación:
		```bash
		# pip
		pip install pydantic		

		# uv
		uv add pydantic
		```
- **decimal** (módulo estándar)
    
    - `Decimal` se emplea para asegurar precisión en los resultados numéricos.
        

---

## Relaciones

- **ORM o capa de persistencia** (externa):
    
    - `HistoryTableDB` no ejecuta operaciones SQL directamente.
        
    - Otras clases o funciones deben mapear la instancia a sentencias `INSERT`/`SELECT` según el motor de base de datos (por ejemplo, usando SQLAlchemy, psycopg2 o cualquier otro driver).
        
- **Capa de negocio**:
    
    - Antes de persistir el resultado de una operación, la lógica de negocio crea una instancia de `HistoryTableDB` para validar y transportar datos.
        
- **Capa de presentación o servicio**:
    
    - Puede utilizar el método `__str__` para renderizar el historial de operaciones en consola, logs o interfaces de usuario.

---
## Ejemplo de uso

```python
from decimal import Decimal
from history_db import HistoryTableDB

def guardar_operacion_en_db(history: HistoryTableDB):
    """
    Función que simula la inserción en la base de datos.
    El código real dependerá del ORM o del driver SQL que emplees.
    """
    # Ejemplo de pseudocódigo de persistencia:
    # sql = "INSERT INTO history_table (equation, result) VALUES (%s, %s)"
    # cursor.execute(sql, (history.equation, str(history.result)))
    # db.commit()
    print(f"Insertando en DB: {history.equation} = {history.result}")

if __name__ == "__main__":
    # 1. Definir ecuación y calcular resultado
    ecuacion = "12 / 4 + 7"
    resultado = Decimal(12) / Decimal(4) + Decimal(7)  # Decimal('10')

    # 2. Crear instancia de HistoryTableDB (Pydantic valida tipos)
    registro = HistoryTableDB(equation=ecuacion, result=resultado)

    # 3. Mostrar representación en cadena
    print(str(registro))  # Salida: "12 / 4 + 7 = 10"

    # 4. Llamar a la función que simula guardar en la base de datos
    guardar_operacion_en_db(registro)
```

### Explicación del ejemplo

1. **Definición de la ecuación**:
    - Se crea la variable `ecuacion` como una cadena de texto que representa la operación.
    - Se calcula `resultado` utilizando objetos `Decimal` para evitar errores de coma flotante.
        
2. **Instanciación de `HistoryTableDB`**:
    - Al llamar a `HistoryTableDB(equation=ecuacion, result=resultado)`, Pydantic valida que:
        - `equation` sea una cadena (`str`).
        - `result` sea un objeto `Decimal`.
    - Si los tipos no coinciden, Pydantic lanza una excepción `ValidationError`.
        
3. **Representación en cadena**:
    - `print(str(registro))` invoca el método `__str__`, mostrando la operación en formato legible (`"12 / 4 + 7 = 10"`).
        
4. **Persistencia simulada**:
    - La función `guardar_operacion_en_db` recibe la instancia `registro` y simula la inserción en la base de datos.
    - En un caso real, esta función generaría y ejecutaría una sentencia SQL o usaría un ORM como SQLAlchemy para persistir el objeto en la tabla `history_table`.

