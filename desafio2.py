'''
Desafío 2:
Escribe un programa que solicite al usuario su información personal, incluyendo
su nombre completo, edad, estatura, peso, dirección y número de teléfono.
A continuación, el programa deberá imprimir un mensaje con los datos
ingresados por el usuario en el siguiente formato:
La información ingresada es la siguiente:
Nombre completo: [nombre completo]
Edad: [edad]
Estatura: [estatura] cm
Peso: [peso] kg
Dirección: [dirección]
Número de teléfono: [número de teléfono]
'''

Nombre_completo= input('Nombre Completo: ')
Edad= int(input('Edad: '))
Estatura= int(input('Estatura en cm: ' ))
Peso= float(input('Peso en kg: '))
Dirección= input('Direccion: ')
Número_de_teléfono= int(input('Número de teléfono: '))


print(f'Nombre completo: {Nombre_completo}.')
print(f'Edad: {Edad}.')
print(f'Estatura: {Estatura} cm.')
print(f'Peso: {Peso} Kg.')
print(f'Dirección: {Dirección}.')
print(f'Número de teléfono: {Número_de_teléfono}.')
