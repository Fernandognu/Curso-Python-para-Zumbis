'''Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.'''

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
categoria = ''

if a != b != c:
    categoria = 'escaleno'
elif a == b == c:
    categoria = 'equilátero'
else:
    categoria = 'isósceles'

if (b - c) < a < b + c:
    print (f"É um Triangulo {categoria}.")
elif (a - c) < b < a + c:
    print (f"É um Triangulo {categoria}.")
elif (a - b) < c < a + b:
    print (f"É um Triangulo {categoria}.")
else:
    print ("Não é triangulo!")