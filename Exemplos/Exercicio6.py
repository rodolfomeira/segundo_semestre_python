n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
op=input('Digite + para somar , ou - para subtrair')

if op == '+':
	soma= n1+n2
	print('A soma de', n1 ,'com', n2 'é:',soma)
elif op == '-':
	sub= n1-n2
	print('A subtração de',n1,'com',n2 'é:',sub)
else:
	print('Operador Inexistente')
