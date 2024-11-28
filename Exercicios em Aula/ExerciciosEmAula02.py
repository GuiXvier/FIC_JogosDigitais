"""
Crie um jogo de advinhação onde o jogador deve advinhar um numero 
aleatorio entre 1 e 20 
"""
import random

# Funcao que define o range do numero aleatorio e onde as perguntas do jogo são feitas
def rangeDoNumero(inicio, fim, nome):
    numeroAleatorio = random.randint(inicio, fim+1)

    for num in range(1, 6, 1):
        tentativa = int(input("Digite um numero: "))
        if tentativa > numeroAleatorio:
            print(f'{nome} o numero misterioso é menor que {tentativa}')
        elif tentativa < numeroAleatorio:
            print(f'{nome} o numero misterioso é maior que {tentativa}')
        else:
            print(f'Parabéns {nome} você acertou! O numero misterioso é {numeroAleatorio}')
            break
        
        # Se o numero de tentativas for igual a 5 então você chegou ao limite
        if num == 5:
            print('Numero de tentaivas esgotadas, o numero continua misterioso')
            print(f'Mentira ele era {numeroAleatorio}')
            break

def rangeDoNumeroWhile(nome):
    venceu = False
    tentativas = 0
    numeroAleatorio = random.randint(1, 21)

    while not(venceu) and tentativas < 5:
        tentativa = int(input("Digite um numero: "))
        if tentativa > numeroAleatorio:
            print(f'{nome} o numero misterioso é menor que {tentativa}')
        elif tentativa < numeroAleatorio:
            print(f'{nome} o numero misterioso é maior que {tentativa}')
        else:
            print(f'Parabéns {nome} você acertou! O numero misterioso é {numeroAleatorio}')
            break

# Parte onde o jogador deve escolher o modo de jogo
jogador = input("Informe seu nome: ")
print("Ecolha o modo de jogo:\n1 - Numero aleatorio de 1 a 20\n2 - Numero aleatorio de um range a sua escolha")
modoDeJogo = eval(input("Digite o numero do modo de jogo: "))

# Se o modo escolhido for 1 será gerado um numero aleatorio de 1 a 20
if modoDeJogo == 1:
    rangeDoNumero(1, 20, jogador)
# Se o modo de jogo for 2 o numero aletorio será em um range indicado pelo usuário
elif modoDeJogo == 2:
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    rangeDoNumero(inicio, fim, jogador)

#==============================================================================

"""
Desenvolva um jogo da forca
"""

import random

# Lista com as "imagens" dos estagios da forca 
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Nome do arquivo que contém as palavras 
file_name = 'listaDePalavras.txt'

# Funcao que abre o arquivo no modo de leitura 
with open(file_name, 'r') as fl_objetct:
    contents =  fl_objetct.read()
    # Coloca o conteudo do arquivo em uma lista 
    words = contents.split()

    # Chama a funcao randit para um indice de uma palavra aleatoria
    # com base no tamanho da lista de palavras
    numPalavraAleatoria = random.randint(1, len(words))
    # Palavra aleatoria da lista de palavras
    palavraAleatoria = words[numPalavraAleatoria]
    # Indice atual da lista de figuras do homem na forca
    numPicHangMan = 0

    # Qual caracter de tentaiva do usuario
    tentativa = ''
    # Qual palavra formada pelo usuario ate agora
    palavraFormada = ''

    # Lista contendo as letras acertadas 
    listaDeLetrasAcertadas = list()
    # Lista contando o numero de letras tentadas 
    listaDeLetrasTentadas = list()
    # Lista contendo o modelo de diplay de letras
    # Ex.: a _ _ b _
    listaDePalavras = list()

    # Inicialmento o display de letras estará vazio, entao todas
    # estarão com "_ _ _"
    for caracter in palavraAleatoria:
        listaDePalavras.append('_')

    # Laço principal do jogo onde suas condições são: A "imagem" da forca
    # nao ser a ultima e a palavra formada ser diferente da palavra aleatoria
    while (numPicHangMan < (len(HANGMANPICS) - 1)) and (palavraFormada != palavraAleatoria):
        # Printa a forca atual
        print(HANGMANPICS[numPicHangMan])
        print('\n')

        # Para cada carcter na lista de palavras, será printado o display
        # de palavras 
        for caracter in listaDePalavras:
            print(f'{caracter} ', end='')
        print("\n")

        # Pede uma tentativa ao usuario
        tentativa = input("Digite a letra: ")

        # Se a palavra alatoria contem o caracter tentado pelo usuario 
        # esse carater sera adcionado a lista de palavras acertadas
        # e um indice será criado para saber o indice exato do caracter na palavra aleatoria
        if palavraAleatoria.__contains__(tentativa):
            listaDeLetrasAcertadas.append(tentativa)
            indice = 0
            for letra in palavraAleatoria:
                if letra == tentativa:
                    listaDePalavras[indice] = letra
                indice += 1
            # Se a lista de letras tentandas nao contem o caracter do 
            # usuario, esse caracter sera adcionado a lista
            if not (listaDeLetrasTentadas.__contains__(tentativa)):
                listaDeLetrasTentadas.append(tentativa)
        # Se não, o usuario errou a letra e a imagem da forca deve ser 
        # atualizada
        else:
            if not (listaDeLetrasTentadas.__contains__(tentativa)):
                listaDeLetrasTentadas.append(tentativa)
            numPicHangMan += 1

        print(f'\nLista de letras tentadas até agora: {listaDeLetrasTentadas}')

        # Palavra formada ate agora pelo usuario
        palavraFormada = ''.join(listaDePalavras)

# Se a imagem da forca eh a ultima mostre a mensagem de Game Over
if numPicHangMan == (len(HANGMANPICS) - 1):
    print(HANGMANPICS[6])
    print("Voce morreu, sinto muito :(\nA palavra era: ", palavraAleatoria)  
# Se o usuario acertou, mostre a palavra formada no display e a mensagem de parabéns
elif (palavraFormada == palavraAleatoria):
    for caracter in listaDePalavras:
            print(f'{caracter} ', end='')
    print("\n")
    print('Parabéns você acertou!!!')