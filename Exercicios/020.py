from random import shuffle

a1 = str(input('Escolha o primeiro aluno: '))
a2 = str(input('Escolha o segundo aluno: '))
a3 = str(input('Escolha o terceiro aluno: '))
a4 = str(input('Escolha o quarto aluno: '))

alunos = [a1, a2, a3, a4]

shuffle(alunos)

print('A ordem de apresentação sera {}'.format(alunos))
