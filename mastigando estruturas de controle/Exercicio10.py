# Calcule o fatorial de dez

n = 1
produto = 1
base = 2
while n <= 9:
    produto = produto * base
    base = base + 1
    n = n + 1
print ("Fatorial de 10: %d" %produto)