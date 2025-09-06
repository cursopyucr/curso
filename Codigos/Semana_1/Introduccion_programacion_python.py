"""
Módulo introductorio a Python: Gestión de calificaciones

Este script introduce los conceptos básicos de Python:
- Variables
- Listas
- Condicionales
- Funciones
- Bucles
Cada función está documentada usando el formato NumPy docstring.
"""

# -------------------------------
# VARIABLES
# -------------------------------

# Variable simple (string)
curso = "Introducción a Python"

# Variable numérica
nota_aprobatoria = 70

# Lista de estudiantes con sus notas
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": 60},
    {"nombre": "Sofía", "nota": 92},
    {"nombre": "Carlos", "nota": 74}
]


# -------------------------------
# FUNCIONES
# -------------------------------

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


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------
if __name__ == "__main__":
    print(f"Curso: {curso}")
    print(f"Nota mínima para aprobar: {nota_aprobatoria}")

    resultados = obtener_resultados(estudiantes, nota_aprobatoria)
    mostrar_resultados(resultados)
