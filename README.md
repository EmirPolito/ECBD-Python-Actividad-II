# Actividad II — Conociendo Python en la practica

> **Materia:** Extracción de Conocimientos de Base de Datos
> <br>

> **Alumno:** Emir Polito Guevara
> <br>

> **Actividad:** II
> <br>

---

## Descripción General

Esta actividad contiene **3 ejercicios prácticos** en Python que trabajan con listas, diccionarios, estructuras de control (`for`, `while`, `if`) y entrada/salida de datos por consola. Cada ejercicio aborda un caso de uso real y cotidiano.

---

## Estructura del Proyecto

```
Actividad-II/
├── 1-calificaciones.py   # Sistema de control de calificaciones
├── 2-inventario.py       # Gestión de inventario de productos
├── 3-estadisticas.py     # Análisis estadístico de una lista de números
└── README.md
```

---

## Ejercicios

### Ejercicio 1 — Sistema de Control de Calificaciones

**Archivo:** `1-calificaciones.py`

Programa que registra información de **5 estudiantes** (nombre y calificación) y genera un reporte completo.

**Funcionalidades:**

- Captura el nombre y calificación de 5 estudiantes mediante `input()`
- Almacena cada estudiante como un **diccionario** dentro de una lista
- Muestra el reporte completo de todos los estudiantes
- Calcula el **promedio general** del grupo
- Identifica al **mejor alumno** y su calificación más alta
- Cuenta cuántos estudiantes **aprobaron** (calificación ≥ 70)

**Conceptos aplicados:** `listas`, `diccionarios`, `bucle for`, `condicionales if`

---

### Ejercicio 2 — Inventario de Productos

**Archivo:** `2-inventario.py`

Sistema interactivo de gestión de inventario con un **menú de opciones** que se ejecuta en bucle hasta que el usuario decide salir.

**Opciones del menú:**
| Opción | Descripción |
|--------|-------------|
| 1 | Agregar un nuevo producto (nombre, precio, cantidad) |
| 2 | Mostrar todos los productos del inventario |
| 3 | Buscar un producto por nombre (sin distinción de mayúsculas) |
| 4 | Calcular el valor total del inventario (`precio × cantidad`) |
| 5 | Salir del programa |

**Conceptos aplicados:** `bucle while`, `if / elif / else`, `listas`, `diccionarios`, `.lower()` para búsqueda insensible a mayúsculas

---

### Ejercicio 3 — Estadísticas de una Lista de Números

**Archivo:** `3-estadisticas.py`

Programa que solicita **10 números enteros** al usuario y realiza un análisis estadístico completo **sin usar funciones built-in** como `max()` o `min()`.

**Estadísticas calculadas:**

- Lista completa de números ingresados
- Número **mayor** (implementado manualmente)
- Número **menor** (implementado manualmente)
- **Suma** total de los números
- **Promedio** de la lista
- Cantidad de números **pares**
- Cantidad de números **impares**
- Lista de números **mayores al promedio**

**Conceptos aplicados:** `bucle for`, `listas`, `condicionales`, operador módulo `%`, lógica de búsqueda manual

---

## Cómo Ejecutar

Asegúrate de tener **Python 3** instalado. Luego, desde la terminal:

```bash
# Ejercicio 1
python 1-calificaciones.py

# Ejercicio 2
python 2-inventario.py

# Ejercicio 3
python 3-estadisticas.py
```

---

## Requisitos

- Python **3.x**
- No se requieren librerías externas — solo la biblioteca estándar de Python

---

## Conceptos de Python Practicados

| Concepto                          | Ejercicios |
| --------------------------------- | ---------- |
| Listas (`list`)                   | 1, 2, 3    |
| Diccionarios (`dict`)             | 1, 2       |
| Bucle `for`                       | 1, 3       |
| Bucle `while`                     | 2          |
| Condicionales `if / elif / else`  | 1, 2, 3    |
| Entrada de datos (`input`)        | 1, 2, 3    |
| Formateo de cadenas (`f-strings`) | 1, 2, 3    |
| Operaciones aritméticas           | 1, 2, 3    |
| Operador módulo `%`               | 3          |
| Métodos de cadenas (`.lower()`)   | 2          |
