
valor = float(input('qual valor do produto? '))
desc = float(input('Qual foi o desconto? '))

porc = 1-(desc/100)
desconto = valor * porc

print ('O produto custa R${} e com o desconto de {}% ficou R${:.2f}' .format (valor,desc,desconto))
