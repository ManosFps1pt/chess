import pygame
from board.board import Board
from constants import *
from chess import Chess

pygame.init()
chess = Chess(screen)

while run:
    screen.fill("#000000")
    chess.draw_board()
    chess.draw_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run &= False
        if event.type == pygame.MOUSEBUTTONDOWN:
            square = chess.get_square_clicked()
            print(f"click detected. Board square clicked, mouse pos: {square}")
            chess.add_squares_to_mark(square)
            chess.flip_board()
    chess.mark_squares()
    pygame.display.update()
    clock.tick()
    pygame.display.set_caption(f"board module implementation - Chess. FPS: {round(clock.get_fps(), 2)}")

pygame.quit()
