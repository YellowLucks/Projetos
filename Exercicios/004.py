algo = input('Digite algo: ')

print('Isso é do tipo ', type(algo))
# print('"{}" é um alfa numerico? '.format(algo), algo.isalnum())
if (algo.isalnum() == True):
    print('"{}" é alphanumerico'.format(algo))

else:
    print('"{}" nao é alphanumerico'.format(algo))

