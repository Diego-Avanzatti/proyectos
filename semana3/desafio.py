import random

nombre = input("Ingrese su nombre: ")

print("¡Bienvenido(a),", nombre + "!")


print("El número a adivinar está entre 1 y 100.")
print("Tienes 8 intentos para adivinarlo.")


numero_adivinar = random.randint(1, 100)

intentos_restantes = 8

while intentos_restantes > 0:
    numero_ingresado = input("Ingresa un número: ")

    
    if not numero_ingresado.isdigit():
        print("No has ingresado un número entero.")
        continue

    numero_ingresado = int(numero_ingresado)

    
    if numero_ingresado < numero_adivinar:
        print("El número a adivinar es mayor.")
    elif numero_ingresado > numero_adivinar:
        print("El número a adivinar es menor.")
    else:
        intento_actual = 8 - intentos_restantes + 1
        print("¡Felicidades,", nombre + "! Has adivinado el número en el intento", intento_actual)
        break

    intentos_restantes -= 1
    print("Intentos restantes:", intentos_restantes)

if intentos_restantes == 0:
    print("Se agotaron los intentos. El número a adivinar era", numero_adivinar)
