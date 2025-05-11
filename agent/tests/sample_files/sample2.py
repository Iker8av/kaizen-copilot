# ejemplo_avanzado.py

def dividir(a, b):
    """Devuelve el resultado de dividir a entre b, manejando división por cero."""
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    else:
        return resultado

def say_hi(nombre, saludo="Hola"):
    """Imprime un saludo personalizado, con saludo opcional."""
    print(f"{saludo}, {nombre}!")

def promedio_lista(numeros):
    """Calcula el promedio de una lista de números."""
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def contar_ocurrencias(lista):
    """Devuelve un diccionario con el conteo de ocurrencias de cada elemento."""
    conteo = {}
    for elemento in lista:
        if elemento in conteo:
            conteo[elemento] += 1
        else:
            conteo[elemento] = 1
    return conteo

# Código de prueba si ejecutas este archivo directamente
if __name__ == "__main__":
    print("División 10 / 2:", dividir(10, 2))
    print("División 10 / 0:", dividir(10, 0))

    say_hi("Iker")
    say_hi("Iker", saludo="¡Qué tal")

    lista = [1, 2, 3, 4, 5]
    print("Promedio de lista:", promedio_lista(lista))

    elementos = ["manzana", "pera", "manzana", "naranja", "pera", "manzana"]
    print("Conteo de ocurrencias:", contar_ocurrencias(elementos))