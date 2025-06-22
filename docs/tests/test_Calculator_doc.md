# Tests unitarios para **Calculator**

## Propósito y Responsabilidad

El archivo `test_calculator.py` contiene pruebas unitarias para verificar el 
funcionamiento correcto de los métodos de la clase `Calculator`. Estas pruebas 
aseguran que las operaciones aritméticas se comportan como se espera en 
diversos escenarios: positivos, negativos, decimales y casos borde como la 
división por cero.

### Características principales

- **Cobertura**: Se cubren los métodos `add`, `subtract`, `multiply` y `divide`.
- **Uso de Decimal**: Todas las pruebas usan `Decimal` para mantener la 
  precisión.
- **Uso de pytest**: Se utiliza `pytest` para manejar las aserciones y 
  excepciones esperadas.
- **Composición**: Cada grupo de pruebas se organiza en una clase independiente 
  por método.

---

## Organización del archivo

El archivo está estructurado en 4 bloques principales, cada uno testeando un 
método de `Calculator`:

- `TestCalculatorAdd`: pruebas del método `add()`.
- `TestCalculatorSubtract`: pruebas del método `subtract()`.
- `TestCalculatorMultiply`: pruebas del método `multiply()`.
- `TestCalculatorDivide`: pruebas del método `divide()`.

---

## Clases de prueba

### TestCalculatorAdd

Pruebas para `Calculator.add()` en los siguientes casos:

- Suma de enteros positivos y negativos.
- Suma de decimales positivos y negativos.
- Casos con cero como uno de los operandos.

### TestCalculatorSubtract

Pruebas para `Calculator.subtract()` con:

- Enteros y decimales (positivos y negativos).
- Validación de resta con cero.

### TestCalculatorMultiply

Pruebas para `Calculator.multiply()` considerando:

- Multiplicación con enteros y decimales.
- Comprobación de signo.
- Multiplicación por cero.

### TestCalculatorDivide

Pruebas para `Calculator.divide()` en:

- División entre enteros y decimales.
- Casos con signos opuestos.
- División por cero (se espera `ZeroDivisionError`).

---

## Diagrama UML 

<figure markdown="span">
  ![TestCalculator - UML](./tests_uml/uml_tests_Calculator.svg){ width="600" }
  <figcaption>TestCalculator</figcaption>
</figure>

---

## Dependencias

|Librería|Descripción|
|---|---|
|`decimal`|Para operaciones de alta precisión numérica.|
|`pytest`|Framework de pruebas utilizado para validar funciones.|

---

## Ejecución

Para ejecutar las pruebas usa el siguiente comando:

```bash
pytest test_calculator.py
```

Esto validará todas las funciones definidas y confirmará que `Calculator` se  
comporta correctamente.

---

## Consideraciones finales

- Se espera que las excepciones, como la división por cero, sean correctamente  
    lanzadas y capturadas.
    
- Cada clase agrupa las pruebas de un único método para mantener claridad y  
    organización.
