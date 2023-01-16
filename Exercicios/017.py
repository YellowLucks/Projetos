from math import hypot
oposto = float(input('digite o cateto oposto: '))
adjacente = float(input('digite o cateto adjacente: '))

hipotenusa = hypot(oposto, adjacente)

print('A hipotenusa é {:.2f}'.format(hipotenusa))
