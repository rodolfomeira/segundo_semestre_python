import os


print ("Cálculo de Salário")
h_trab = float (input ('Digite a quantidade de horas trabalhadas: '))
val_hora = float (input ('Digite o valor pago por hora trabalhada: '))
desc_inss = float (input('Digite o percentual de desconto do INSS: '))
res_b = h_trab*val_hora
res_desc = res_b*(desc_inss/100)
res_liq = res_b-res_desc

os.system('cls')

print ("Salário Bruto é R$",res_b)
print ("Valor descontado é R$" , res_desc)
print ("Salário Liquido é R$" , res_liq)
