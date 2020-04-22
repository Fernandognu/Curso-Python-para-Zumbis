## Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento.##
## Exiba o valor do aumento e do novo salário. ##

salario = float(input('Salario: R$'))
aumento = float(input('Porcentagem de aumento: '))/ 100

salarioNovo = (salario * aumento) + salario

print (f'O novo salario é R${salarioNovo:.2f}')