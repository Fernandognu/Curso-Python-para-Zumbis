# Calcule o fatorial de um numero inteiro n

fat = int(input("Digite um numero: "))
n = 1
produto = 1
while n <= fat:
    produto = produto * n
    n = n + 1
print (f"Fatorial de {fat}: %d" %produto)