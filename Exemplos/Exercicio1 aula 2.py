import os

print ("Salário")
sbr = float (input ('Digite o Salário bruto: '))
grat = sbr*0.05
imp = sbr/100*7
sliq = sbr-imp+grat
texto = ("Sua gratificação é R$")
os.system('cls')

print ("Salário bruto: R$" ,sbr)
print ('{0:10.20}{1:>10.2f}' .format(texto,grat ))
print ("Sua taxa de imposto é R$" , imp)
print ("Salário Liquido é R$" , sliq)
