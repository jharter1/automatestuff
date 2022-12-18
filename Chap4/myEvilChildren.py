evilChildren = ['Zorp', 'Krum', 'Derf', 'Phlegma']
print('Enter the name of one of my evil Children:')
name = input()
if name not in evilChildren:
	print('That is not one of my evil Children: I have no evil child named ' + name)
else:
	print(name + ' is one of my evil Children')