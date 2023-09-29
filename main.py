import pygame
import sys


pygame.init()


LARGURA, ALTURA = 300, 300
TAMANHO_QUADRADO = LARGURA // 3
COR_FUNDO = (255, 255, 255)
COR_LINHA = (0, 0, 0)
TAMANHO_LINHA = 15


janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tic-Tac-Toe")


tabuleiro = [['' for _ in range(3)] for _ in range(3)]


def desenhar_tabuleiro():
    for linha in range(1, 3):
        pygame.draw.line(janela, COR_LINHA, (0, linha * TAMANHO_QUADRADO), (LARGURA, linha * TAMANHO_QUADRADO), TAMANHO_LINHA)
        pygame.draw.line(janela, COR_LINHA, (linha * TAMANHO_QUADRADO, 0), (linha * TAMANHO_QUADRADO, ALTURA), TAMANHO_LINHA)


def desenhar_simbolos():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 'X':
                x_pos = coluna * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2
                y_pos = linha * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2
                pygame.draw.line(janela, COR_LINHA, (x_pos - 30, y_pos - 30), (x_pos + 30, y_pos + 30), TAMANHO_LINHA)
                pygame.draw.line(janela, COR_LINHA, (x_pos + 30, y_pos - 30), (x_pos - 30, y_pos + 30), TAMANHO_LINHA)
            elif tabuleiro[linha][coluna] == 'O':
                x_pos = coluna * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2
                y_pos = linha * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2
                pygame.draw.circle(janela, COR_LINHA, (x_pos, y_pos), 30, TAMANHO_LINHA)


def verificar_vencedor():
   
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != '':
            return tabuleiro[linha][0]

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != '':
            return tabuleiro[0][coluna]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != '':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != '':
        return tabuleiro[0][2]

    return None


jogador_atual = 'X'
vencedor = None
jogo_acabou = False

# Loop principal do jogo
while not jogo_acabou:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN and not vencedor:
            x, y = evento.pos
            coluna = x // TAMANHO_QUADRADO
            linha = y // TAMANHO_QUADRADO

            if tabuleiro[linha][coluna] == '':
                tabuleiro[linha][coluna] = jogador_atual
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        vencedor = verificar_vencedor()
        if vencedor:
            jogo_acabou = True

    janela.fill(COR_FUNDO)
    desenhar_tabuleiro()
    desenhar_simbolos()

    if vencedor:
        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(f"Jogador {vencedor} venceu!", True, COR_LINHA)
        retangulo_texto = texto.get_rect(center=(LARGURA // 2, ALTURA // 2))
        janela.blit(texto, retangulo_texto)
        pygame.display.flip()
        pygame.time.wait(2000)  

    pygame.display.update()
