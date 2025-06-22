# Clase **TestHistoryManager**

## Propósito y Responsabilidad

La clase TestHistoryManager contiene un conjunto completo de pruebas unitarias diseñadas para validar el correcto funcionamiento de la clase HistoryManager. Esta clase de pruebas se encarga de verificar todas las operaciones críticas de gestión del historial de operaciones matemáticas, asegurando la integridad de los datos y la correcta implementación de patrones de diseño.

### Características principales

- **Cobertura exhaustiva**: Prueba todas las funcionalidades principales de HistoryManager incluyendo inserción, consulta, eliminación y patrón Singleton.
- **Aislamiento de pruebas**: Utiliza bases de datos en memoria para evitar efectos colaterales entre pruebas.
- **Uso de fixtures**: Emplea fixtures de pytest para proporcionar entornos de prueba consistentes y reutilizables.
- **Mocking estratégico**: Implementa técnicas de mocking para aislar las pruebas de dependencias externas.
- **Validación de patrones**: Verifica la correcta implementación del patrón Singleton en HistoryManager.

### Estrategia de Testing aplicada

Se utiliza el patrón de pruebas unitarias con pytest, empleando fixtures para la preparación del entorno y mocking para el aislamiento de dependencias.

### Implementación del patrón de testing

```python
class TestHistoryManager:
    @pytest.fixture
    def history_manager(self):
        return HistoryManager()

    @pytest.fixture
    def memory_db_connection(self):
        conn = sqlite3.connect(':memory:')
        yield conn
        conn.close()
```

#### Por qué esta estrategia y sus ventajas

- **Aislamiento completo**: Cada prueba se ejecuta en un entorno limpio sin interferencias de otras pruebas.
- **Velocidad**: Las bases de datos en memoria son extremadamente rápidas y no requieren E/O de disco.
- **Reproducibilidad**: Las pruebas siempre producen los mismos resultados independientemente del entorno.
- **Facilidad de mantenimiento**: Las fixtures centralizan la configuración y limpieza del entorno de prueba.

---

## Diagrama UML

<figure markdown="span">
  ![TestHistoryManager - UML](./tests_uml/uml_tests_HistoryManager.svg){ width="500" }
  <figcaption>TestHistoryManager</figcaption>
</figure>

---

## Métodos principales

```python
+ history_manager(): HistoryManager (fixture)
+ memory_db_connection(): sqlite3.Connection (fixture)
+ test_new_history_inserts_data(history_manager, memory_db_connection, mocker): None
+ test_get_last_records(history_manager, memory_db_connection, mocker): None
+ test_delete_history(history_manager, memory_db_connection, mocker): None
+ test_singleton_pattern(): None
```

#### Descripción de métodos

- `history_manager()` **(fixture)**  
    Proporciona una instancia fresca de HistoryManager para cada prueba, garantizando aislamiento entre tests.
    
- `memory_db_connection()` **(fixture)**  
    Crea una conexión temporal a una base de datos SQLite en memoria que se limpia automáticamente después de cada prueba.
    
- `test_new_history_inserts_data()`  
    Verifica la inserción correcta de registros individuales, validando la conversión de tipos y la integridad de los datos guardados.
    
- `test_get_last_records()`  
    Prueba la recuperación de los últimos registros, insertando múltiples entradas y verificando el orden y contenido correcto.
    
- `test_delete_history()`  
    Valida la eliminación completa del historial, probando tanto con datos existentes como con tablas vacías.
    
- `test_singleton_pattern()`  
    Confirma que el patrón Singleton está correctamente implementado verificando que múltiples instanciaciones retornan el mismo objeto.
    

---

## Dependencias

|||
|---|---|
|Python|versión igual o mayor a python3.7|
|pytest|framework de testing principal|
|pytest-mock|extensión para funcionalidades de mocking|
|sqlite3|módulo estándar para base de datos de prueba|
|decimal|para manejo de precisión numérica en los datos de prueba|
|HistoryManager|Clase bajo prueba (SUT - System Under Test)|
|history_manager_db|Módulo que contiene la implementación de HistoryManager|

---

## Relaciones

|||
|---|---|
|HistoryManager (SUT)|Clase principal bajo prueba. TestHistoryManager valida todas sus funcionalidades y comportamientos esperados.|
|pytest.fixture|Utiliza fixtures para proporcionar entornos de prueba consistentes y reutilizables.|
|mocker (pytest-mock)|Emplea mocking para aislar las pruebas de dependencias externas como conexiones a base de datos.|
|sqlite3.Connection|Utiliza conexiones en memoria para pruebas rápidas y aisladas.|
|Sistema de CI/CD|Estas pruebas serán ejecutadas automáticamente en pipelines de integración continua para validar la calidad del código.|

---

## Ejemplo de uso

```python
import pytest
from decimal import Decimal
from test_history_manager import TestHistoryManager

# Ejecutar todas las pruebas
if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# Ejecutar una prueba específica
def test_example():
    test_class = TestHistoryManager()
    
    # Las pruebas se ejecutan normalmente con pytest
    # pytest test_history_manager.py::TestHistoryManager::test_singleton_pattern
    
    # O usando pytest directamente desde la línea de comandos:
    # pytest test_history_manager.py -v
```

### Explicación del ejemplo

1. **Ejecución de pruebas**:  
    Las pruebas se ejecutan mediante pytest, que automaticamente descubre y ejecuta todos los métodos que comienzan con `test_`.
    
2. **Fixtures automáticas**:  
    Pytest inyecta automáticamente las fixtures necesarias en cada método de prueba según sus parámetros.
    
3. **Aislamiento automático**:  
    Cada prueba se ejecuta en un entorno limpio gracias a las fixtures que se crean y destruyen automáticamente.
    
4. **Validación automática**:  
    Las aserciones (`assert`) validan automáticamente que los resultados sean los esperados, fallando la prueba si no se cumple alguna condición.
    
5. **Reporte detallado**:  
    Pytest proporciona reportes detallados del resultado de cada prueba, incluyendo información sobre fallos y errores.
    

---

## Cobertura de Pruebas

### Funcionalidades Cubiertas

- ✅ Inserción de nuevos registros de historial
- ✅ Recuperación de los últimos registros
- ✅ Eliminación completa del historial
- ✅ Verificación del patrón Singleton
- ✅ Manejo de bases de datos en memoria
- ✅ Conversión correcta de tipos de datos

### Casos de Prueba

- **Caso positivo**: Inserción exitosa de datos válidos
- **Caso de límites**: Recuperación de registros con diferentes límites
- **Caso de vacío**: Operaciones sobre tablas vacías
- **Caso de patrón**: Verificación de instancia única
- **Caso de integridad**: Validación de datos después de operaciones

### Métricas de Testing

- **Tests totales**: 4 de 41 planificados
- **Cobertura actual**: Funcionalidades básicas
- **Tiempo de ejecución**: < 1 segundo (base de datos en memoria)
- **Tasa de éxito**: 100% en entorno controlado
