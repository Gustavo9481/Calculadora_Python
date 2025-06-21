# Clase **AppCalculator**

## Propósito y Responsabilidad

La clase `AppCalculator` tiene como propósito iniciar y gestionar la ejecución de
una aplicación de calculadora con interfaz gráfica basada en PyQt. Esta clase actúa
como punto de entrada de alto nivel en la arquitectura del programa, manteniendo
una única responsabilidad: inicializar y ejecutar los componentes visuales y de base
de datos de la aplicación.

### Características principales

- **Inicialización clara**: Gestiona la creación de la interfaz y la conexión a la
  base de datos histórica.

- **Responsabilidad única**: Se enfoca en el arranque de la aplicación, evitando
  lógica de negocio en esta capa.

- **Modularidad**: Se apoya en otros módulos (`InterfaceCreator` y
  `HistoryManager`) para delegar funcionalidades específicas.

### Patrón de Diseño aplicado

Se aplica el patrón **Fachada (Facade Pattern)**:

- Este patrón proporciona una interfaz unificada y simplificada a un conjunto de
  interfaces en un subsistema más complejo.

- En este caso, `AppCalculator` encapsula la inicialización de la UI y la base de
  datos, simplificando el uso externo de esos módulos.

### Implementación del patrón

```python
class AppCalculator:
    interface = InterfaceCreator()
    history_db = HistoryManager()

    def main(self) -> None:
        self.interface.run()
        self.history_db.create_table()
```

#### Por qué este patrón y sus ventajas

- **Simplicidad para el usuario final**: El cliente solo necesita instanciar  
    `AppCalculator` y llamar a `main()` para iniciar todo el sistema.
    
- **Separación de preocupaciones**: La lógica de la UI y la persistencia están  
    claramente separadas y delegadas.
    
- **Escalabilidad**: Es fácil extender la aplicación sin modificar la clase central,  
    simplemente modificando las dependencias.
    

---

## Diagrama UML


<figure markdown="span">
  ![AppCalculator - UML](./clases_uml/uml_app_calculator.svg){ width="300" }
  <figcaption>Clase AppCalculator</figcaption>
</figure>


## Métodos principales

- `main() -> None`
    
    - Inicia la ejecución de la aplicación, lanzando la interfaz gráfica y  
        asegurando que la base de datos esté inicializada.
        

---

## Dependencias

|                  |                                                  |
| ---------------- | ------------------------------------------------ |
| Python           | versión igual o mayor a python3.7                |
| PyQt             | Para la construcción y ejecución de la UI.       |
| InterfaceCreator | Módulo encargado de generar la interfaz gráfica. |
| HistoryManager   | Módulo que gestiona la base de datos histórica.  |

---

## Relaciones

- Esta clase orquesta los módulos `InterfaceCreator` y `HistoryManager`.
    
- Es utilizada como punto de entrada en el script principal de la aplicación:
    
    ```python
    if __name__ == "__main__":     
	    app = AppCalculator()     
	    app.main()
	```

---

## Ejemplo de uso

```python
from main import AppCalculator  

if __name__ == "__main__":     
	app = AppCalculator()     
	app.main()
```
### Explicación del ejemplo

1. **Importación de la clase**: Se importa la clase principal desde el módulo `main`.
    
2. **Instanciación de la aplicación**: Se crea un objeto de tipo `AppCalculator`.
    
3. **Llamada al método `main()`**: Se ejecuta la aplicación, lanzando la UI y la  
    inicialización de la base de datos.
    
4. **Composición simple**: No requiere parámetros, todo está gestionado internamente.
