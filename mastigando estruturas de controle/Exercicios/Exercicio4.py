#Faça um Programa que leia três números e mostre o maior deles.
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))
x = 0
if a > b and a > c:
    x = a
elif b > c and b > a:
    x = b
else:
    x = c
print(f"O numero maior é {x}")