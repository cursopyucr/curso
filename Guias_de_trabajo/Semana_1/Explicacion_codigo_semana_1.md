# Introducción a Python: Conceptos básicos con ejemplo práctico

Este documento presenta los **conceptos básicos de programación en Python** utilizando un ejemplo de **gestión de calificaciones** de estudiantes.

Es importante tener en cuenta que este ejemplo no es un programa real, sino una **simulación** de un programa que podría ser utilizado en un proyecto real. Y además, consideraremos el uso de documentación en el código mediante el uso de **NumPy docstring**. 

Para más detalles puede acceder al siguiente [enlace](https://numpydoc.readthedocs.io/en/latest/format.html). (Para ver como funciona numpydoc). Este ejemplo, se puede ejecutar directamente desde el editor de código en la carpeta `c:/Users/Public/Documents/Curso_python/GitHub/curso/Codigos/Semana_1/`.

## 1. Variables

Las **variables** son espacios en memoria donde guardamos información para usarla después.  
En Python no es necesario declarar el tipo de dato; se infiere automáticamente.

```python
curso = "Introducción a Python"  # Cadena de texto (string)
nota_aprobatoria = 70           # Número entero (int)
```

---

## 2. Tipos de datos básicos

- **int** → Números enteros: `10`, `-3`, `0`
- **float** → Números decimales: `3.14`, `-1.5`
- **str** → Cadenas de texto: `"Hola"`, `'Python'`
- **bool** → Valores lógicos: `True`, `False`

Ejemplo en el código:
```python
curso = "Introducción a Python"  # str
nota_aprobatoria = 70           # int
```

---

## 3. Listas

Las **listas** son colecciones ordenadas de elementos.  
Pueden contener cualquier tipo de dato, incluso otros diccionarios o listas.

```python
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": 60},
    {"nombre": "Sofía", "nota": 92},
    {"nombre": "Carlos", "nota": 74}
]
```

En este ejemplo:
- Cada elemento de la lista es un **diccionario** con las claves `"nombre"` y `"nota"`.

---

## 4. Condicionales (`if`, `elif`, `else`)

Sirven para ejecutar código **solo si** se cumple cierta condición.

```python
if nota >= nota_minima:
    print("Aprobado")
elif nota >= 60:
    print("Recuperación")
else:
    print("Reprobado")
```

En nuestro ejemplo:
```python
if es_aprobado(estudiante["nota"], nota_minima):
    aprobados.append(estudiante["nombre"])
else:
    reprobados.append(estudiante["nombre"])
```

---

## 5. Funciones

Las **funciones** agrupan código que realiza una tarea específica y que podemos reutilizar.

### Sintaxis
```python
def nombre_funcion(parametros):
    # código
    return resultado
```

En nuestro ejemplo:
```python
def es_aprobado(nota, nota_minima):
    return nota >= nota_minima
```

---

## 6. Documentación de funciones con **NumPy docstring**

Es un estándar para documentar funciones en Python, indicando:
- **Parámetros**
- **Tipos de datos**
- **Valor de retorno**
- **Descripción**

Ejemplo:
```python
def es_aprobado(nota, nota_minima):
    """
    Determina si una nota es aprobatoria.

    Parameters
    ----------
    nota : int or float
        Nota obtenida por el estudiante.
    nota_minima : int or float
        Nota mínima para aprobar.

    Returns
    -------
    bool
        True si la nota es mayor o igual a la nota mínima, False en caso contrario.
    """
    return nota >= nota_minima
```

---

## 7. Bucles (`for` y `while`)

Los **bucles** permiten repetir código varias veces.

### Bucle `for`
Recorre una secuencia de elementos.
```python
for estudiante in estudiantes:
    print(estudiante["nombre"])
```

### Bucle `while`
Se repite **mientras** se cumpla una condición.
```python
contador = 0
while contador < 3:
    print("Intento", contador)
    contador += 1
```

En el ejemplo, usamos `for` para procesar todos los estudiantes.

---

## 8. Ejemplo completo

```python
curso = "Introducción a Python"
nota_aprobatoria = 70

estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": 60},
    {"nombre": "Sofía", "nota": 92},
    {"nombre": "Carlos", "nota": 74}
]

def es_aprobado(nota, nota_minima):
    """
    Determina si una nota es aprobatoria.

    Parameters
    ----------
    nota : int or float
        Nota obtenida por el estudiante.
    nota_minima : int or float
        Nota mínima para aprobar.

    Returns
    -------
    bool
        True si la nota es mayor o igual a la nota mínima, False en caso contrario.
    """
    return nota >= nota_minima

def obtener_resultados(lista_estudiantes, nota_minima):
    """
    Procesa la lista de estudiantes para determinar quién aprueba y quién reprueba.

    Parameters
    ----------
    lista_estudiantes : list of dict
        Lista con diccionarios que contienen 'nombre' y 'nota'.
    nota_minima : int or float
        Nota mínima para aprobar.

    Returns
    -------
    dict
        Diccionario con dos claves:
        - 'aprobados': lista de nombres de estudiantes aprobados.
        - 'reprobados': lista de nombres de estudiantes reprobados.
    """
    aprobados = []
    reprobados = []

    for estudiante in lista_estudiantes:
        if es_aprobado(estudiante["nota"], nota_minima):
            aprobados.append(estudiante["nombre"])
        else:
            reprobados.append(estudiante["nombre"])

    return {"aprobados": aprobados, "reprobados": reprobados}

def mostrar_resultados(resultados):
    """
    Imprime en pantalla los estudiantes aprobados y reprobados.

    Parameters
    ----------
    resultados : dict
        Diccionario con listas de estudiantes aprobados y reprobados.
    """
    print("\n--- Resultados ---")
    print("Aprobados:")
    for nombre in resultados["aprobados"]:
        print(f" - {nombre}")

    print("Reprobados:")
    for nombre in resultados["reprobados"]:
        print(f" - {nombre}")

# Programa principal
if __name__ == "__main__":
    print(f"Curso: {curso}")
    print(f"Nota mínima para aprobar: {nota_aprobatoria}")

    resultados = obtener_resultados(estudiantes, nota_aprobatoria)
    mostrar_resultados(resultados)
```

---

Este ejemplo cubre:
- Variables y tipos de datos
- Listas y diccionarios
- Condicionales
- Funciones
- NumPy docstring
- Bucles `for` y `while`
