nome = str(input('qual seu nome? ')).strip()

print('Nome maiusculo: {}'.format(nome.upper()))
print('Nome minusculo: {}'.format(nome.lower()))
print('Seu nome todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome tem {} letras'.format(len(separa[0])))
