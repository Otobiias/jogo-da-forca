import sys
import os
import random

def verifica_letra():
    global erro
    if letra_digitada in lista_palavra_escolhida or letra_digitada == palavra_escolhida:
        verifica_se_ganhou()
        i = 0
        while i < len(lista_palavra_escolhida):
            if letra_digitada == lista_palavra_escolhida[i]:
                lista_palavra_secreta[i] = letra_digitada
            i += 1
        verifica_se_ganhou()
    else:
        erro += 1

def inicia_lista_palavra_secreta():

    for p in lista_palavra_escolhida:
        lista_palavra_secreta.append('_')

def verifica_se_ganhou():
    if lista_palavra_escolhida == lista_palavra_secreta or letra_digitada == palavra_escolhida:
        os.system('cls')
        print(f'Você ganhou! A palavra era "{palavra_escolhida}".')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        input('Pressione <enter> para finalizar')
        sys. exit()

def desenho_forca():
    if erro == 0:
        print(' _______   ')
        print('|/      |  ')
        print('|          ')
        print('|          ')
        print('|          ')
        print('|          ')
        print('|________ ')
    elif erro == 1:
        print(' _______   ')
        print('|/      |  ')
        print('|     (ಠ_ಠ) ')  
        print('|          ')
        print('|          ')
        print('|          ')
        print('|________  ')  
    elif erro == 2:
        print(' _______   ')
        print('|/      |  ')
        print('|     (ಠ_ಠ) ')
        print('|       |  ')
        print('|          ')
        print('|          ')
        print('|________  ') 
    elif erro == 3:
        print(' _______   ')
        print('|/      |  ')
        print('|     (ಠ_ಠ) ')
        print('|       |  ')
        print('|       |  ')
        print('|          ')
        print('|________  ') 
    elif erro == 4:
        print(' _______   ')
        print('|/      |  ')
        print('|     (ಠ_ಠ) ')
        print('|      /|\ ')
        print('|       |  ')
        print('|          ')
        print('|________  ') 
    else:
        print(' _______   ')
        print('|/      |  ')
        print('|     (ಠ_ಠ) ')
        print('|      /|\ ')
        print('|       |  ')
        print('|      / \ ')
        print('|________  ')

lista_palavras = ['morango', 'banana', 'uva', 'melancia', 'laranja']
erro = 0
palavra_escolhida = random.choice(lista_palavras)
lista_palavra_escolhida = list(palavra_escolhida)
lista_palavra_secreta = []

inicia_lista_palavra_secreta()

while True:

    os.system('cls')

    if erro == 5:
        desenho_forca()
        input('Você perdeu! Pressione <enter> para finalizar!')
        
        break
    else:
        desenho_forca()

        print(lista_palavra_secreta)
        print(f'Erros: {erro}')
        print('Dica: Fruta')
        letra_digitada = input('Digite uma letra: ')

        verifica_letra()