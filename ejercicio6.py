# Ejercicio 6 Contraseña
pswd = 'contraseña'
print('<CONTROL DE CONTRASEÑAS>')
while (input('Introduzca la contraseña: ').casefold() != pswd):
    print('Contraseña incorrecta.\n')
print('¡¡¡CONTRASEÑA CORRECTA!!!.\n')
