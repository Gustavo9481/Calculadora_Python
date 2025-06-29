# Calculadora Python

<p align="center">
  <img src="calculator.svg" alt="Ícono de Calculadora" width="150"/>
</p>


<p align="center">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build Status">
  <img src="https://img.shields.io/badge/PyQt-5.15+-orange.svg" alt="PyQt Version">
</p>



## Descripción General

**Calculadora Python** es una aplicación de calculadora de escritorio construida con Python y el framework PyQt para su interfaz gráfica de usuario. Ofrece operaciones aritméticas estándar con alta precisión y mantiene un historial de cálculos. El proyecto enfatiza una arquitectura limpia y modular, haciéndola fácil de entender y mantener.

## Capturas de Pantalla

### Interfaz Principal
![Calculadora Principal](docs/screenshots/main-interface.png)
*Vista principal de la calculadora con botones numéricos y operaciones básicas*

### Historial de Cálculos
![Historial](docs/screenshots/history-view.png)
*Panel de historial mostrando cálculos anteriores*

### Demo en Vivo
![Demo de la Calculadora](docs/demo.gif)
*Demostración de las funcionalidades principales*

## Características

*   **Interfaz Gráfica de Usuario (GUI):** Interfaz intuitiva y responsiva impulsada por PyQt.
*   **Operaciones Aritméticas Estándar:**
    *   Suma (+)
    *   Resta (-)
    *   Multiplicación (×)
    *   División (÷)
    *   Porcentaje (%)
*   **Cálculos de Alta Precisión:** Utiliza el módulo `decimal` de Python para asegurar precisión, especialmente importante para cálculos financieros o científicos.
*   **Historial Persistente de Cálculos:** Guarda automáticamente el historial de cálculos en una base de datos SQLite local, permitiendo a los usuarios revisar operaciones pasadas.
*   **Arquitectura Modular:** Separación bien definida de responsabilidades entre la interfaz de usuario, la lógica de cálculo y las capas de persistencia de datos.

## Inicio Rápido

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd proyecto-calculadora-python

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python main.py
```

## Descripción de la Arquitectura

La aplicación está diseñada con un enfoque modular, con componentes clave que incluyen:

*   **`AppCalculator`**: El orquestador principal de la aplicación. Inicializa la UI y la conexión a la base de datos, actuando como una Fachada para simplificar el proceso de inicio.
*   **Componentes de UI (`InterfaceCreator`, `ButtonsCreator`, `ScreensCreator`)**: Estas clases son responsables de construir y manejar los diversos elementos de la interfaz gráfica basada en PyQt.
*   **`Calculator`**: Una clase utilitaria sin estado que proporciona métodos estáticos para todas las operaciones aritméticas. Utiliza `Decimal` para precisión y `lru_cache` para optimización de rendimiento.
*   **`HistoryManager`**: Maneja todas las interacciones con la base de datos SQLite para almacenar y recuperar el historial de cálculos. Está implementado como un Singleton para asegurar una sola conexión a la base de datos.
*   **`HistoryTableDB`**: Un Objeto de Transferencia de Datos (DTO) utilizado para manejar registros del historial.

<figure markdown="span">
  ![Módulos](modulos.svg){ width="400" }
</figure>

Se emplean varios patrones de diseño para mejorar la estructura y mantenibilidad del código:
*   **Patrón Fachada**: Utilizado por `AppCalculator` para proporcionar una interfaz simplificada a los subsistemas complejos de inicialización de UI y base de datos.
*   **Patrón Singleton**: Asegura que `HistoryManager` tenga solo una instancia, gestionando el acceso a la base de datos de forma centralizada.
*   **Clase Utilitaria Sin Estado**: La clase `Calculator` agrupa funciones aritméticas relacionadas sin mantener ningún estado interno.

## Stack Tecnológico

*   **Lenguaje de Programación:** Python (versión 3.7 o superior)
*   **Framework GUI:** PyQt (probado con PyQt5, adaptable para PyQt6)
*   **Base de Datos:** SQLite (a través del módulo integrado `sqlite3` de Python)
*   **Aritmética de Precisión:** Módulo `decimal` de Python
*   **Caché:** `functools.lru_cache` para optimizar cálculos

## Prerrequisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado lo siguiente:

*   Python 3.7 o más reciente
*   PIP (instalador de paquetes de Python)

## Instalación

1.  **Clonar el repositorio (si aplica):**
    ```bash
    git clone https://github.com/Gustavo9481/Calculadora_Python.git
    cd proyecto-calculadora-python
    ```
    Si tienes los archivos localmente, navega al directorio raíz del proyecto.

2.  **Instalar dependencias:**
    La dependencia externa principal es PyQt. Puedes instalarla usando pip:
    ```bash
    pip install PyQt5
    ```
    *(Nota: Si planeas usar una versión diferente, como PyQt6, instala esa en su lugar: `pip install PyQt6`)*

    O usar el archivo de requirements:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar la aplicación calculadora, ejecuta el script principal desde el directorio raíz del proyecto:

```bash
python main.py
```


### Operaciones Básicas
- **Números:** Haz clic en los botones numéricos para ingresar números
- **Operaciones:** Usa +, -, ×, ÷ para operaciones básicas
- **Porcentaje:** Usa el botón % para cálculos de porcentaje

## Estructura del Proyecto

<figure markdown="span">
  ![Estructura de archivos](tree.svg){ width="500" }
</figure>

## Documentación

Este proyecto utiliza MkDocs para generar documentación. Puedes encontrar información detallada sobre clases, métodos y arquitectura en el directorio `docs`.

Para servir la documentación localmente:

1.  **Instalar MkDocs y el tema Material (si no se ha hecho ya):**
    ```bash
    pip install mkdocs mkdocs-material
    ```
2.  **Servir la documentación:**
    Desde el directorio raíz del proyecto, ejecuta:
    ```bash
    mkdocs serve
    ```
    Esto iniciará un servidor local, y podrás ver la documentación en tu navegador web (usualmente en `http://127.0.0.1:8000`).

