nome = input('Digite seu nome: ')
sexo = input('Digite m (masculino) e f (feminino): ')
idade = int (input('Digite sua idade: '))
while sexo!='f' and sexo!='m':
	print('Sexo inválido')
	sexo = input('Digite m (masculino) e f (feminino): ')

if (sexo=='f' or sexo=='F') and idade<25:
	print('Nome: {0:} - ACEITA'. format(nome))
else:
	print('Não aceita')
