# Ejercicio 15
# Diccionario de lo clientes
# @author Andres Sanchez Martinez

db_clients = {}

print('<GENERADOR DE DICCIONARIO DE CLIENTES A PARTIR DE LINEAS>\n')
cli_str = 'nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7'

print('Cadena a traducir: ' + cli_str)
raw_lines = cli_str.split('\n')

cli_guide = raw_lines[0].split(';')
del cli_guide[0]
del raw_lines[0]

print('\n---\n')
for cli in raw_lines:

    cli_data_array = cli.split(';')
    dni = cli_data_array.pop(0)

    actual_cli = dict(zip(cli_guide,cli_data_array))
    db_clients[dni] = actual_cli


print(db_clients)    
        
