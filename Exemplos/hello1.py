'''
x = float(input('Digite x: '))
y = 3*x+2
print('O valor de y em função de x é: ', y)


distP = float(input('Digite a dist: '))
volC = float(input('Digite o volume: '))
consM = distP/volC
print('Consumo médio é de ', consM,'km/l')
'''
import os

ht = float(input('digite ht: '))
vh = float(input('digite vh: '))
pd = float(input('digite pd: '))
sb = ht*vh
vd = sb*pd/100
sl = sb-vd
'''
print('HT = ', ht)
print('VH = ', vh)
print('PD = ', pd)
print('SB = ', sb)
print('VD = ', vd)
print('SL = ', sl)
'''
os.system('cls')
print('{0:#<30} = {1:>10.2f}'.format( 'Horas Trabalhadas', ht) )
print('{0:#<30} = {1:>10.2f}'.format( 'Valor recebido por hora', vh) )
print('{0:#<30} = {1:>10.2f}'.format( 'Porcentagem de INSS', pd) )
print('{0:<30} = {1:>10.2f}'.format( 'Salário Bruto', sb) )
print('{0:<30} = {1:>10.2f}'.format( 'Valor do desconto', vd) )
print('{0:<30} = {1:>10.2f}'.format( 'Salário Líquido', sl) )

