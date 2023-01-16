largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))

area = altura * largura
litro = 2
gasto = area/litro

print('A area da parede é {:.0f} metros e a quantidade de tinta gasta vai ser de {:.0f} litros'.format(area, gasto))
