#Ejercicio 12
personas = {}
print('La lista de datos actualmente esta vacia.')
while input('¿Introducir nuevo dato? (S/N)\n->').casefold() == 's':
    nombre = input('Nombre del dato: ')
    valor = input(nombre + ': ')
    personas[nombre] = valor
    print(personas)
    print()
