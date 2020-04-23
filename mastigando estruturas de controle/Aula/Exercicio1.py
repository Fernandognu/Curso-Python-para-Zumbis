velocidade = int(input(" Qual a velocidade do carro: "))
if velocidade > 110:
    print("Voce foi multado!")
    multa = (velocidade - 110) * 5
    print(f"O valor da multa é R$ {multa:.2f}")