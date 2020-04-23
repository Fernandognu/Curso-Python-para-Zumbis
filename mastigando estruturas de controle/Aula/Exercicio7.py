# reescreva o programa anterior para escrever os 10 primeiros multiplos de 3
x = 0
multiplo = 0
while x <= 10:
    if multiplo % 3 == 0:
        print (multiplo)
        multiplo = multiplo + 1
        x = x + 1
    else:
        multiplo = multiplo + 1