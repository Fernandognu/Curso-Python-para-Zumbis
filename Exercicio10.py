## Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
# total de dias. ##

cigarros = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Quantos anos Você fumou? '))

minutosPerdido = ((cigarros * 10) * 365) * anos
diasPerdidos = (minutosPerdido / 60) / 24


print (f'Você perdeu {minutosPerdido} minutos de vida, ou se preferir {diasPerdidos:.0f} dias perdidos!')