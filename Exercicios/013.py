salario = float(input('qual seu salaraio? '))
aumento = float(input('Qual foi o aumento? '))

porc = 1+(aumento/100)
nsalario = salario * porc

print('seu novo salario é {:.2f}'.format(nsalario))

