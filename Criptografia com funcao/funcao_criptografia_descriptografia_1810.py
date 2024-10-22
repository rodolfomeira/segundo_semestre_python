# Função para criptografar o texto
def criptografar(texto, alfabeto, chave):
    texto_convertido = ""
    tamanho = len(alfabeto)
    
    # Verifica cada letra no texto fornecido
    for letra in texto:
        if letra in alfabeto:
            # Obtém o índice da letra no alfabeto
            ind_o = alfabeto.index(letra)
            # Calcula o novo índice após aplicar a chave
            ind_novo = ind_o + chave
            # Ajusta o índice se exceder o tamanho do alfabeto (rotação)
            if ind_novo >= tamanho:
                ind_novo = ind_novo - tamanho
            # Adiciona a letra correspondente ao novo índice
            texto_convertido += alfabeto[ind_novo]
        else:
            # Mantém o caractere original se não estiver no alfabeto
            texto_convertido += letra
    
    return texto_convertido

# Função para descriptografar o texto
def descriptografar(texto, alfabeto, chave):
    texto_convertido = ""
    tamanho = len(alfabeto)
    
    # Verifica cada letra no texto fornecido
    for letra in texto:
        if letra in alfabeto:
            # Obtém o índice da letra no alfabeto
            ind_o = alfabeto.index(letra)
            # Calcula o novo índice subtraindo a chave
            ind_novo = ind_o - chave
            # Ajusta o índice se for negativo (rotação inversa)
            if ind_novo < 0:
                ind_novo = tamanho + ind_novo
            # Adiciona a letra correspondente ao novo índice
            texto_convertido += alfabeto[ind_novo]
        else:
            # Mantém o caractere original se não estiver no alfabeto
            texto_convertido += letra
    
    return texto_convertido

# Solicita um texto ao usuário e converte todas as letras para minúsculas
texto = input("Digite um texto: ").lower()

# Define o alfabeto utilizado para a criptografia
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# Calcula o tamanho do alfabeto (quantidade de letras)
tamanho = len(alfabeto)

# Solicita ao usuário uma chave numérica para a criptografia/descriptografia
chave = int(input("Digite uma chave entre 1 a {}: ".format(tamanho-1)))

# Verifica se a chave está dentro dos limites válidos (entre 1 e tamanho)
while (chave < 1) or (chave >= tamanho):
    print("Senha incorreta")  # Informa ao usuário que a chave é inválida
    chave = int(input("Digite uma chave entre 1 a {}: ".format(tamanho-1)))

# Solicita ao usuário a escolha de criptografar (1) ou descriptografar (2)
cd = int(input("Digite 1 para criptografar e 2 para descriptografar: "))

# Realiza a operação conforme a escolha do usuário
if cd == 1:
    texto_convertido = criptografar(texto, alfabeto, chave)
elif cd == 2:
    texto_convertido = descriptografar(texto, alfabeto, chave)
else:
    texto_convertido = "Opção inválida."

# Exibe o texto criptografado ou descriptografado
print("Texto convertido:", texto_convertido)
