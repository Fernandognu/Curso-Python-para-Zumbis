'''João Papo de Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na 
variável excesso e na variável multa o valor da multa queJoão deverá pagar. Caso contrário mostrar tais 
variáveis com o conteúdo ZERO.'''

pesoPescado = float(input("Quantos quilos vôce pescou? "))
excesso = 0
multa = 0
if pesoPescado > 50:
    excesso = pesoPescado - 50
    multa = excesso * 4
    print(f"A quantidade pescada é maior que o limite, Excesso: {excesso:.2f}Kg e a multa é de R$ {multa:.2f}.")
else:
    print(f"A quantidade pescada é menor que o limite, Excesso: {excesso:.2f}Kg e a multa é de R$ {multa:.2f}.")