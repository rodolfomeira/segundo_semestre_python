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
    chave = int(input("Digite uma chave entre 1 a {}: ".format(tamanho-1)))  # Solicita uma nova chave

# Solicita ao usuário a escolha de criptografar (1) ou descriptografar (2)
cd = int(input("Digite 1 para criptografar e 2 para descriptografar: "))

# Inicializa uma variável para armazenar o texto criptografado/descriptografado
texto_convertido = ""

# Verifique sobre cada letra no texto fornecido
for letra in texto:
    # Verifica se a letra está presente no alfabeto
    if letra in alfabeto:
        # Obtém o índice da letra no alfabeto
        ind_o = alfabeto.index(letra)
        
        # Se a escolha for criptografar (1)
        if cd == 1:
            # Calcula o novo índice após aplicar a chave
            ind_novo = ind_o + chave
            # Ajusta o índice se ele exceder o tamanho do alfabeto (rotação)
            if ind_novo >= tamanho:
                ind_novo = ind_novo - tamanho
        
        # Se a escolha for descriptografar (2)
        elif cd == 2:
            # Calcula o novo índice subtraindo a chave
            ind_novo = ind_o - chave
            # Ajusta o índice se ele for negativo (rotação inversa)
            if ind_novo < 0:
                ind_novo = tamanho + ind_novo
        
        # Adiciona a letra correspondente ao novo índice no texto convertido
        texto_convertido += alfabeto[ind_novo]
    
    # Se a letra não estiver no alfabeto (por exemplo, um caractere especial ou espaço)
    else:
        # Mantém o caractere original no texto convertido
        texto_convertido += letra

# Exibe o texto criptografado ou descriptografado
print(texto_convertido)
