import pygame
import sys

pygame.init()

width = 800
height = 800
square_size = width // 8

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess')

white = (255, 255, 255)
black = (0, 0, 0)
grey = (169, 169, 169)
blue = (0, 0, 255)

font = pygame.font.SysFont('Arial', 40)

def draw_board():
    colors = [white, grey]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(window, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '--':
                piece_text = font.render(piece, True, black if piece[0] == 'w' else white)
                window.blit(piece_text, (col * square_size + 15, row * square_size + 15))

def create_initial_board():
    board = [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
    ]
    return board

def main():
    board = create_initial_board()
    selected_piece = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // square_size
                row = pos[1] // square_size
                if selected_piece:
                    board[selected_piece[0]][selected_piece[1]], board[row][col] = '--', board[selected_piece[0]][selected_piece[1]]
                    selected_piece = None
                else:
                    if board[row][col] != '--':
                        selected_piece = (row, col)

        draw_board()
        draw_pieces(board)
        pygame.display.flip()

if __name__ == "__main__":
    main()
