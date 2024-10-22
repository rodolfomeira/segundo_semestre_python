import random

numPc = random.randint(0,10)
resposta = input("Digite p = par ou i=impar: ")
resposta = resposta.lower()
numUsu = int(input("Digite seu número: "))
soma = numPc + numUsu

print ("\n\nNumero que o computador sorteou: ", numPc)
print ("Numero que o usuario escolheu: ", numUsu)
print ("A soma dos numeros: ", soma)
print("\n")

if(resposta!='p' and resposta!='i'):
    print('\nErro - Você não escolheu uma opção válida para par ou impar')
elif (resposta=='p' and soma%2 == 0):
    print("\nVc apostou Par - Voce ganhou")
elif(resposta=='p' and soma%2 != 0):
    print("\nVc apostou Par - Voce perdeu")
elif(resposta=='i' and soma%2 != 0):
    print("\nVc apostou Impar - Voce ganhou")
else:
    print("\nVc apostou Impar - Voce perdeu")

