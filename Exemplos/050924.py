#Ex08
'''nome= input('Digite o seu nome: ')
sexo= input('Digite o sexo m/f : ')
sexo=sexo.lower()
idade= int(input('Digite a idade :'))
if (sexo=='f' and idade<25):
	print(nome,' - ACEITA')
else:
	print('NÃO ACEITA')'''
	
#Ex09
'''idade=int(input('Digite a Idade: '))
if (idade>21):
	print ('Maior de Idade')
else:
	print ('Menor de Idade')'''
	
'''import random
num= random.randint(0,10)
print (num)		
	
'''

import random
n1= int(input('Digite um número entre 0 a 10: '))
escolha= input('Escolha par ou ímpar (p/i): ')
escolha=escolha.lower()
n2=random.randint (0,10)
print ('Maquina escolheu:',n2)
res=(n1+n2)
print (res)
if (res%2==0 and escolha=='p'):
	print ('Você Ganhou')
elif (res%2!=0 and escolha=='i'): 
	print ('Você ganhou')	
else:
	print ('Você Perdeu!')	

	
	
