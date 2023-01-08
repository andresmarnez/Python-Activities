# Ejercicio 5 Tramos IRPF
print('<Calculadora de tipos impositivos en la declaración de la renta>\n')
renta = input('Introduzca su renta anual en €: ')
if not renta.isdigit():
    print('Introduzca un digito.')
else :
    if int(renta) < 10000:
        print('Su tipo impositivo es del 5%')
    elif int(renta) < 20000:
        print('Su tipo impositivo es del 15%')
    elif int(renta) < 35000:
        print('Su tipo impositivo es del 20%')
    elif int(renta) < 60000:
        print('Su tipo impositivo es del 30%')
    else:
        print('Su tipo impositivo es del 45%')