Para construir el sitio de documentación estática:
```bash
mkdocs build
```

## Roadmap

### Versión Actual (1.0.0)
- [x] Operaciones aritméticas básicas (+, -, ×, ÷)
- [x] Cálculos de porcentaje
- [x] Historial persistente de cálculos
- [x] Interfaz gráfica con PyQt
- [x] Arquitectura modular

### Próximas Versiones
- [ ] **v1.1.0** - Calculadora Python
  - [ ] Temas personalizables (claro/oscuro)
  - [ ] Interfaz para historial de operaciones

## Problemas Conocidos

- **Windows 7**: Puede requerir instalación manual de Visual C++ Redistributable
- **División por cero**: Muestra mensaje de error estándar, considerar implementar manejo más elegante
- **Números muy grandes**: El rendimiento puede verse afectado con números extremadamente grandes (>1000 dígitos)
- **PyQt6**: Algunas importaciones pueden necesitar ajustes menores al migrar desde PyQt5


## Contribución

¡Las contribuciones son bienvenidas! Aquí te explicamos cómo puedes ayudar:

### Proceso de Contribución
1. **Fork** el proyecto
2. Crea una **rama** para tu feature (`git checkout -b feature/CaracteristicaIncreible`)
3. **Commit** tus cambios (`git commit -m 'Agregar CaracteristicaIncreible'`)
4. **Push** a la rama (`git push origin feature/CaracteristicaIncreible`)
5. Abre un **Pull Request**

### Tipos de Contribuciones
- 🐛 **Reportar bugs** - Crea un issue describiendo el problema
- 💡 **Sugerir features** - Propón nuevas características
- 📝 **Mejorar documentación** - Ayuda a hacer la documentación más clara
- 🔧 **Escribir código** - Implementa nuevas funcionalidades o arregla bugs
- 🧪 **Escribir tests** - Mejora la cobertura de pruebas

### Guías de Contribución
- Sigue las convenciones de código Python (PEP 8)
- Escribe tests para nuevas funcionalidades
- Actualiza la documentación cuando sea necesario
- Usa mensajes de commit descriptivos

### Configuración del Entorno de Desarrollo
```bash
# Clonar tu fork
git clone https://github.com/tu-usuario/proyecto-calculadora-python.git
cd proyecto-calculadora-python

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# Ejecutar tests
python -m pytest tests/
```


## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

### Resumen de la Licencia MIT
- ✅ Uso comercial permitido
- ✅ Modificación permitida
- ✅ Distribución permitida
- ✅ Uso privado permitido
- ❌ Sin garantía
- ❌ El autor no es responsable por daños

## Autores

- **[GUScode | Gustavo Colmenares]** - *Desarrollo inicial y mantenimiento* - [Gustavo9481](https://github.com/Gustavo9481)

## Agradecimientos

- Inspirado por la calculadora estándar de Android.
- Iconos proporcionados por [Phosphoricons](https://phosphoricons.com)
- Documentación mejorada gracias a [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- Comunidad de Python por las excelentes librerías utilizadas


---

<p align="center">
  <strong>¿Te gusta el proyecto? ¡Dale una ⭐ en GitHub!</strong>
</p>

<p align="center">
  Hecho con ❤️ por la comunidad de desarrolladores Python
</p>

