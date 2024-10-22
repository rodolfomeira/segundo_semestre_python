import random

numPc = random.randint(0,10)
resposta = input("Digite p = par ou i=impar: ").lower()
if (resposta != 'p' and resposta !='i'):
	print("\nErro - Você não escolheu uma opção válida para par ou impar")
else:
	numUsu = int(input("Digite seu número: "))
	soma = numPc + numUsu

	print ("\n\nNumero que o computador sorteou: ", numPc)
	print ("Numero que o usuario escolheu: ", numUsu)
	print ("A soma dos numeros: ", soma)
	print("\n")

	if (resposta=='p'):
		print("\nVoce e par!")
		if(soma%2 == 0):
			print("Voce ganhou")
		else:
			print("Voce perdeu")
	else:
		print("\nVoce e impar!")
		if(soma%2 == 0):
			print("Voce perdeu")
		else:
			print("Voce ganhou")
