peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
sexo = input('Digitar sexo m ou f : ').lower()

#m 1.7 40 - 60 - 80 - 85 - 95
#f 1.6  40 - 60 - 69 - 75 -  95

if sexo == 'f':
	abaixo = 19.1
	ideal = 25.8
	medio = 27.3
	acima = 32.3
elif sexo == 'm':
	abaixo = 20.7
	ideal = 26.4
	medio = 27.8
	acima = 31.1
else:
	peso = -1
	altura = -1
imc = peso / (altura * altura)
print('IMC = {0:.2f}'.format(imc))
if imc == -1:
	print('Sexo inválido')
elif imc<abaixo:
	print('Abaixo do peso ideal')
elif imc<ideal:
	print('No peso ideal')
elif imc<medio:
	print('Marginalmente acima do peso')
elif imc<acima:
	print('Acima do peso ideal')
else:
	print('Obeso')
