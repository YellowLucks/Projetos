from math import sin, cos, tan, radians
angulo = float(input('informe o angulo: '))

seno = sin(radians(angulo))
print('o SENO do angulo {} é {:.2f}'.format(angulo, seno))
coseno = cos(radians(angulo))
print('o COSENO do angulo {} é {:.2f}'.format(angulo, coseno))
tangente = tan(radians(angulo))
print('o TANGENTE do angulo {} é {:.2f}'.format(angulo, tangente))
