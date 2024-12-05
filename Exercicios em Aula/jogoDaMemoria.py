import emoji  # Biblioteca para usar emojis no código.
import random  # Biblioteca para trabalhar com operações aleatórias, como embaralhar listas.

# Definindo o número de linhas e colunas do tabuleiro do jogo.
n_linhas = 4  # O tabuleiro terá 4 linhas.
n_colunas = 3  # O tabuleiro terá 3 colunas.

# Função que retorna o tamanho de um tabuleiro (ou lista).
def tamanhoTabuleiro(tab):
    return len(tab)  # Retorna a quantidade de elementos na lista.

# Função para gerar um tabuleiro oculto com um emoji de carta em todas as posições.
def gerar_tabuleiro(tabuleiro, n_objetos):
    for i in range(0, n_objetos):  # Para cada posição no tabuleiro...
        tabuleiro.append(emoji_carta)  # Adiciona o emoji de carta

# Função que imprime o tabuleiro organizado em linhas e colunas.
def printa_tabuleiro(tabuleiro, n_linhas, n_colunas):
    for i in range(0, n_linhas * n_colunas, n_colunas):  # Itera sobre cada linha do tabuleiro.
        for j in range(n_colunas):  # Itera sobre cada coluna na linha atual.
            print(f'{tabuleiro[j + i]} ', end='')  # Imprime o emoji da posição correspondente.
        print('\n')  # Move para a próxima linha após imprimir todas as colunas.

# Função que permite ao jogador fazer duas escolhas de posições no tabuleiro.
def escolhas(listaDeAcertos):
    # Jogador escolhe a primeira posição.
    posicao1 = int(input("Escolha uma posicao: "))

    # Revela o emoji da primeira posição escolhida no tabuleiro.
    tabuleiro[posicao1] = tabuleiro_oculto[posicao1]
    printa_tabuleiro(tabuleiro, n_linhas, n_colunas)  # Mostra o tabuleiro atualizado.

    # Jogador escolhe a segunda posição.
    posicao2 = int(input("Escolha uma segunda posicao: "))
    tabuleiro[posicao2] = tabuleiro_oculto[posicao2]  # Revela o emoji da segunda posição.

    printa_tabuleiro(tabuleiro, n_linhas, n_colunas)  # Mostra o tabuleiro novamente.

    # Verifica se os emojis das duas posições escolhidas são iguais.
    resultado = tabuleiro[posicao2] == tabuleiro[posicao1]

    if resultado:  # Se forem iguais...
        listaDeAcertos.append(tabuleiro[posicao1])  # Adiciona o emoji à lista de acertos.

    return resultado  # Retorna se as escolhas foram iguais (True/False).

# Emojis usados no jogo.
emoji_carta = emoji.emojize(':flower_playing_cards:')  # Emoji genérico (carta virada para baixo).

# Lista de emojis que representam os pares no jogo.
abacate = emoji.emojize(':avocado:')
urso = emoji.emojize(':bear:')
tijolo = emoji.emojize(':brick:')
cavalo = emoji.emojize(':carousel_horse:')
guarda_chuva = emoji.emojize(':closed_umbrella:')
carinha = emoji.emojize(':confounded_face:')

# Cria a lista de emojis ocultos no tabuleiro (pares de cada emoji).
tabuleiro_oculto = [abacate, abacate, urso, urso, tijolo, tijolo, cavalo, cavalo, guarda_chuva, guarda_chuva, carinha, carinha]
random.shuffle(tabuleiro_oculto)  # Embaralha os emojis para torná-los aleatórios.

# Tabuleiro inicial (com todas as posições viradas para baixo).
tabuleiro = []
gerar_tabuleiro(tabuleiro, tamanhoTabuleiro(tabuleiro_oculto))  # Preenche o tabuleiro com emojis genéricos.

# Início do jogo.
print("==== Bem Vindo ao meu jogo da Memoria ====")

printa_tabuleiro(tabuleiro, n_linhas, n_colunas)  # Mostra o tabuleiro inicial (cartas viradas para baixo).

# Variáveis para acompanhar o progresso do jogo.
acertos = 0  # Quantidade de pares encontrados.
lista_de_acertos = []  # Lista de emojis que já foram acertados.

# Loop principal do jogo: continua até o jogador encontrar todos os pares.
while acertos < tamanhoTabuleiro(tabuleiro_oculto) / 2:
    resultado = escolhas(lista_de_acertos)  # Jogador faz uma jogada.

    if (not resultado) and acertos == 0:  # Se não acertar e não houver pares encontrados ainda...
        tabuleiro = []  # Reseta o tabuleiro.
        gerar_tabuleiro(tabuleiro, tamanhoTabuleiro(tabuleiro_oculto))  # Preenche com emojis genéricos.
    elif not resultado and acertos > 0:  # Se não acertar, mas já houver pares encontrados...
        for i in range(len(tabuleiro)):  # Percorre todo o tabuleiro.
            for objeto in lista_de_acertos:  # Verifica se uma posição já foi acertada.
                if tabuleiro[i] != objeto:  # Se não foi acertada...
                    tabuleiro[i] = emoji_carta  # Volta para o emoji de carta.
    else:  # Se acertar o par...
        acertos += 1  # Incrementa o número de pares encontrados.

    print("===============================================================\n")
    printa_tabuleiro(tabuleiro, n_linhas, n_colunas)  # Mostra o estado atualizado do tabuleiro.

# Fim do jogo: o jogador encontrou todos os pares.
print("Parabéns você ganhou")
