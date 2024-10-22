# Solicita o texto de entrada
textodeentrada = input("Digite um texto: ")

# Verifica se há necessidade de tornar tudo maiúsculo ou minúsculo
textodeentrada = textodeentrada.lower()  # Aqui estamos tornando tudo minúsculo, pode ser ajustado conforme necessário

# Cria o alfabeto (aqui, apenas letras minúsculas)
alfabeto = "abcdefghijklmnopqrstuvwxyz"
tamanho_alfabeto = len(alfabeto)

# Solicita uma chave válida dentro do intervalo
chave = int(input(f"Digite uma chave entre 1 e {tamanho_alfabeto - 1}: "))

# Enquanto a chave estiver incorreta, solicita novamente
while chave < 1 or chave >= tamanho_alfabeto:
    chave = int(input(f"Chave inválida. Digite uma chave entre 1 e {tamanho_alfabeto - 1}: "))

# Solicita o tipo de conversão (1-crip ou 2-decrip)
tipo_conversao = int(input("Digite 1 para criptografar ou 2 para descriptografar: "))

# Inicializa a string que armazenará o texto convertido
textoconvertido = ""

# Laço para percorrer o texto digitado
for caractere in textodeentrada:

    # Verifica se o caractere está no alfabeto
    if caractere in alfabeto:

        # Encontra o índice (posição) da letra no alfabeto
        indice_original = alfabeto.index(caractere)

        # Se 1 é para criptografar
        if tipo_conversao == 1:
            # Soma-se o valor da chave ao índice
            indice_novo = indice_original + chave

        # Se 2 é para decriptografar
        elif tipo_conversao == 2:
            # Subtrai-se o valor da chave ao índice
            indice_novo = indice_original - chave

        # Se o novo índice for maior ou igual ao tamanho do alfabeto, rotaciona
        if indice_novo >= tamanho_alfabeto:
            indice_novo = indice_novo - tamanho_alfabeto

        # Se o novo índice for menor que 0, rotaciona
        if indice_novo < 0:
            indice_novo = tamanho_alfabeto + indice_novo

        # Adiciona o caractere da posição do índice ajustado ao novo texto
        textoconvertido += alfabeto[indice_novo]

    # Se o caractere não está no alfabeto, copia o mesmo caractere para o novo texto
    else:
        textoconvertido += caractere

# Imprime o novo texto (criptografado ou decriptografado)
print("Texto convertido:", textoconvertido)

