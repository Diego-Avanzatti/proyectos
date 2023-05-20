'''1-Crear un diccionario con los nombres de tres frutas y sus respectivos precios y
mostrar el diccionario completo.'''

frutas = {
    'manzana': 12,'pera':15,'melon':20}
print('lista de frutas: ',frutas)

'''2-Crear una lista con los nombres de tres ciudades y agregar una cuarta ciudad al
final de la lista.'''

cuidades = [ 'chaco','corrientes','cordoba']

cuidades.append('santa fe')
print(cuidades)

'''3-Crear una lista con los nombres de tres países y mostrar el segundo país de la
lista.'''
paises = [ 'España','Chile','Francia']
segundo_pais=paises[1]
print('El segundo pais es: ',segundo_pais)


'''4-Crear un diccionario con los nombres de tres personas y sus respectivas
edades. Mostrar la edad de la tercera persona en el diccionario.'''

personas = {'juan':23,'pedro':22,'pepe':34}
edad = personas.get('pepe')
print('La edad de la tercera persona es: ',edad)



'''5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número más
grande en el conjunto.'''

conjunto = {3,2,6,5,9,8,1,4,7,10}
num_mas_grande = max(conjunto)
print('El numero mas grande es: ',num_mas_grande)


'''6-Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número
de elementos en el conjunto.'''

conjunto = {3,2,6,5,9,8,1,4,7,10}
num_conjunto = len(conjunto)
print('El numero de elementos en el conjunto es: ',num_conjunto)


'''7-Crear un diccionario con los nombres de tres ciudades y sus respectivas
poblaciones. Agregar una cuarta ciudad al diccionario con su respectiva
población. Mostrar el diccionario resultante.'''

cuidades = {
    'chaco': 40.000
    ,'corrientes':50.000
    ,'cordoba': 100.000
    }

cuidades['santa fe']=120.000

print('las cuidades y su poblacion: ',cuidades)




'''
8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso.'''

num = [1,2,3,4,5,6,7,8,9,10]
num.reverse()
num_inverso= num
print('la lista alreves es: ',num_inverso)

'''9-Crear una lista con los nombres de tres países y ordenar la lista en orden
alfabético. Mostrar la lista resultante.'''

paises = [ 'España','Chile','Francia']
paises.sort()
print("lista de paises en orden alfabetico: ", paises)

'''10-Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la
lista. Mostrar la lista resultante.'''

frutas = ['manzana','pera','melon']
frutas.pop(1)
print('lista de frutas: ',frutas)

'''11-Crear una lista con los nombres de tres animales y agregar una cuarta animal
al principio de la lista. Mostrar la lista resultante.'''

animales = ['perro','gato','leon']
animales.insert(0,'mono')
print('lista de animales: ',animales)


''' 12-Crear una lista con los nombres de tres países y reemplazar el segundo país de
la lista por otro país. Mostrar la lista resultante.'''

paises = [ 'España','Chile','Francia']
paises[1] =  'Argentina'
print('lista de paises: ',paises)




'''13-Crear una lista con los nombres de tres colores y agregar dos colores más al
final de la lista. Mostrar la lista resultante.'''

colores = ['rojo','azul','verde']
colores.extend(['negro','blanco'])
print('lista de colores: ', colores)

'''14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los
elementos de la tupla.'''

tupla = (1,2,3,4,5)
suma = sum(tupla)
print('la suma de la tupla es: ',suma)


'''FIN'''