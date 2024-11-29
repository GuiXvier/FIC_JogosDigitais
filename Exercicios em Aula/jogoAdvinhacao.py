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