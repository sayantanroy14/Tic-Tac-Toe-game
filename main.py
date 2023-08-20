import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the board
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Draw the grid
def draw_grid():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw the X and O symbols
def draw_symbols():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE), ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)
                pygame.draw.line(screen, LINE_COLOR, ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE), (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2, LINE_WIDTH)

# Check for a win or tie
def check_winner(symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    
    # Check columns
    for col in range(BOARD_COLS):
        if all(board[row][col] == symbol for row in range(BOARD_ROWS)):
            return True
    
    # Check diagonals
    if all(board[i][i] == symbol for i in range(BOARD_ROWS)) or all(board[i][BOARD_COLS - 1 - i] == symbol for i in range(BOARD_ROWS)):
        return True
    
    return False

# Main game loop
turn = 'X'
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            
            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = turn
                if check_winner(turn):
                    game_over = True
                elif all(cell != '' for row in board for cell in row):
                    game_over = True
                else:
                    turn = 'O' if turn == 'X' else 'X'
    
    screen.fill(BG_COLOR)
    draw_grid()
    draw_symbols()
    pygame.display.update()

# Game loop ended, wait for a while before quitting
pygame.time.wait(2000)
pygame.quit()
sys.exit()
