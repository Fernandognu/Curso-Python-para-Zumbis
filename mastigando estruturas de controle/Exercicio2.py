minutos = int(input("Quantos minutos: "))

'''if minutos < 200:
    valor = minutos * 0.20
    print (f"Valor da conta R$ {valor:.2f}")
if 200 <= minutos < 400:
    valor = minutos * 0.18
    print (f"Valor da conta R$ {valor:.2f}")
if minutos >= 400:
    valor = minutos * 0.15
    print (f"Valor da conta R$ {valor:.2f}")'''


if minutos < 200:
    preço = 0.20
else:
    if minutos <= 400:
        preço = 0.18
    else:
        preço = 0.15
print (f"Valor da conta R$ {minutos * preço:.2f}")
