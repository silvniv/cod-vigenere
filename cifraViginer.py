def letra_para_indice(letra):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    return alfabeto.index(letra.lower())

def indice_para_letra(indice, maiuscula=False):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    letra = alfabeto[indice % 26]
    return letra.upper() if maiuscula else letra

def repetir_chave(chave, tamanho):
    chave = chave.lower()
    return (chave * (tamanho // len(chave) + 1))[:tamanho]

def cifra_vigenere(texto, chave, modo='cifrar'):
    resultado = ''
    chave_repetida = repetir_chave(chave, len(texto))

    for i, letra in enumerate(texto):
        if letra.isalpha():
            indice_texto = letra_para_indice(letra)
            indice_chave = letra_para_indice(chave_repetida[i])
            deslocamento = indice_chave if modo == 'cifrar' else -indice_chave
            novo_indice = (indice_texto + deslocamento) % 26
            nova_letra = indice_para_letra(novo_indice, letra.isupper())
            resultado += nova_letra
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    while True:
        
        chave = input("Digite a chave de cifra (palavra):\t")
        texto = input("Digite o texto:\t")
        modo = input("Digite o modo ('cifrar' ou 'decifrar'):\t").strip().lower()

        if modo not in ['cifrar', 'decifrar']:
            print("Modo inválido. Use 'cifrar' ou 'decifrar'.")
        else:
            resultado = cifra_vigenere(texto, chave, modo=modo)
            print(f"Resultado ({modo}):\t{resultado}")

        if input("Deseja continuar? (s/n):\t").strip().lower() != 's':
            break
