# Calculo da média de dez numeros inteiros

n = 1
media = 0
soma = 0
while n <= 10:
    x = int(input("Digite o %d numero: " %n))
    soma = soma + x
    media = soma / n
    n = n + 1
print ("Média: %5.2f" %media)