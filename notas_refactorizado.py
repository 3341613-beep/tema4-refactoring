# Programa de gestión de boletines de calificaciones
# Autor: [ESCRIBE TU NOMBRE AQUÍ]
# Fecha: [ESCRIBE LA FECHA DE HOY AQUÍ]

def calcular_media(nota1, nota2, nota3):
    """
    Calcula la media aritmética de tres calificaciones.
    
    Args:
        nota1 (float): Primera calificación del alumno.
        nota2 (float): Segunda calificación del alumno.
        nota3 (float): Tercera calificación del alumno.
        
    Returns:
        float: Valor medio de las tres notas obtenidas.
    """
    # Suma las notas recibidas y divide entre la cantidad total de evaluaciones
    return (nota1 + nota2 + nota3) / 3

def obtener_calificacion(media):
    """
    Evalúa la nota media y devuelve la calificación cualitativa correspondiente en formato texto.
    """
    # Se utiliza la estructura elif para detener la evaluación una vez se cumple la condición correcta
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def mostrar_boletin(nombre, nota1, nota2, nota3):
    """
    Imprime en consola el resumen detallado de notas y la calificación final del alumno.
    """
    # Separamos la lógica de cálculo matemático de la presentación por pantalla
    media = calcular_media(nota1, nota2, nota3)
    calificacion = obtener_calificacion(media)
    
    print("Alumno: " + nombre)
    print("Nota 1: " + str(nota1))
    print("Nota 2: " + str(nota2))
    print("Nota 3: " + str(nota3))
    print("Media: " + str(media))
    print(calificacion)
    print("------------------")

def main():
    mostrar_boletin("Ana García", 8, 7, 9)
    mostrar_boletin("Luis Pérez", 4, 5, 3)
    mostrar_boletin("Marta Gómez", 6, 7, 5)

main()