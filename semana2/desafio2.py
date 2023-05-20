
texto = input("Ingresa un texto: ")

letra1 = input("Ingresa la primera letra: ")
letra2 = input("Ingresa la segunda letra: ")
letra3 = input("Ingresa la tercera letra: ")


texto = texto.lower()

''' Cantidad de veces que aparece cada una de letras que eligió. '''
contador1 = texto.count(letra1)
contador2 = texto.count(letra2)
contador3 = texto.count(letra3)


print("La letra", letra1, "aparece", contador1, "veces.")
print("La letra", letra2, "aparece", contador2, "veces.")
print("La letra", letra3, "aparece", contador3, "veces.")


'''Cuantas palabras hay en total en todo el texto.'''

palabras = texto.split(' ')

cantidad_palabras = len(palabras)
print('en el texto hay: ', cantidad_palabras)


'''Cual es la primera letra y cuál es la última. (Indexación)'''

primera_letra = texto[0]
ultima_letra = texto[-1]

print("La primera letra del texto es:", primera_letra)
print("La última letra del texto es:", ultima_letra)





'''Mostrar el texto en orden inverso.'''

texto_inverso = texto[::-1]
print("Texto en orden inverso:", texto_inverso)


'''Decir si la palabra "python" aparece en el texto.'''


aparece_python = "python" in texto

resultado_python = {
    True: "La palabra 'python' aparece en el texto.", 
    False: "La palabra 'python' no aparece en el texto."
    }

print(resultado_python[aparece_python])


'''FIN'''



