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
import datetime 

print("ingrese su fecha de nacimiento dd/mm/aaaa")
fecha_nac = input()
dia, mes, anio = map(int, fecha_nac.split('/'))

fecha_act = datetime.date.today()
anio_hoy = fecha_act.year
mes_hoy = fecha_act.month
dia_hoy = fecha_act.day

edad = anio_hoy - anio

if(mes > mes_hoy):
    edad = edad -1
    print('tu edad actual es de '+ str(edad)+' años')
elif((mes==mes_hoy) and (dia==dia_hoy)):
    print("feliz cumple numero", edad, "años")
elif((mes==mes_hoy) and (dia > dia_hoy)):
    print("feliz cumple numero", edad," años, atrasado")
elif((mes==mes_hoy) and (dia < dia_hoy)):
    print("falta poco para tu cumple numero", edad)


'''
13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.'''

nombre=str(input('como se llama '))
edad=int(input(f'Hola {nombre} ingrese su edad: '))
print(f'{nombre}, en 10 años tendras {edad + 10}')


'''
14-Escribe un programa que solicite al usuario un número entero y luego
imprima el doble y el triple de ese número.'''

numero_entero = int(input('Ingrese un numero entero: '))
print(f' El doble  de {numero_entero} es: {numero_entero * 2} y el triple es: {numero_entero* 3 }')


'''
15-Escribe un programa que solicite al usuario una temperatura en grados
Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.'''

temperatura = float(input('introducir temperatura en grados celsius: '))
print(f' la temperatura en grados Fahrenheit es: {temperatura*1.8 +32}')

'''16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
e imprima su índice de masa corporal (IMC).
La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).
'''
peso = float(input('introduzca su peso:'))
altura = float(input('introduzca su altura:'))
print(f' su imc es de: {round(peso/(altura**2))}')

'''17-Escribe un programa que solicite al usuario dos palabras y luego las imprima
en orden inverso.
Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
"mundo hola".
Importante!!! Utiliza un solo print() 😈.
'''
palabras = input('introducir 2 palabras: ')
palabras_invertidas= palabras.split(" ")
print(" ".join(reversed(palabras_invertidas)))


'''
18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de
residencia, y lo muestre en pantalla Utilizando una sola línea de código.
*Recuerda el print() del ejercicio anterior 🤫
'''

nombre = input('introducir su nombre: ')
edad = int(input('introducir su edad: '))
ciudad_residencia= input('introducir su ciudad de residencia: ')
print(f'su nombre es: {nombre}, su edad es: {edad}  y su ciudad de residencia es: {ciudad_residencia}.')

'''
19-Escribe un programa que solicite al usuario un número decimal y luego
imprima la parte entera y decimal por separado.'''

numero =input('introduzca un numero decimal: ')
entero_decimal = numero.split(".")
print(f' numero entero: {entero_decimal[0]} y el numero decimal: {entero_decimal[1]} ')



''' Fin'''