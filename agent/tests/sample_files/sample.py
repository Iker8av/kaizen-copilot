def saludar(nombre):
    """Imprime un saludo personalizado."""
    print(f"Hola, {nombre}!")

def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def es_par(numero):
    """Devuelve True si el número es par, False si es impar."""
    return numero % 2 == 0

def factorial(n):
    """Calcula el factorial de un número de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def lista_pares(hasta):
    """Devuelve una lista de números pares hasta un número dado."""
    return [x for x in range(hasta + 1) if es_par(x)]

# Código de prueba si ejecutas este archivo directamente
if __name__ == "__main__":
    saludar("Iker")
    print("Suma de 3 + 4:", sumar(3, 4))
    print("¿Es 10 par?", es_par(10))
    print("Factorial de 5:", factorial(5))
    print("Lista de pares hasta 10:", lista_pares(10))
    
    print("Mariana Bustos")