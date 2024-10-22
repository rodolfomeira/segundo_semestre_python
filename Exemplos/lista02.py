import os

'''
sb = float(input('Digite sb: '))
grat = sb*5/100
imp = sb*7/100
sl = sb-imp+grat

os.system('cls')
print('sb = ', sb)
print('gr = ', grat)
print('im = ', imp)
print('sl = ', sl)


nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
nt3 = float(input('Digite a terceira nota: '))
media = (nt1+nt2+nt3)/3
print('A media é: ', media)
'''
gt = float(input('Digite o total gasto: '))
pg = gt*10/100
vp = gt+pg
os.system("cls")
print('{0:<30} -> {1:>10.2f}'.format('Total Gasto: ', gt))
print('{0:<30} -> {1:>10.2f}'.format('Garçon: ', pg))
print('{0:<30} -> {1:>10.2f}'.format('Valor Pago: ', vp))

