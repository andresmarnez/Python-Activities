# Ejercicio 10
print('<Precio de verduras y frutas>\n')
frutas = {'platano':1.34,'manzana':0.8,'melon':1.9,'pera':0.85,'naranja':0.7,'kiwi':3.4}

fruta = input('¿Que fruta quiere pesar?\n-> ')
if (fruta in frutas.keys()):
    peso = input('Introduzca el peso: ')
    if peso.isdigit():
        print('PRECIO: ' + str(int(peso)*frutas[fruta]) + '€')
    else:
        print('Debe ingresar solo numeros.')
            

else:
    print('La fruta \''+ fruta + '\' no esta registrada.')
