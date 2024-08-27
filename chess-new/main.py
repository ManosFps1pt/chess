import pygame
from board.board import Board

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

board = Board(screen)
board.__size = 800, 800

run = True

while run:
    screen.fill("#000000")
    board.draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(board.get_square_clicked())

    pygame.display.update()
    clock.tick()
    pygame.display.set_caption(f"board module implementation. FPS: {int(clock.get_fps())}")
