import pygame
from GUI.board_GUI import Board

from logic.logic import ChessLogic

pygame.init()
board = Board((600, 600), ("#ffffff", "#000000"), (100, 100), {"color": "#0000ff", "thickness": 5}, 5)
# help(board)
logic = ChessLogic((600, 600), ("#ffffff", "#000000"), (100, 100), {"color": "#0000ff", "thickness": 5}, 5)

board.pieces_setup()
surface = pygame.Surface((800, 800))
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))

run = True

board.refresh = True
while run:
    pygame.display.update()
    screen.fill("#111111")
    board.draw_board()
    board.draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick()
    fps = int(clock.get_fps())
    pygame.display.set_caption(f"chess {fps} fps")

pygame.quit()
print("----------------| execution finished successfully |----------------------------------------------------------------")
