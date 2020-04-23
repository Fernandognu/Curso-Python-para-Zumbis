#modifique o programa da empresa thau para uma promoção onde a tarifa é de R$ 0,08 quando voce utiliza mais que 800 minutos#

minutos = int(input("Minutos usados: "))

if minutos < 200:
    tarifa = 0.20
else:
    if minutos <= 400:
        tarifa = 0.18
    else:
        if minutos <= 800:
            tarifa = 0.15
        else:
            tarifa = 0.08
print (f"Valor da Conta é R$ {minutos * tarifa:.2f}")
