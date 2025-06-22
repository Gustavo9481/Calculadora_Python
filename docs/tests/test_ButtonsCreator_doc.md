# Clase **MockDisplay**

## Propósito y Responsabilidad

La clase `MockDisplay` es una clase auxiliar utilizada en pruebas unitarias para 
simular el comportamiento del widget `QLabel` de PyQt5 para permitir test
unitarios sobre la clase `ButtonsCreator`. Su principal objetivo 
es permitir verificar el flujo y la lógica del programa sin necesidad de una 
interfaz gráfica real, haciendo posible el testeo automatizado de componentes 
que interactúan con elementos visuales.

### Características principales

- Simulación de interfaz: Reemplaza a `QLabel` en entornos de prueba.
- Facilidad de prueba: Permite verificar que se actualice correctamente el texto.
- Aislamiento: Reduce dependencias en entornos gráficos complejos.
- Simple y reutilizable: Puede utilizarse en múltiples tests donde se necesite 
  simular etiquetas visuales.

---

## Diagrama UML


<figure markdown="span">
  ![MockDisplay - UML](./tests_uml/uml_tests_ButtonsCreator.svg){ width="500" }
  <figcaption>Clase MockDisplay</figcaption>
</figure>

---

## Métodos principales

```python
+ __init__() -> None
+ setText(text: str) -> None
```

### Descripción de métodos clave

- `__init__()`  
    Inicializa una nueva instancia de `MockDisplay`, con el atributo `text` vacío.
    
- `setText(text)`  
    Emula el método `setText` de `QLabel`, guardando el valor recibido en el  
    atributo `text` interno.
    
---

## Dependencias

| Componente | Descripción                                            |
| ---------- | ------------------------------------------------------ |
| Python     | No requiere librerías externas.                        |
| PyQt5      | Simula el comportamiento de `QLabel`, pero sin usarlo. |

---

## Relaciones

| Relación       | Descripción                                                    |
| -------------- | -------------------------------------------------------------- |
| ButtonsCreator | Se usa como reemplazo de los `QLabel` en pruebas unitarias.    |
| pytest         | Framework que ejecuta los tests donde se emplea `MockDisplay`. |

---

## Ejemplo de uso

```python
def test_insert_value():
    display = MockDisplay()
    display.setText("5")
    assert display.text == "5"
```

### Explicación del ejemplo

1. **Instanciación**  
    Se crea un objeto `MockDisplay`.
    
2. **Simulación de interacción**  
    Se usa el método `setText("5")` para simular un cambio de texto.
    
3. **Verificación**  
    Se evalúa que el atributo `text` haya sido correctamente actualizado.
