# Ejercicio 13
# Lista de la compra
# @author Andres Sanchez Martinez
lista = {}
print('<LISTA DE LA COMPRA>')

while True:
    articulo = input('Nombre del articulo\t\t\t\tVACIO PARA SALIR\n->')
    if articulo == '':
        break
    precio = input('Precio unitario\n->')
    if not precio.replace(".","",1).isdigit():
        print('No se ha introducido una cantidad numerica.')
    else:
        lista[articulo] = precio
    print()

total = 0
for art in lista:
    print(art + '\t\t\t\t\t\t' + lista[art] + '€')
    total += float(lista[art])
print('\nTotal\t\t\t\t\t\t'+ str(round(total)) + '€')
