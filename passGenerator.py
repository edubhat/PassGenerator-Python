import random
import string

def gerar_senha(comprimento=12, maiusculas=True, minusculas=True, numeros=True, simbolos=True):
    caracteres = ''
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if len(caracteres) == 0:
        raise ValueError("Pelo menos um conjunto de caracteres deve ser selecionado")

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

comprimento_senha = int(input("Digite o comprimento da senha desejada: "))
usar_maiusculas = input("Usar letras maiúsculas? (Sim/Não): ").strip().lower() == 'sim'
usar_minusculas = input("Usar letras minúsculas? (Sim/Não): ").strip().lower() == 'sim'
usar_numeros = input("Usar números? (Sim/Não): ").strip().lower() == 'sim'
usar_simbolos = input("Usar símbolos? (Sim/Não): ").strip().lower() == 'sim'

try:
    senha_gerada = gerar_senha(
        comprimento_senha, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos
    )
    print("Senha gerada:", senha_gerada)
except ValueError as e:
    print(e)
