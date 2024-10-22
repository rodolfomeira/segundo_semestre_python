import random

#numPc = random.randint(0,10)
numPc = 5
resposta = input("Digite p = par ou i=impar: ")
resposta = resposta.lower()
numUsu = int(input("Digite seu número: "))
soma = numPc + numUsu

print ("\n\nNumero que o computador sorteou: ", numPc)
print ("Numero que o usuario escolheu: ", numUsu)
print ("A soma dos numeros: ", soma)
print('\n')

if(resposta!='p' and resposta!='i'):
    print('\nErro - Você não escolheu uma opção válida para par ou impar')
elif(soma%2==0):
    print('Par')
    if(resposta=='p'):
        print('Você ganhou')
    else:
        print('Você perdeu')
else:
    print('Impar')
    if(resposta=='i'):
        print('Você ganhou')
    else:
        print('Você perdeu')
