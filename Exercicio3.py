dia = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

segundosTotal = ((((dia * 24)+ horas)* 60)+ minutos)* 60 + segundos

print (f'{dia} dias, {horas} horas, {minutos} minutos e {segundos} segundos tem no total {segundosTotal} segundos.')