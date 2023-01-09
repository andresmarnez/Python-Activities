#Ejercicio 11 Creditos
subjects = {'Matematicas':6,'Fisica':4, 'Quimica':5, 'Castellano':6 , 'Progrmacion de dispositivos moviles':6}
total = 0
for sub in subjects:
    cred = subjects[sub]
    print(sub + ' tiene ' + str(cred) + ' creditos.' )
    total+=cred
print('\nEl curso esta formado por: ' + str(total) + ' creaditos.')
