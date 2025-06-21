# Clase **Calculator**

## Propósito y Responsabilidad

La clase `Calculator` tiene como propósito proporcionar operaciones aritméticas básicas con alta precisión, utilizando el tipo `Decimal` del módulo estándar `decimal`. Esta clase permite realizar sumas, restas, multiplicaciones, divisiones y cálculo de porcentajes de forma **determinista**, **precisa**, **thread-safe** y **stateless**.

### Características principales

- **Precisión**: Utiliza `Decimal` con una precisión configurada de 28 dígitos, ideal para contextos financieros o científicos.
    
- **Cacheo**: Aplica `functools.lru_cache` para evitar cálculos repetitivos.
    
- **Thread-safe**: Al no usar estado interno y emplear funciones puras, es seguro para ejecución concurrente.
    
- **Stateless**: Todos los métodos son estáticos y no dependen del estado de una instancia.
    

### Patrón de Diseño aplicado

Se aplica el patrón **Estrategia estática sin estado (Stateless Utility Class)**:

- Este patrón encapsula un conjunto de funciones relacionadas en una clase que no mantiene estado ni requiere instanciación.
    
- Permite agrupar lógica común (en este caso, operaciones aritméticas) de manera ordenada y reutilizable.
    

### Implementación del patrón

```python
class Calculator:
    @staticmethod
    @lru_cache(maxsize=1000)
    def add(value_1: Decimal, value_2: Decimal) -> Decimal:
        return value_1 + value_2
    # ... resto de operaciones similares (resta, multiplicación, división, porcentaje)
```

#### Por qué este patrón y sus ventajas

- **Claridad y organización**: Todas las funciones aritméticas están agrupadas en una clase.
    
- **Reutilización**: Puede ser usada por cualquier módulo sin necesidad de instanciación.
    
- **Bajo acoplamiento**: No depende de otras clases o estados internos.
    
- **Alto rendimiento**: Uso de `lru_cache` para evitar recálculos innecesarios.
    

---

## Diagrama UML

![Calculator UML - Diagrama de clase](./clases_uml/uml_calculator.svg)
---

## Métodos principales

- `add(value_1: Decimal, value_2: Decimal) -> Decimal`
    
    - Suma dos valores decimales.
        
- `subtract(value_1: Decimal, value_2: Decimal) -> Decimal`
    
    - Resta dos valores decimales.
        
- `multiply(value_1: Decimal, value_2: Decimal) -> Decimal`
    
    - Multiplica dos valores decimales.
        
- `divide(value_1: Decimal, value_2: Decimal) -> Decimal`
    
    - Divide dos valores decimales. Lanza `ZeroDivisionError` si el divisor es cero.
        
- `percent(value_1: Decimal, value_2: Decimal) -> Decimal`
    
    - Calcula el porcentaje de `value_1` respecto a `value_2`.
        

---
## Dependencias

|                             |                                                        |
| --------------------------- | ------------------------------------------------------ |
| Python                      | versión igual o mayor a python3.7                      |
| decimal (módulo estándar)   | Para realizar operaciones con alta precisión numérica. |
| functools (módulo estándar) | Se usa `lru_cache` para mejorar el rendimiento.        |

---
## Relaciones

- Esta clase puede ser utilizada por cualquier capa de la aplicación (negocio, servicios, presentación).
    
- Puede complementarse con objetos DTO como `HistoryTableDB` para registrar los resultados.
 
---
## Ejemplo de uso

```python
from decimal import Decimal
from calculator import Calculator

if __name__ == "__main__":
    a = Decimal("12.5")
    b = Decimal("7.3")

    print("Suma:", Calculator.add(a, b))
    print("Resta:", Calculator.subtract(a, b))
    print("Multiplicación:", Calculator.multiply(a, b))
    print("División:", Calculator.divide(a, b))
    print("Porcentaje:", Calculator.percent(a, b))
```

### Explicación del ejemplo

1. **Importación de la clase**: Se importa `Calculator` y el tipo `Decimal`.
    
2. **Inicialización de datos**: Se crean dos valores decimales de prueba.
    
3. **Llamadas a métodos estáticos**: Se realizan todas las operaciones sin necesidad de crear una instancia de la clase.
    
4. **Salida legible**: Cada resultado se muestra por consola en un formato claro y directo.
