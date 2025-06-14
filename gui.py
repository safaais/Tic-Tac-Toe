# gui.py
import pygame
from tic_tac_toe import TicTacToe
from q_learning_ai import QLearningAgent

# colors
WIDTH, HEIGHT = 300, 350
BG_COLOR = (255, 248, 236)       
LINE_COLOR = (80, 80, 80)        
X_COLOR = (231, 76, 60)            
O_COLOR = (52, 152, 219)        
TEXT_COLOR = (44, 62, 80)         
HIGHLIGHT = (255, 223, 186)      

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe AI")
font = pygame.font.SysFont("Arial", 72, bold=True)
msg_font = pygame.font.SysFont("Arial", 24, bold=True)

def draw_board(board, message=""):
    screen.fill(BG_COLOR)
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * 100), (300, i * 100), 4)
        pygame.draw.line(screen, LINE_COLOR, (i * 100, 0), (i * 100, 300), 4)

    for i in range(9):
        x = (i % 3) * 100 + 30
        y = (i // 3) * 100 + 10
        if board[i] == 'X':
            text = font.render('X', True, X_COLOR)
            screen.blit(text, (x, y))
        elif board[i] == 'O':
            text = font.render('O', True, O_COLOR)
            screen.blit(text, (x, y))

    pygame.draw.rect(screen, HIGHLIGHT, (0, 300, 300, 50))
    msg_surface = msg_font.render(message, True, TEXT_COLOR)
    screen.blit(msg_surface, (10, 310))

def get_square(pos):
    x, y = pos
    if y >= 300:
        return None
    return (y // 100) * 3 + (x // 100)

def main():
    agent = QLearningAgent()
    agent.load()
    game = TicTacToe()
    player = 'X'
    running = True
    game_over = False
    message = "You are X - AI is O"

    draw_board(game.board, message)
    pygame.display.update()

    while running:
        if player == 'O' and not game_over:
            pygame.time.delay(400)
            action = agent.choose_action(game, 'O')
            game.make_move(action, 'O')
            player = 'X'

        draw_board(game.board, message)
        pygame.display.update()

        if game.current_winner:
            message = f"{game.current_winner} wins!"
            game_over = True
        elif game.is_full():
            message = "It's a tie!"
            game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not game_over:
                    square = get_square(pygame.mouse.get_pos())
                    if square is not None and game.make_move(square, 'X'):
                        player = 'O'
                else:
                    game.reset()
                    player = 'X'
                    game_over = False
                    message = "You are X - AI is O"

    pygame.quit()

if __name__ == '__main__':
    main()
