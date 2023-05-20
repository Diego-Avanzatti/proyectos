'''1-Escribe un programa que pida al usuario una palabra y luego imprima cada
letra de la palabra en una línea separada. '''

palabra = input("Ingresa una palabra: ")

for letra in palabra:
    print(letra)


'''
2-Escribe un programa que pida al usuario un número y calcule la suma de todos
los números naturales del 1 hasta ese número.
'''
num = int(input('Introduce un número: '))

suma = 0

for i in range(1, num + 1):
    suma += i

print(suma)




'''3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
multiplicar correspondiente a ese número del 1 al 10.
'''
numero = int(input("Ingresa un número: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)


'''4-Escribe un programa que imprima los números pares del 1 al 100.'''

for i in range(1,101):
    if i % 2 == 0:
        print('numero pares: ',i)
    
'''5-Escribe un programa que imprima la suma de todos los números pares del 1 al
100.
'''

suma = 0

for i in range(2, 101 + 2):
    suma+= i

print(suma)


'''6-Escribe un programa que pida al usuario una palabra y luego imprima la misma
palabra pero con las letras en orden inverso.
'''
palabra = input('Introsucir una palabra: ')
palabra_inversa = palabra[::-1]

print(palabra_inversa)




''' 7-Escribe un programa que pida al usuario una palabra y determine si es un
palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
izquierda).'''

palabra = input('Introsucir una palabra: ')
palabra.lower()

palabra_ivertida = palabra[::-1]

if palabra_ivertida == palabra:
    print('la palabra' , palabra, 'es polindromo')
else: 
    print('la palabra', palabra, 'no es polindromo')


''' 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
el número de palabras que contiene.'''

texto = input('Introduce un texto: ')
palabras = texto.split()

num_palabras = len(palabras)

print('El número de palabras es:', num_palabras)




'''9-Escribe un programa que pida al usuario un número y luego imprima la
secuencia de Fibonacci correspondiente a ese número.
'''
num = int(input("Ingrese un número: "))


fibonacci = [0, 1]

while fibonacci[-1] < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

for i in fibonacci:
    if i <= num:
        print(i, end=" ")



'''
10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con todas las vocales en mayúscula.'''

texto = input('Introduce un texto: ')
vocales = ['a', 'e', 'i', 'o', 'u']
texto_modificado = ""

for caracter in texto:
    if caracter.lower() in vocales:
        caracter = caracter.upper()
    texto_modificado += caracter

print("La cadena modificada es:", texto_modificado)

'''
11-Escribe un programa que pida al usuario un número y calcule su factorial.
Un factorial es el producto que resulta de multiplicar un número entero positivo
dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
de 4 es 4! = 4 × 3 × 2 × 1 = 24.
'''
numero = int(input("Ingrese un número entero positivo: "))

# Verificar si el número es cero o negativo
if numero < 0:
    print("El número debe ser positivo.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print("El factorial de", numero, "es", factorial)


'''12-Escribe un programa que pida al usuario una lista de números separados por
comas y calcule su promedio.
'''
numeros = input("Ingrese una lista de números separados por comas: ")
lista_numeros = numeros.split(",")
suma = 0

for numero in lista_numeros:
    suma += float(numero)

promedio = suma / len(lista_numeros)
print("El promedio de los números es:", promedio)



'''13-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de asteriscos con esa cantidad de filas.
*
**
***
****
*****
'''

numero = int(input("Ingrese un número entero: "))

for i in range(1, numero + 1):
    print('*' * i)


'''14-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
numero = int(input("Ingrese un número entero: "))

for i in range(1, numero + 1):
    fila = ""
    for j in range(i):
        fila += str(i) + " "
    print(fila)


'''15-Escribe un programa que pida al usuario una cadena de texto y determine
cuántas veces aparece cada letra en la cadena.'''

texto = input("Introduce una cadena de texto: ")
frecuencia_letras = {}

for letra in texto:
    if letra in frecuencia_letras:
        frecuencia_letras[letra] += 1
    else:
        frecuencia_letras[letra] = 1

print("Frecuencia de letras en el texto:")


'''16-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con cada palabra al revés.'''

texto = input("Introduce una cadena de texto: ")
palabras = texto.split()
texto_invertido = ""

for palabra in palabras:
    texto_invertido += palabra[::-1] + " "

print("Cadena invertida por palabras:")
print(texto_invertido)


'''17-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con las palabras en orden inverso.'''

texto = input("Introduce una cadena de texto: ")
palabras = texto.split()
texto_inverso = " ".join(palabras[::-1])

print("Cadena con las palabras en orden inverso:")
print(texto_inverso)


'''18-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
1
2 3
4 5 6
7 8 9 10
'''
numero = int(input("Ingrese un número entero: "))

num = 1
for i in range(1, numero + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()




''' 19-Escribe un programa que pida al usuario un número y luego imprima si ese
número es un número perfecto o no. Un número perfecto es aquel que es igual a
la suma de sus divisores propios (excluyendo el propio número).
Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6
'''

numero = int(input("Ingrese un número entero: "))
suma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        suma_divisores += i

if suma_divisores == numero:
    print(numero, "es un número perfecto.")
else:
    print(numero, "no es un número perfecto.")



'''FIN'''