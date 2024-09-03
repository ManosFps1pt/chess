import pygame
from board.board import Board
from constants import *

pygame.init()


while run:
    screen.fill("#000000")
    board.draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run &= False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(board.get_square_clicked())

    pygame.display.update()
    clock.tick()
    pygame.display.set_caption(f"board module implementation - Chess. FPS: {int(clock.get_fps())}")

pygame.quit()
