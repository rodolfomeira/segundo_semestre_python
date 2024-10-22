n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
op = input('Digite + para somar ou - para subtrair: ')
if op == '+':
	soma = n1+n2
	print('A soma de', n1, 'com', n2, 'é: ', soma)
elif op == '-':
	sub = n1-n2
	print('A dif entre', n1, 'e', n2, 'é: ', sub)
else:
	print('Operador inexistente')
