# Ejercicio 14
# Base de datos de clientes
# @author Andres Sanchez Martinez

db_clientes = {}

print('<BASE DE DATOS DE CLIENTES DE OIL&GO>')
while True:
    opt = input('Indique una opcion:\n\t1.Añadir cliente.\n\t2.Eliminar cliente.\n\t3.Mostrar cliente.\n\t4.Listar todos los clientes\n\t5.Listar clientes preferentes.\n\t6.Salir.\n->')
    if opt == '1':
        
        
        print('\n1.AÑDIR CLIENTE')
        
        dni = input('DNI:')
        name = input('NOMBRE:')
        tlf = input('TELEFONO:')
        email = input('CORREO:')
        prf = input('¿ES PREFERENTE? (S/N):').casefold()
        
        if  not(prf == 's' or prf == 'n'):
            print('No corresponde a una opcion, se le ha asignado NO preferente.')
            prf = False
        elif prf == 's':
            prf = True
        else:
            prf = False

        actual_cli = {'NOMBRE':name,'TELEFONO':tlf,'CORREO':email,'PREFERENTE':prf}
        
        db_clientes[dni] =actual_cli       
        
    elif opt == '2':

        print('\n2.ELIMINAR CLIENTE')
        dni = input('DNI:')
        
        if dni in db_clientes.keys():
            del db_clientes[dni]
        else:
            print('NO EXISTE EL CLIENTE.')
        
    elif opt == '3':

        print('\n3.MOSTRAR CLIENTE')
        dni = input('DNI:')
        
        if dni in db_clientes.keys():
            print(cli + ': ' + db_clientes[dni]['NOMBRE'])
        else:
            print('NO EXISTE EL CLIENTE.')
        
    elif opt == '4':
        for cli in db_clientes:
            print(cli + ': ' + db_clientes[cli]['NOMBRE'])
    elif opt == '5':
        for cli in db_clientes:
            if  db_clientes[cli]['PREFERENTE'] == 1:
                print(cli + ': ' + db_clientes[cli]['NOMBRE'])
    elif opt == '6':
        exit()
    else:
        print('Opcion no valida.')
    print()
    
