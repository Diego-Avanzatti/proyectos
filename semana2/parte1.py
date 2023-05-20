'''
1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es
mayor de edad (18 años o más) o no.'''

Edad = int(input('ingrese su edad: '))

if Edad >= 18:
    print('Es mayor de edad.')
else: 
    print('No es mayor de edad.')



'''
2-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es positivo, negativo o cero.'''

num_entero= float(input('Introducir cualquier numero: '))

if num_entero == 0:
    print('El numero es cero')
elif num_entero > 0:
    print('Es positivo')
else: 
    print('Es negativo')


'''
3-Escribir un programa que pida al usuario dos números y muestre por pantalla
cuál de ellos es mayor.'''

num1= int(input('introducir un numero: '))
num2= int(input('introducir un numero: '))

if num1 > num2:
    print(f'{num1} es mayor a {num2}.')
elif num1 < num2:
    print(f'{num2} es mayor a {num1}.')
else:
    print('Son iguales')



'''
4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
pantalla si está aprobado (5 o más) o no.'''

nota= int(input('introducir una nota del 0 al 10: '))

if nota >= 5:
    print('Esta aprobado')
elif nota < 5:
    print('Esta desaprobado')


'''
5-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es par o impar.
'''
num = int(input('introducir un numero: '))
if num % 2 == 0:
    print(f'{num}, es par.')
else:
    print(f'{num}, es impar.')

'''
6-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es múltiplo de 2 y de 3 a la vez.'''

num = int(input('introducir un numero: '))
if num % 2 == 0:
    print(f'{num}, es multiplo de 2.')
if num % 3 == 0:
    print(f'{num}, es multiplo de 3.')
else:
    print(f'{num}, no es multiplo de 2 o de 3.')


'''
7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
es una letra mayúscula, una letra minúscula, un número o un carácter especial.'''

caracter = input('introducir un caracter: ')

if(caracter.isalpha()):
    if(caracter.islower()):
        print("Es una letra minuscula")
    else:
        print("Es una letra mayuscula")
elif(caracter.isdigit()):
    print("Es numero")
else:
    print("Es un caracter especial")

'''8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
por pantalla si contiene la letra "a".'''

cadena = input('introducir cadena de texto: ')

for i in range(len(cadena)):
    if cadena[i] == 'a' or cadena[i] == 'A':
        print('contiene la letra A')
        break


'''9-Escribir un programa que pida al usuario tres números y muestre por pantalla
el mayor de ellos.'''

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el ssegundo numero: '))
num3 = int(input('Ingrese el tercero numero: '))

num_mayor = num1

if num2 > num_mayor:
    num_mayor = num2

if num3 > num_mayor:
    num_mayor = num3

print('El numero mayor es: ',num_mayor)



'''10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
una vocal o una consonante.'''

letra = input(' Ingresar una letra: ')

letra = letra.lower()
vocales = [ 'a','e','i','o','u']

if letra in vocales:
    print('La letra es una vocal')
else: 
    print('Es una consonate')

'''11-Escribir un programa que pida al usuario dos números y muestre por pantalla
la suma de ellos solo si ambos son pares.
'''

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    suma = num1 + num2
    print("La suma de los números es:", suma)
else:
    print("Al menos uno de los números no es par.")


''' FIN'''