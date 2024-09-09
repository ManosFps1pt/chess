from itertools import chain
from typing import List, Tuple

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
                (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)
            ]
        self.white_squares_reachable: set[tuple[int, int]] = set()

        self.black_pieces: list[str] = \
            [
                "r", "kn", "b", "q", "k", "b", "kn", "r",
                "p", "p", "p", "p", "p", "p", "p", "p"
            ]

        self.black_pos: list[tuple[int, int]] = \
            [
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)
            ]

        self.black_squares_reachable: set[tuple[int, int]] = set()

    def draw_pieces(self):
        for i in range(len(self.white_pos)):
            piece: str = self.white_pieces[i]
            pos: tuple[int, int] = self.square_to_pos(self.white_pos[i])
            image = white_images[piece]
            self.screen.blit(image, pos)

        for i in range(len(self.black_pos)):
            piece: str = self.black_pieces[i]
            pos: tuple[int, int] = self.square_to_pos(self.black_pos[i])
            image = black_images[piece]
            self.screen.blit(image, pos)

    def pawn_available(self, pos: tuple[int, int], is_white: bool) -> list[tuple[int, int]]:
        moves_list = []
        if is_white:
            friendly_list = self.white_pos
            enemy_list = self.black_pos
            if (pos[0], pos[1] + 1) not in friendly_list and (pos[0], pos[1] + 1) not in enemy_list and pos[1] <= 6:
                moves_list.append((pos[0], pos[1] + 1))
                if (pos[0], pos[1] + 2) not in friendly_list and (pos[0], pos[1] + 2) not in enemy_list and pos[1] == 1:
                    moves_list.append((pos[0], pos[1] + 2))
            if (pos[0] + 1, pos[1] + 1) in enemy_list:
                moves_list.append((pos[0] + 1, pos[1] + 1))
            if (pos[0] - 1, pos[1] + 1) in enemy_list:
                moves_list.append((pos[0] - 1, pos[1] + 1))
        else:
            friendly_list = self.black_pos
            enemy_list = self.white_pos
            if (pos[0], pos[1] - 1) not in friendly_list and (pos[0], pos[1] - 1) not in enemy_list and pos[1] >= 1:
                moves_list.append((pos[0], pos[1] - 1))
                if (pos[0], pos[1] - 2) not in friendly_list and (pos[0], pos[1] - 2) not in enemy_list and pos[1] == 6:
                    moves_list.append((pos[0], pos[1] - 2))
            if (pos[0] + 1, pos[1] - 1) in enemy_list:
                moves_list.append((pos[0] + 1, pos[1] - 1))
            if (pos[0] - 1, pos[1] - 1) in enemy_list:
                moves_list.append((pos[0] - 1, pos[1] - 1))
        return moves_list

    def bishop_available(self, pos: tuple[int, int], is_white: bool) -> list[tuple[int, int]]:
        moves_list: list[tuple[int, int]] = []
        if is_white:
            friendly_list = self.white_pos
            enemy_list = self.black_pos
        else:
            friendly_list = self.black_pos
            enemy_list = self.white_pos
        for i in range(4):
            match i:
                case 0:
                    direction: tuple[int, int] = 1, 1
                case 1:
                    direction: tuple[int, int] = 1, -1
                case 2:
                    direction: tuple[int, int] = -1, 1
                case 3:
                    direction: tuple[int, int] = -1, -1
                case _:
                    direction: tuple[int, int] = 0, 0 # not accessible

            chain: int = 1
            path = True
                checking_square: tuple[int, int] = pos[0] + (chain * direction[0]), pos[1] + (chain * direction[1])
                if checking_square not in friendly_list and 0 <= checking_square[0] <= 7:
                    moves_list.append(checking_square)
                    if checking_square in enemy_list:
                        path = False


        return moves_list

if __name__ == "__main__":
    clock = pygame.time.Clock()
    run: bool = True
    chess = Chess(screen)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                square_clicked = chess.get_square_clicked()


        pygame.display.set_caption(f"fps: {int(clock.get_fps())}")

        screen.fill("#000000")
        chess.draw_board()
        chess.draw_pieces()
        chess.mark_squares()
        pygame.display.update()
        clock.tick()
