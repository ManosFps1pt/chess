import pygame

pygame.init()


class Board:
    def __init__(self, screen: pygame.display):
        self.screen: pygame.display = screen
        self.__size: tuple[int, int] = 600, 600
        self.colors: tuple[int | str, int | str] = "#aaaaaa", "#000000"
        self.top_left: tuple[int, int] = 100, 100
        self.outline_color = "#002200"
        self.outline_thickness = 10
        self.__squares_to_mark: set[tuple[int, int]] = set()
        self.__square_size: tuple[int, int] = self.__size[0] // 8, self.__size[1] // 8
        self.index_row_dict: dict[int:str] = {
            0: "A",
            1: "B",
            2: "C",
            3: "D",
            4: "E",
            5: "F",
            6: "G",
            7: "H"
        }

        self.__board_inverted: bool = False

    @property
    def board_inverted(self):
        return self.__board_inverted

    @board_inverted.setter
    def board_inverted(self, val: bool):
        if type(val) == type(bool):
            self.__board_inverted = val

    def flip_board(self):
        self.__board_inverted ^= True  # xor boolean operation : 0, 0 -> 0 | 0, 1 -> 1 | 1, 0 -> 1 | 1, 1 -> 0

    @property
    def squares_to_mark(self) -> set[tuple[int, int]]:
        return self.__squares_to_mark

    def clear_marked_squares(self) -> None:
        self.__squares_to_mark = set()

    def add_squares_to_mark(self, squares: list[tuple[int, int]]) -> None:
        if squares is not None:
            for i in squares:
                if i is not None:
                    self.__squares_to_mark.add(i)

    @property
    def size(self) -> tuple[int, int]:
        return self.__size

    @size.setter
    def size(self, value: tuple[int, int]) -> None:
        self.__size = value
        self.__square_size = self.__size[0] // 8, self.__size[1] // 8

    @property
    def square_size(self) -> tuple[int, int]:
        return self.__square_size

    @staticmethod
    def key_from_value(dictionary: dict, value: object):
        return list(dictionary.keys())[list(dictionary.values()).index(value)]

    def index_to_row(self, x: int) -> str:
        return self.index_row_dict[x]

    def row_to_index(self, x: str) -> int:
        return self.key_from_value(self.index_row_dict, x)

    @staticmethod
    def index_to_colum(x: int) -> int:
        return x + 1

    @staticmethod
    def colum_to_index(x: int) -> int:
        return x - 1

    def draw_board(self) -> None:
        """Draw the board"""
        # outline
        pygame.draw.rect(
            self.screen,
            self.outline_color,
            pygame.Rect(
                self.top_left[0] - self.outline_thickness,
                self.top_left[1] - self.outline_thickness,
                self.__size[0] + self.outline_thickness * 2,
                self.__size[1] + self.outline_thickness * 2
            )
        )

        pygame.draw.rect(
            self.screen,
            self.outline_color,
            pygame.Rect(
                self.top_left[0] - 5,
                self.top_left[1] - 5,
                self.__size[0] + 10,
                self.__size[1] + 10
            )
        )

        # color a (white)
        if self.__board_inverted:
            pygame.draw.rect(
                self.screen,
                self.colors[1],
                pygame.Rect(
                    self.top_left[0],
                    self.top_left[1],
                    self.__size[0],
                    self.__size[1]
                )
            )
        else:
            pygame.draw.rect(
                self.screen,
                self.colors[0],
                pygame.Rect(
                    self.top_left[0],
                    self.top_left[1],
                    self.__size[0],
                    self.__size[1]
                )
            )

        # color b (black)
        if self.__board_inverted:
            for i in range(32):
                colum = i // 4
                row = (i % 4) * 2
                if colum % 2 == 0:
                    row += 1
                x = (row * self.__square_size[0]) + self.top_left[0]
                y = (colum * self.__square_size[1]) + self.top_left[1]
                pygame.draw.rect(self.screen, self.colors[0],
                                 pygame.Rect(x, y, self.__square_size[0], self.__square_size[1]))

        else:
            for i in range(32):
                colum = i // 4
                row = (i % 4) * 2
                if colum % 2 == 0:
                    row += 1
                x = (row * self.__square_size[0]) + self.top_left[0]
                y = (colum * self.__square_size[1]) + self.top_left[1]
                pygame.draw.rect(self.screen, self.colors[1],
                                 pygame.Rect(x, y, self.__square_size[0], self.__square_size[1]))

        # draw letters
        for i in range(8):
            row_letter = self.index_to_row(i)
            font = pygame.font.SysFont("Calibri", 30)
            text_surface = font.render(row_letter, True, "#ffffff")
            pos = \
                (
                    self.top_left[0] + (i * self.__square_size[0]),
                    self.top_left[1] + self.__size[1] + round(self.__square_size[1] * .1)
                )
            self.screen.blit(text_surface, pos)

        # draw numbers
        for i in range(8):
            font = pygame.font.SysFont("Calibri", 30)
            text_surface = font.render(str(self.invert(self.colum_to_index(i))), True, "#ffffff")
            pos = self.top_left[0] - 30, (i * self.__square_size[1]) + 30 + self.__square_size[1]
            self.screen.blit(text_surface, pos)

    @staticmethod
    def invert(i: int) -> int:
        return abs(7 - i)

    def square_to_pos(self, square_pos: tuple[int, int]) -> tuple[int, int]:
        if self.__board_inverted:
            row: int = square_pos[0]
            colum: int = square_pos[1]
            return self.top_left[0] + (self.__square_size[0] * row) - self.__square_size[0], (
                    self.top_left[1] + (self.__square_size[1] * colum)) - self.__square_size[1]
        else:
            row: int = square_pos[0]
            colum: int = self.invert(square_pos[1])
            return self.top_left[0] + (self.__square_size[0] * row), self.top_left[1] + (self.__square_size[1] * colum)

    def pos_to_square(self, pos: tuple[int, int]) -> tuple[int, int]:
        cords_on_board = (pos[0] - self.top_left[0], pos[1] - self.top_left[1])
        if self.__board_inverted:
            row = int(cords_on_board[0] // self.__square_size[0]) + 1
            colum = int(cords_on_board[1] // self.__square_size[1]) + 1
        else:
            row = int(cords_on_board[0] // self.__square_size[0]) + 1
            colum = self.invert(int(cords_on_board[1] // self.__square_size[1]))
        return row, colum

    def get_square_clicked(self) -> tuple[int, int] | None:
        clicked: bool = pygame.mouse.get_pressed()[0]
        if clicked:
            pos = pygame.mouse.get_pos()
            if self.top_left[0] < pos[0] < self.top_left[0] + self.__size[0] and self.top_left[1] < pos[1] < \
                    self.top_left[1] + self.__size[1]:
                square = self.pos_to_square(pos)
                return self.colum_to_index(square[0]), square[1]
        return None

    def mark_square(self, squares: list[tuple[int, int]]) -> None:
        if squares is None:
            return None
        for square in squares:
            pos = self.square_to_pos(square)
            pygame.draw.circle(
                self.screen,
                "#72777c",
                (pos[0] + self.__square_size[0] // 2, pos[1] + self.__square_size[1] // 2),
                10
            )

    def mark_squares(self) -> None:
        self.mark_square(list(self.squares_to_mark))


if __name__ == "__main__":
    display = pygame.display.set_mode((1_000, 1_000))
    clock = pygame.time.Clock()
    board = Board(display)
    board.__board_inverted = True
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit")
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = board.get_square_clicked()
                print(board.square_to_pos(click))

        pygame.display.set_caption(f"fps: {int(clock.get_fps())}")

        display.fill("#000000")
        board.draw_board()

        pygame.display.update()
        clock.tick()
