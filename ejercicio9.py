#Ejercicio 9 Asignaturas Suspensas
print('Asignación de notas.\n')
asignaturas = ['Matemáticas', 'Física', 'Química','Historia','Lengua']
rem_asignaturas = []
for asignatura in asignaturas:
    nota_asignatura = input('Introduzca nota de ' + asignatura + ' (0-10): ')
    if  not nota_asignatura.isdigit():
        print('No se ha podido guardar la nota ya que no es un numero.')
    elif 0 <= int(nota_asignatura) <= 4:
        continue
    else:
        rem_asignaturas.append(asignatura)

for asignatura in rem_asignaturas:
    asignaturas.remove(asignatura)

print('\nASIGNATURAS A REPETIR:')
for asignatura in asignaturas:
    print('-' + asignatura + '.')
