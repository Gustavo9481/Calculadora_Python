# Clase `AppCalculator`

La clase **`AppCalculator`** es el punto de entrada principal de la aplicación de la calculadora. Su función es inicializar y gestionar la aplicación, coordinando la interfaz gráfica y la base de datos del historial.

---

## Funcionalidad

- **Inicialización de la Aplicación**: Crea la instancia de la interfaz gráfica (`InterfaceCreator`) y el gestor de la base de datos (`HistoryManager`).
- **Gestión de la Base de Datos**: Se asegura de que la tabla del historial exista en la base de datos al iniciar la aplicación.
- **Ejecución de la Interfaz**: Inicia el bucle de eventos de la aplicación Qt para mostrar la ventana principal y gestionar las interacciones del usuario.

---

## Atributos

| Atributo    | Tipo               | Descripción                                            |
|-------------|--------------------|--------------------------------------------------------|
| `interface` | `InterfaceCreator` | Instancia de la interfaz gráfica de la calculadora.    |
| `history_db`| `HistoryManager`   | Instancia del gestor de la base de datos del historial.|

---

## Métodos

### `main()`

Este método es el punto de entrada que inicia la ejecución de la aplicación.

- **Responsabilidad**:
  1. Llama a `create_table()` en la instancia de `history_db` para asegurar que la tabla del historial esté lista.
  2. Llama a `run()` en la instancia de `interface` para mostrar la ventana principal e iniciar el bucle de eventos de Qt.

- **Parámetros**: No recibe ningún parámetro.
- **Retorno**: No retorna ningún valor (`None`).

---

## Diagrama UML

<p align="center">
    <img src="../clases_uml/uml_app_calculator.svg" alt="Diagrama UML
        AppCalculator" width="300"/>
</p>

---

## Ejemplo de Uso

Para iniciar la aplicación, se crea una instancia de `AppCalculator` y se llama a su método `main()`:

```python
if __name__ == "__main__":
    app = AppCalculator()
    app.main()
```
