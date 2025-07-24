# Pruebas de `TestCalculator`

La clase **`TestCalculator`** contiene las pruebas unitarias para la clase `Calculator`. El objetivo de estas pruebas es asegurar que todas las operaciones aritméticas (suma, resta, multiplicación, división y porcentaje) funcionen correctamente y manejen los casos límite de manera adecuada.

---

## Funcionalidad de las Pruebas

- **Pruebas Parametrizadas**: Se utiliza `pytest.mark.parametrize` para probar cada operación con un conjunto diverso de datos, incluyendo números positivos, negativos, decimales y cero. Esto permite cubrir múltiples escenarios con un solo método de prueba.
- **Manejo de Errores**: Se verifica que la operación de división lance correctamente la excepción `ZeroDivisionError` cuando se intenta dividir por cero.
- **Precisión Decimal**: Se asegura que los cálculos que involucran `Decimal` mantengan la precisión esperada.

---

## Métodos de Prueba

### `test_add(value_1, value_2, expected)`
Verifica que la suma de `value_1` y `value_2` sea igual a `expected`.

### `test_subtract(value_1, value_2, expected)`
Verifica que la resta de `value_2` de `value_1` sea igual a `expected`.

### `test_multiply(value_1, value_2, expected)`
Verifica que la multiplicación de `value_1` y `value_2` sea igual a `expected`.

### `test_divide(value_1, value_2, expected)`
Verifica que la división de `value_1` por `value_2` sea igual a `expected`.

### `test_divide_by_zero(value_1, value_2)`
Verifica que al intentar dividir `value_1` por cero (`value_2`), se lance la excepción `ZeroDivisionError`.

### `test_percent(value_1, value_2, expected)`
Verifica que el cálculo del porcentaje de `value_1` con respecto a `value_2` sea igual a `expected`.

---

## Diagrama UML de Pruebas

<p align="center">
    <img src="../tests_uml/uml_tests_Calculator.svg" alt="Diagrama UML
        TestCalculator" width="550"/>
</p>
