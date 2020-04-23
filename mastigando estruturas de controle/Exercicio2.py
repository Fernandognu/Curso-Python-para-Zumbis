minutos = int(input("Quantos minutos: "))

if minutos < 200:
    valor = minutos * 0.20
    print (f"Valor da conta R$ {valor}")
if 200 <= minutos < 400:
    valor = minutos * 0.18
    print (f"Valor da conta R$ {valor}")
if minutos >= 400:
    valor = minutos * 0.15
    print (f"Valor da conta R$ {valor}")
