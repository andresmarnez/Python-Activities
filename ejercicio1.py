## Ejercicio 1
contrasenya = 'contraseña'
intent = input('<User Log In>\nContraseña: ')
if contrasenya.casefold() == intent.casefold():
    print('Contraseña correcta')
else:
    print('\nContraseña incorrecta')


