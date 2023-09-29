def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    # Verificar colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def tabuleiro_cheio(tabuleiro):
    return all(celula != ' ' for linha in tabuleiro for celula in linha)

def main():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'

    print("Bem-vindo ao Jogo da Velha!")
    #jogo da velha chamado tambem de tic tac toe

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha, coluna = map(int, input(f'Jogador {jogador_atual}, insira a linha (0, 1, 2) e coluna (0, 1, 2) separadas por espaço: ').split())

        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break
        elif tabuleiro_cheio(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if __name__ == "__main__":
    main()
