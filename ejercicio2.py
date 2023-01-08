# Ejercicio 2
print('Calculadora de divisiones x/y\n')
x = input('Introduzca x: ')
y = input('Introduzca y: ')

if  y == 0:
    print('Error: división entre 0.')
elif not x.isdigit() or not y.isdigit():
    print('Error: ambos digitos deben ser números.')
else:
    print('Resultado: ' + str(int(x)/int(y)))
