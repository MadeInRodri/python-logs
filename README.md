# Analizador de logs en Python

## Descripción

Proyecto académico que utiliza la inteligencia artificial como asistente para crear un script de Python que analiza archivos de logs de texto. El programa permite elegir un archivo desde un menú en la consola y genera un reporte con el conteo de niveles de severidad y la validación de fechas.

La IA se utiliza como apoyo durante el desarrollo y la comprensión del código; la revisión, adaptación y uso del resultado forman parte del trabajo del autor.

## Funcionalidades

- Busca archivos `.txt` y `.log` en la carpeta actual.
- Muestra los archivos disponibles en un menú numerado.
- Permite seleccionar el archivo que se desea analizar.
- Cuenta los niveles `[INFO]`, `[WARNING]` y `[ERROR]`.
- Procesa cada evento en una sola pasada por el archivo.
- Muestra el total de eventos procesados y los conteos de severidad.
- Valida que cada evento incluya un nivel de severidad, una fecha y un mensaje.
- Valida la fecha ubicada como segunda palabra de cada línea. Los formatos aceptados son `AAAA-MM-DD` y `DD/MM/AAAA`.
- Comprueba que las fechas sean válidas en el calendario.
- Cuenta cada evento inválido una sola vez, aunque pueda tener más de un problema. Los contadores de cada problema son métricas independientes y pueden solaparse.
- Presenta los resultados en un reporte en la consola.

## Requisitos

- Python 3.
- No se requieren dependencias externas.

## Librerías y tecnologías utilizadas

- **Python 3:** lenguaje de programación del proyecto.
- **`re` (biblioteca estándar):** valida la estructura de las fechas mediante expresiones regulares.
- **`datetime` (biblioteca estándar):** comprueba que la fecha exista en el calendario.
- **`pathlib` (biblioteca estándar):** busca archivos en la carpeta actual.
- **Consola:** interfaz para elegir un archivo y consultar el reporte.
- **Inteligencia artificial:** herramienta de asistencia para crear, explicar y documentar el script.

## Uso

Ejecuta el script desde la carpeta que contiene los archivos de log:

```bash
python main.py
```

El programa mostrará un menú similar a este:

```text
Elija el archivo log a leer:
[1] case_1.txt
[2] case_2.txt
```

Ingresa el número correspondiente al archivo que deseas analizar. El reporte mostrará el total de eventos, los conteos por severidad, las fechas correctas e incorrectas, los mensajes faltantes y el total de eventos inválidos.

## Casos de uso a probar

1. **Selección válida:** elegir un archivo disponible y comprobar que se genera el reporte para ese archivo.
2. **Opción fuera del menú:** ingresar `0` o un número mayor a la cantidad de archivos; el programa debe pedir una opción válida.
3. **Entrada no numérica:** ingresar texto en lugar de un número; el programa debe rechazarlo y volver a solicitar la selección.
4. **Sin archivos compatibles:** ejecutar el script en una carpeta sin archivos `.txt` ni `.log`; debe informar que no encontró archivos.
5. **Fechas aceptadas:** probar `2025-01-10` y `13/01/2025`; ambas deben contarse como correctas.
6. **Formato de fecha no permitido:** probar una fecha como `10-01-2025`; debe contarse como incorrecta.
7. **Fecha inexistente:** probar una fecha con estructura correcta pero inválida, como `2025-99-99`; debe contarse como incorrecta.
8. **Fecha faltante:** probar una línea que no tenga una segunda palabra; debe contarse como fecha incorrecta y como evento inválido.
9. **Niveles de severidad:** probar `[INFO]`, `[WARNING]` y `[ERROR]`, además de un nivel desconocido como `[DEBUG]`, y comprobar sus conteos.
10. **Mensaje faltante:** probar `[INFO] 2025-01-10` sin texto después de la fecha; debe contarse como evento inválido.
11. **Varios problemas en un evento:** combinar una severidad desconocida, una fecha incorrecta o un mensaje faltante; cada evento debe incrementar el total de eventos inválidos una sola vez.
12. **Total de eventos:** comprobar que coincida con el número de líneas del archivo, incluidas las vacías.
13. **Línea vacía o severidad mal formada:** comprobar que se cuente como un evento inválido.

## Archivos de ejemplo

- `case_1.txt`: contiene logs con niveles de severidad y fechas en el formato `AAAA-MM-DD`.
- `case_2.txt`: contiene ejemplos de fechas válidas e inválidas y variaciones en los niveles de severidad.
- `case_3.log`: verifica que el programa también analice archivos `.log`, con fechas válidas e inválidas y distintos niveles de severidad.

## Fuente consultada

- [Cómo abrir y leer un archivo de texto línea por línea en Python — freeCodeCamp Español](https://www.freecodecamp.org/espanol/news/python-abre-archivo-como-leer-un-archivo-de-texto-linea-por-linea/)
