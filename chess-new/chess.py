import pygame
from board.board import Board
from constants import *

pygame.init()


class Chess(Board):
    def __init__(self, screen: pygame.display):
        super().__init__(screen)

        self.white_pieces: list[str] = \
            [
                "r", "kn", "b", "q", "k", "b", "kn", "r",
                "p", "p", "p", "p", "p", "p", "p", "p"
            ]

        self.white_pos: list[tuple[int, int]] = \
            [
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)
            ]

        self.black_pieces: list[str] = \
            [
                "r", "kn", "b", "q", "k", "b", "kn", "r",
                "p", "p", "p", "p", "p", "p", "p", "p"
            ]

        self.black_pos: list[tuple[int, int]] = \
            [
                (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)
            ]

    def draw_pieces(self):
        for i in range(len(self.white_pos)):
            piece = self.white_pieces[i]
            pos = super().square_to_pos(self.white_pos[i])
            image = white_images[piece.index(piece)]
            self.screen.blit(image, pos)


