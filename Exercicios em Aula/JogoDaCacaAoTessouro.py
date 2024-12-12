import emoji  # Biblioteca para usar emojis no código, como ícones de cobra, folha, etc.
import random  # Biblioteca para gerar números aleatórios.
import pygame  # Biblioteca para criar jogos 2D.
from pygame.locals import *  # Importa constantes e funções do Pygame.

# Inicializa o Pygame, configurando sua base para o funcionamento do jogo.
pygame.init()

# Emojis que serão usados no tabuleiro para representar diferentes elementos.
emoji_folha = emoji.emojize('🌹')  # Representa um espaço vazio no tabuleiro.
ovos = emoji.emojize('🪺')  # Representa os ovos que a cobra deve encontrar.
cobra = emoji.emojize('🐍')  # Representa a cobra no tabuleiro.
buraco = emoji.emojize('🟤')  # Representa um buraco (espaço onde a cobra já passou e errou).

# Função para criar o tabuleiro com um número fixo de "folhas" em cada posição.
def gerar_tabuleiro(tabuleiro, len_tabuleiro):
    for _ in range(len_tabuleiro):
        tabuleiro.append(emoji_folha)  # Adiciona folhas em todas as posições do tabuleiro.

# Função que imprime o tabuleiro organizado em linhas e colunas.
def printa_tabuleiro(tabuleiro, n_linhas, n_colunas):
    for i in range(0, n_linhas * n_colunas, n_colunas):  # Itera linha por linha.
        for j in range(n_colunas):  # Itera coluna por coluna.
            print(f'{tabuleiro[j + i]} ', end='')  # Imprime o emoji correspondente.
        print('\n')  # Quebra a linha para organizar o visual do tabuleiro.

# Inicializa o tabuleiro como uma lista vazia e uma lista para guardar buracos.
tb = []
buracos = []

# Configura as dimensões do tabuleiro e gera sua estrutura inicial.
n_linhas = 3  # Número de linhas do tabuleiro.
n_colunas = 4  # Número de colunas do tabuleiro.
tamanho_tabuleiro = n_linhas * n_colunas  # Calcula o número total de posições.
gerar_tabuleiro(tb, tamanho_tabuleiro)  # Preenche o tabuleiro com folhas.

# Define a posição inicial da cobra no tabuleiro (sempre no índice 0).
pos_snake = 0
tb[pos_snake] = cobra  # Coloca o emoji da cobra na posição inicial.

# Define a posição dos ovos aleatoriamente, garantindo que não sejam colocados na posição inicial da cobra.
pos_ovos = random.randint(0, tamanho_tabuleiro - 1)
while pos_ovos == pos_snake:  # Garante que ovos e cobra não começam no mesmo lugar.
    pos_ovos = random.randint(0, tamanho_tabuleiro - 1)

# Mostra o tabuleiro inicial no console.
printa_tabuleiro(tb, n_linhas, n_colunas)

# Configura uma janela do Pygame (necessária para capturar teclas, mas aqui não será usada visualmente).
tela = pygame.display.set_mode((1, 1))

# Função para atualizar a posição da cobra no tabuleiro.
def atualiza_pos_cobra(pos_anterior_S, pos_snake):
    if pos_anterior_S in buracos:  # Se a posição anterior já era um buraco.
        tb[pos_anterior_S] = buraco  # Mantém o emoji de buraco.
    else:
        tb[pos_anterior_S] = emoji_folha  # Restaura o emoji de folha.
    tb[pos_snake] = cobra  # Atualiza a nova posição com o emoji da cobra.

tentativas = 6  # Número máximo de tentativas que o jogador tem.

# Loop principal do jogo (permanece ativo enquanto o jogador não vence ou esgota as tentativas).
rodando = True
while rodando and tentativas > 0:
    for evento in pygame.event.get():  # Captura os eventos do teclado.
        if evento.type == QUIT:  # Se o jogador fechar a janela do jogo.
            rodando = False  # Termina o jogo.
        elif evento.type == KEYDOWN:  # Se uma tecla foi pressionada.
            pos_anterior_S = pos_snake  # Salva a posição anterior da cobra.

            # Move a cobra para a esquerda, se possível.
            if evento.key == K_LEFT and pos_snake % n_colunas > 0:
                pos_snake -= 1
            # Move a cobra para a direita, se possível.
            elif evento.key == K_RIGHT and pos_snake % n_colunas < n_colunas - 1:
                pos_snake += 1
            # Move a cobra para cima, se possível.
            elif evento.key == K_UP and pos_snake >= n_colunas:
                pos_snake -= n_colunas
            # Move a cobra para baixo, se possível.
            elif evento.key == K_DOWN and pos_snake < tamanho_tabuleiro - n_colunas:
                pos_snake += n_colunas
            # Verifica se a tecla Enter foi pressionada para confirmar uma ação.
            elif evento.key == K_RETURN:
                if pos_snake == pos_ovos:  # Se a cobra encontrar os ovos.
                    tb[pos_snake] = ovos  # Substitui a posição com os ovos.
                    print('\n' * 100)  # Limpa o console.
                    printa_tabuleiro(tb, n_linhas, n_colunas)  # Mostra o tabuleiro final.
                    rodando = False  # Termina o jogo.
                else:
                    tb[pos_snake] = buraco  # Marca a posição como buraco.
                    buracos.append(pos_snake)  # Adiciona a posição aos buracos.
                    tentativas -= 1  # Reduz o número de tentativas restantes.

            # Atualiza o tabuleiro com a nova posição da cobra.
            atualiza_pos_cobra(pos_anterior_S, pos_snake)

            # Limpa o console e reimprime o tabuleiro atualizado.
            print('\n' * 100)
            print(f'Você ainda tem {tentativas} tentativas restantes\n')
            printa_tabuleiro(tb, n_linhas, n_colunas)

# Mostra a mensagem final, dependendo se o jogador venceu ou perdeu.
if tentativas > 0:
    print("Parabéns você encontrou os ovos! Boa refeição")
else:
    tb[pos_ovos] = ovos  # Mostra a posição dos ovos para o jogador.
    print('\n' * 100)
    printa_tabuleiro(tb, n_linhas, n_colunas)
    print("Desculpe acabou as tentativas")

# Encerra o Pygame.
pygame.quit()
