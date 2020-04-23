#Faça um Programa que leia três números e mostre o maior e o menor deles.
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))
x = 0
y = 0
if a > b and a > c:
    x = a
elif b > c and b > a:
    x = b
else:
    x = c
if a < b and a < c:
    y = a
elif b < c and b < a:
    y = b
else:
    y = c
print(f"O numero maior é {x}, e o menor é {y}")
