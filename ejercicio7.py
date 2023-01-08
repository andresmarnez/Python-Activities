# Ejercicio 7 Frase y letra
print('Identificador de letras.\n')
frase = input('Introduzca una frase: ')
letra = input('Letra a buscar: ')
if len(letra) == 1:
    count = 0
    for c in frase:
        if c == letra:
            count+=1
    print('La letra ' + letra + ' aparece un total de ' + str(count) + ' veces.')
else:
    print('Por favor, introduzca una única letra')
