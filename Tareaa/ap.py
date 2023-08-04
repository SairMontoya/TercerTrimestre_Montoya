from Pais import *
import csv 

listapaises=[]

with open('c:c:\\Andres\\pais.', encoding='utf-8') as archivo:

    lectura=csv.reader(archivo)
    for row in lectura:
        ob=Pais(row[1], row[7], row[8], row[9])
        listapaises.append(ob)
        #print(row )



for apr in listapaises:
    #print(apr)
    print('Pais:',apr.getPais())
    print('pobla:',apr.getpobla())
    print('Altura:',apr.getaltura())
    print('Perpob:',apr.getPerpob())