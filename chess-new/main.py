import pygame
from board.board import Board
from constants import *
from chess import Chess

pygame.init()
chess = Chess(screen)
chess.board_inverted = False
while run:
    screen.fill("#000000")
    chess.draw_board()
    chess.draw_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run &= False
        if event.type == pygame.MOUSEBUTTONDOWN:
            chess.clear_marked_squares()
            square = chess.get_square_clicked()
            print(f"click detected. Board square clicked, mouse pos: {pygame.mouse.get_pos()}, square: {square}, "
                  f"to pos: {chess.square_to_pos(square)}")
            chess.add_squares_to_mark(chess.rook_available(square, False))
    chess.mark_squares()
    pygame.display.update()
    clock.tick()
    pygame.display.set_caption(f"board module implementation - Chess. FPS: {round(clock.get_fps(), 2)}")

pygame.quit()
