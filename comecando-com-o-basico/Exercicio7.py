## Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32 ##

celsius = float(input('Temperatura em Celsius: '))
fahrenheit = 9 * celsius / 5 + 32

print (f'{celsius:.1f}° Celsius é igual a {fahrenheit:.1f}° Fahrenheit.')