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



if __name__ == "__main__":
    clock = pygame.time.Clock()
    run: bool = True
    chess = Chess(screen)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run &= False
            if event.type == pygame.MOUSEBUTTONDOWN:
                square = chess.get_square_clicked()
                print(square)
                chess.add_square_to_mark(square)
                chess.invert_board()

        pygame.display.set_caption(f"fps: {int(clock.get_fps())}")

        screen.fill("#000000")
        chess.draw_board()
        chess.draw_pieces()
        chess.mark_squares()
        pygame.display.update()
        clock.tick()
