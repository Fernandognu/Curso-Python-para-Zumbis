'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calculee mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto,
quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - 
Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
    a. + Salário Bruto : R$
    b. - IR (11%) : R$
    c - INSS (8%) : R$
    d. - Sindicato ( 5%) : R$
    e. = Salário Liquido : R$'''

ir = 0.11
inss = 0.08
sind = 0.05

valorHoras = float(input("Quanto recebe por hora? "))
horas = float(input("Quantas horas por mês? "))

salarioBruto = (valorHoras * horas)
ir = salarioBruto * ir
inss = salarioBruto * inss
sind = salarioBruto * sind

print(f"A. Salário Bruto: R$ {salarioBruto:.2f}")
print(f"B. IR (11%): R$ {ir:.2f}")
print(f"C. INSS (8%): R$ {inss:.2f}")
print(f"D. Sindicato (5%): R${sind:.2f}")
print(f"E. Salario Liquido: R$ {salarioBruto - ir - inss - sind:.2f}")