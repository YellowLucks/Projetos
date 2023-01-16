print('Conversor de metros para centimetro e milimetro')

metros = float(input('Metros: '))

centimetro = metros * 100
milimetros = metros * 1000

print('{} é igual a {:.0f} centimetros\n{} é igual a {:.0f} milimetros'.format(metros, centimetro, metros, milimetros))
