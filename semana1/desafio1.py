'''
Desafío 1:
Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
sus ventas totales y el departamento comercial te solicita que ayudes a los
vendedores a calcular sus comisiones creando un programa que les pregunte su
nombre y cuánto han vendido en éste mes.
Tu programa le va a responder con una frase que incluya su nombre y el monto
que le corresponde por las comisiones
'''
vendedor= input('introducir nombre: ')
venta =int(input('introducir venta: '))
ventas = [10,30,40]
ventas.append(venta)
print(f'Al vendedor: {vendedor} le corresponde una comision de: {round(sum(ventas)*0.06)} pesos por el total de sus ventas.')





