#Funciones para Agregar, editar y eliminar inmuebles a la lista.

def agregar_inmueble(lista, inmueble):
    if validar_inmueble(inmueble):
        lista.append(inmueble)
        print("Inmueble agregado correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

def editar_inmueble(lista, indice, inmueble):
    if validar_inmueble(inmueble):
        if indice >= 0 and indice < len(lista):
            lista[indice] = inmueble
            print("Inmueble editado correctamente.")
        else:
            print("El índice del inmueble a editar es inválido.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

def eliminar_inmueble(lista, indice):
    if indice >= 0 and indice < len(lista):
        del lista[indice]
        print("Inmueble eliminado correctamente.")
    else:
        print("El índice del inmueble a eliminar es inválido.")

#------------------------------------------------------------

#Funcion para cambiar el estado


def cambiar_estado(lista, indice, nuevo_estado):
    if indice >= 0 and indice < len(lista):
        lista[indice]['estado'] = nuevo_estado
        print("Estado del inmueble cambiado correctamente.")
    else:
        print("El índice del inmueble es inválido.")
#--------------------------------------------------------------
#Funcion para buscar el inmueble por presupuesto dado
def buscar_inmuebles(lista, presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista:
        if inmueble['estado'] in ['Disponible', 'Reservado'] and calcular_precio(inmueble) <= presupuesto:
            inmueble_con_precio = dict(inmueble)
            inmueble_con_precio['precio'] = calcular_precio(inmueble)
            inmuebles_encontrados.append(inmueble_con_precio)
    return inmuebles_encontrados

#-------------------------------------------------
#Funcion para validar inmueble

def validar_inmueble(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] < 2:
        return False
    return True
#--------------------------------------------------


#Funcion para calcular con las reglas de precio
def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble['año']
    if inmueble['zona'] == 'A':
        precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1 - antiguedad / 100)
    elif inmueble['zona'] == 'B':
        precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1 - antiguedad / 100) * 1.5
    else:
        precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1 - antiguedad / 100) * 2
    return precio



#Utilizando las funciones


lista_inmuebles = [
    {'año': 2007, 'metros': 150, 'habitaciones': 5, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2002, 'metros': 90, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Vendido'},
    ]


#Ejemplo de agregacion de inmueble
nuevo_inmueble = {'año': 2022, 'metros': 120, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Disponible'}
agregar_inmueble(lista_inmuebles, nuevo_inmueble)
#--------------------------------------------

#Ejemplo de agregacion de inmueble
editar_inmueble(lista_inmuebles, 2, {'año': 2005, 'metros': 160, 'habitaciones': 5, 'garaje': False, 'zona': 'A', 'estado': 'Reservado'})
#--------------------------------------------

#Ejemplo de eliminar un inmueble
eliminar_inmueble(lista_inmuebles, 3)
#--------------------------------------------

#Ejemplo de cambiar el estado de un inmueble
cambiar_estado(lista_inmuebles, 0, 'Reservado')
#--------------------------------------------



#Ejemplo de la búsqueda de inmuebles en función de un presupuesto dado. 
presupuesto = 200000
inmuebles_encontrados = buscar_inmuebles(lista_inmuebles, presupuesto)
print("Inmuebles encontrados dentro del presupuesto:")
for inmueble in inmuebles_encontrados:
    print(inmueble)
#--------------------------------------------

