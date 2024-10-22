idade = int(input('Digite sua idade: '))
# idades válidas 12-17 - idades não válidas 0,1,2,3...11 <12 e >17 18,19,20...
# or somente falso com dois falsos
# com o not o if só será executado quando dois falsos (vira verdadeiro)
if ( not( (idade < 12 or idade > 17) )  ):
	print('Adolescente')
