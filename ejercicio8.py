#Ejercicio 8 NOTAS
print('Asignación de notas.\n')
asignaturas = ['Matemáticas', 'Física', 'Química','Historia','Lengua']
notas = []
for asignatura in asignaturas:
    nota_asignatura = input('Introduzca nota de ' + asignatura + ' (0-10): ')
    if  not nota_asignatura.isdigit():
        print('No se ha podido guardar la nota ya que no es un numero.')
    elif not (0 <= int(nota_asignatura) <= 10):
        print('No se ha podido guardar la nota debido a que no está entre 0 y 10.')
    else:
        notas.append([asignatura,nota_asignatura])
print('\nNOTAS:')
for nota in notas:
    print('En ' + nota[0] + ' has sacado un ' + nota[1] + '.')
