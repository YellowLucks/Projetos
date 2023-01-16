km = float(input('Quantos Km voce rodou com seu carro alugado? '))
dias = int(input('Quantos dias o carro ficou alugado? '))

preco = (60 * dias) + (0.15 * km)

print('Você precisa pagar {:.2f}R$.'.format(preco))

