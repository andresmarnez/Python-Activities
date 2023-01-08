# Ejercicio 4 Grupos por nombre
print('<Programa de asignación de grupos>\n')
sexo = input('Introduzca el sexo del estudiante (F/M): ').casefold()
nombre = input('Introduzca el nombre del alumno: ').casefold()
if not(sexo == 'f' or sexo == 'm'):
    print('El sexo introducido es incorrecto')
elif (sexo == 'f' and nombre < 'm') or (sexo == 'm' and nombre > 'n'):
    print('Le ha tocado el grupo A')
else :
    print('Le ha tocado el grupo B')
        
