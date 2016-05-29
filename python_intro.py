print("Hello, Djangogirls")

def hi(name):
	if name == "Ola":
		print("Hi Ola!")
	elif name == "Sonja":
		print("Sonja")
	else:
		print("Hi anonimous!")

hi('Ola')

def hi(name):
	print("HI " + name + "!")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
		hi(name)
		print("Next girl")

for i in range(1, 6):
	print(i)



