## Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem ##

distancia = float(input('distancia da viagem: '))
velocidade = float(input('Velocidade media do veiculo: '))

tempo = distancia / velocidade

print(f'O tempo estimado da viagem é {tempo} horas.')