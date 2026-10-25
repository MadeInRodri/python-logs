# Evidencias

## Reflexión Técnica

### Partes sugeridas por la IA

- La IA sugirió utilizar la utilidad de python 're' para poder crear regex y evaluar que los patrones en los tipos de logs y las fechas sean correctos.
- La IA sugirió utilizar la librería 'pathlib' para poder escanear la carpeta actual y permitirle al usuario elegir por medio de la consola que archivo quiere que el script analice.

### Decisiones tomadas

- Decidí limitar los logs válidos a 3 en concreto [INFO, WARNING, ERROR], ya que podría haber otra palabra distinta como primer parámetro en el log, como en el caso 2 y 3 con [DEBUG], el cual al no estar registrado en la lista de logs válidos se marca como error.
- Decidí limitar las fechas a dos formatos válidos: (AAAA-MM-DD, DD/MM/AAAA), por lo cual si están en un orden distinto, o con un número de fecha inválido se marca la línea como error.
- Decidí que el script valide que existan como mínimo 3 partes de un log, y que si el orden de las partes es alterado se marque como inválido.

### Ejemplo de algo incorrecto

La IA utilizada en este proyecto fue el agente Github Copilot, el cual inicialmente sugirió dividir en 2 funciones distintas los procesos de detectar el tipo de log y reconocer el formato correcto de la fecha, pero el archivo debía ser abierto dos veces durante el flujo del algoritmo, por lo que tomaría el doble de trabajo con archivos muy grandes.

### Como se corrigió

Al trabajar los eventos dos veces, ya que se requerían de dos funciones, el algoritmo podía marcar 2 errores en un mismo log, lo que ocasionaba que no existiera una cuenta exacta de los logs que contenían errores, lo cual se corrigió al manejar la operación en una sola lectura.

### Que es lo que aprendí

La IA puede ser una herramienta muy versátil a la hora de acompañarnos en la creación de un script, durante este trabajo descubrí nuevas funciones y formas de validar datos de una manera muy óptima que si no fuera por la IA me hubiera tomado horas de investigación, gracias a esto pude centrarme en el flujo principal del algoritmo y en lo que quería lograr que hiciera, además de darle un resultado visualmente agradable al usuario final delegando la tarea de la presentación final del reporte de los logs a la IA, como programador me parece que es una herramienta que no reemplaza mi trabajo ni mi criterio, sino que potencia la forma en la que programo y me ayuda a ser más productivo.

## Casos probados

### case_1.txt

```text
==============================================
REPORTE DE LOGS
==============================================
Archivo analizado : case_1.txt
Total de eventos : 7
Eventos válidos : 6
Eventos inválidos : 1

---

Niveles de severidad
Información : 3
Advertencias : 2
Errores : 2
Severidad inválida: 0

---

Validación de eventos
Fechas correctas : 6
Fechas incorrectas: 1
Mensajes faltantes: 0
==============================================
```

### case_2.txt

```text
==============================================
REPORTE DE LOGS
==============================================
Archivo analizado : case_2.txt
Total de eventos : 10
Eventos válidos : 4
Eventos inválidos : 6

---

Niveles de severidad
Información : 3
Advertencias : 2
Errores : 2
Severidad inválida: 3

---

Validación de eventos
Fechas correctas : 6
Fechas incorrectas: 4
Mensajes faltantes: 1
==============================================
```

### case_3.log

```text
==============================================
REPORTE DE LOGS
==============================================
Archivo analizado : case_3.log
Total de eventos : 8
Eventos válidos : 4
Eventos inválidos : 4

---

Niveles de severidad
Información : 3
Advertencias : 2
Errores : 2
Severidad inválida: 1

---

Validación de eventos
Fechas correctas : 5
Fechas incorrectas: 3
Mensajes faltantes: 0
==============================================
```
