## Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar. ##

preço = float(input('Preço do produto: '))
desconto = float(input('Percentual de desconto: '))/ 100

preçoComDesconto = preço -(preço * desconto)

print (f'O preço com desconto é R$ {preçoComDesconto:.2f}')