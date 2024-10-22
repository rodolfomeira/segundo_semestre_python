import os
print ('Cupom Fiscal Restaurante ComaBem')

n1 = float (input ('Digite o valor gasto :'))
pg = n1*10/100
vlr= n1*10/100+n1
os.system ('cls')
print('{0:<30}->{1:>10.2f}'.format('O valor gasto foi :',n1))
print('{0:<30}->{1:>10.2f}'.format('A taxa do garçom foi :',pg))
print('{0:<30}->{1:>10.2f}'.format('O valor total é :',vlr))


