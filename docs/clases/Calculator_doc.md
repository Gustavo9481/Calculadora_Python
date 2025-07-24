# Clase `Calculator`

La clase **`Calculator`** proporciona métodos estáticos para realizar operaciones aritméticas básicas (suma, resta, multiplicación, división y porcentaje).

Su diseño se centra en la **precisión, el rendimiento y la seguridad**, utilizando el tipo `Decimal` en un entorno controlado para evitar efectos secundarios.

---

## Funcionalidad y Diseño

- **Precisión Controlada**: A través del decorador `use_precision`, todos los cálculos se ejecutan dentro de un **contexto local** con una precisión de 28 dígitos. Esto garantiza resultados exactos sin modificar el estado de precisión global de la aplicación, haciendo la clase autocontenida y robusta.
- **Cálculos Optimizados**: Cada método de operación está decorado con `@lru_cache` para almacenar en caché los resultados. Esto mejora significativamente el rendimiento cuando se repiten las mismas operaciones.
- **Diseño sin Estado (Stateless)**: La clase no almacena ningún estado interno entre llamadas. Cada operación es independiente, lo que la hace predecible y segura para usar en entornos concurrentes (thread-safe).

---

## Atributos de Clase

| Atributo     | Tipo  | Descripción                                                                 |
|--------------|-------|-----------------------------------------------------------------------------|
| `_PRECISION` | `int` | Define la precisión decimal (28 dígitos) utilizada en todos los cálculos. |

---

## Métodos

Todos los métodos son estáticos y están decorados con `@use_precision` y `@lru_cache`.

| Método       | Parámetros                      | Retorno   | Descripción                                     |
|--------------|---------------------------------|-----------|-------------------------------------------------|
| `add`        | `value_1: Decimal`, `value_2: Decimal` | `Decimal` | Suma dos números decimales.                     |
| `subtract`   | `value_1: Decimal`, `value_2: Decimal` | `Decimal` | Resta dos números decimales.                    |
| `multiply`   | `value_1: Decimal`, `value_2: Decimal` | `Decimal` | Multiplica dos números decimales.               |
| `divide`     | `value_1: Decimal`, `value_2: Decimal` | `Decimal` | Divide dos números decimales.                   |
| `percent`    | `value_1: Decimal`, `value_2: Decimal` | `Decimal` | Calcula el porcentaje de un número.             |

---

## Diagrama UML

<p align="center">
    <img src="../clases_uml/uml_calculator.svg" alt="Diagrama UML Calculator" width="600"/>
</p>

---

## Ejemplo de Uso

El uso de la clase no cambia, ya que la gestión de la precisión es interna.

```python
from decimal import Decimal
from calculator import Calculator

# Suma
resultado_suma = Calculator.add(Decimal('10.5'), Decimal('5.2'))
print(f"Suma: {resultado_suma}")  # Salida: Suma: 15.7

# División
try:
    resultado_division = Calculator.divide(Decimal('10'), Decimal('3'))
    print(f"División: {resultado_division}")
except ZeroDivisionError as e:
    print(e)
```
