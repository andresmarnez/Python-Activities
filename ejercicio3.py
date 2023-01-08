# Ejercicio 3
print('¿Es par o impar?\n')
x = input('Introduzca un número: ')

if  not x.isdigit():
    print('Error: Debes introducir un número.')
elif int(x)%2 == 1:
    print(x + ' es impar.')
else:
    print(x + ' es par.')
