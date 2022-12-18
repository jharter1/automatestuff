evilChildren = []
while True:
	print('Enter the name of the evil Child ' + str(len(evilChildren) + 1) + 
		' (Or enter nothing to stop.):')
	name = input()
	if name == '':
		break
	evilChildren = evilChildren + [name]
print('The names of my evil children are:')
for name in evilChildren:
	print(' ' + name)