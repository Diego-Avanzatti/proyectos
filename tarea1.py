'''
1-Escribe un programa que solicite al usuario su nombre y lo imprima en la
pantalla.
'''

nombre = input("Introducir su nombre")
print(nombre) 

'''
2-Escribe un programa que solicite al usuario su nombre y luego imprima un
mensaje de bienvenida.'''

nombre = input("Introdusca su nombre: ")
print("bienvenido," + nombre )

'''
3-Crea un programa que pida al usuario su edad y lo imprima en pantalla.
'''
edad = input("Introdusca su edad: ")
print(edad)


'''
4-Crea un programa que calcule la suma de dos números y lo imprima en
pantalla.
'''
a= 12
b= 10
suma = a + b 
print(suma)

'''
5-Crea un programa que pida al usuario dos números enteros y muestre en
pantalla su cociente y su resto.
'''

a = int(input("introdusca un numero:"))
b = int(input("introdusca un numero:"))

cociente = a//b
print(cociente)

resto= a%b
print(resto)


'''
6-Crea un programa que pida al usuario el radio de un círculo y calcule su área.
La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
Supongamos que pi = 3.1416 '''

radio= float(input("radio del circulo"))

area= 3.1416 * radio**2
print(area)

'''
7-Escribe un programa que calcule el área de un triángulo a partir de la base y la
altura dadas. '''

base = float(input("instrodusca la base:"))
altura = float(input("instrodusca altura:"))

area = (base * altura) /2
print(area)


'''
8-Crea un programa que pida al usuario el radio de un círculo y muestre su
diámetro, su circunferencia y su área.
Supón que pi es aproximadamente 3.14159.
'''

radio = float(input("introducir radio: "))

area= 3.1416 * radio**2
print(area)

diametro = radio *2
print(diametro)

circunferencia = 2 * 3.1416 * radio 
print(circunferencia)

'''
9-Escribe un programa que solicite al usuario dos números y luego imprima la
suma, la resta, la multiplicación y la división de los dos números '''

a = float(input("introdusca un numero:"))
b = float(input("introdusca un numero:"))

suma=a+b
print(suma)
resta=a-b
print(resta)
multiplicacion= a*b
print(multiplicacion)
division= a/b
print(division)

'''
10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a
euros.
Supón que el tipo de cambio es de 0.84 euros por dólar.
'''

dolar = float(input("cantidad de dolares: "))

euros= dolar * 0.84
print(euros)

'''
11-Crea un programa que pida al usuario una palabra y muestre en pantalla
cuántas letras tiene.
Pss psssss toma... .len() '''

palabra = input("introducir una palabra: ")
print(len(palabra))

'''
12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
dd/mm/aaaa y luego imprima su edad en años.
Utiliza la función .split()
'''

























