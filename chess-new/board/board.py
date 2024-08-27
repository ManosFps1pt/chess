import pygame

pygame.init()


class Board:
    def __init__(self, screen: pygame.display):
        self.screen: pygame.display = screen
        self.__size: tuple[int, int] = 600, 600
        self.colors: tuple[int | str, int | str] = "#aaaaaa", "#000000"
        self.top_left: tuple[int, int] = 100, 100
        self.outline_color = "#002200"
        self.outline_thickness = 5

        self.__square_size: tuple[int, int] = self.__size[0] // 8, self.__size[1] // 8
        self.index_row_dict: dict = {
            0: "A",
            1: "B",
            2: "C",
            3: "D",
            4: "E",
            5: "F",
            6: "G",
            7: "H"
        }

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: tuple[int, int]):
        self.__size = value
        self.__square_size = self.__size[0] // 8, self.__size[1] // 8

    @property
    def square_size(self):
        return self.__square_size

    @staticmethod
    def key_from_value(dictionary: dict, value: str | int):
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
        for i in range(32):
            colum = i // 4
            row = (i % 4) * 2
            if colum % 2 == 0:
                row += 1
            x = (row * self.__square_size[0]) + self.top_left[0]
            y = (colum * self.__square_size[1]) + self.top_left[1]
            pygame.draw.rect(self.screen, self.colors[1],
                             pygame.Rect(x, y, self.__square_size[0], self.__square_size[1]))

        # draw letters and numbers
        for i in range(8):
            row_letter = self.index_to_row(i)
            font = pygame.font.SysFont("Calibri", 30)
            text_surface = font.render(row_letter, True, "#ffffff")
            pos = self.top_left[0] + (i * self.__square_size[0]), self.top_left[1] + self.__size[1] + round(
                self.__square_size[1] * .1)
            self.screen.blit(text_surface, pos)

        for i in range(8):
            font = pygame.font.SysFont("Calibri", 30)
            text_surface = font.render(str(self.invert(i)), True, "#ffffff")
            pos = self.top_left[0] - 30, (self.invert(i) * self.__square_size[1]) + 30
            self.screen.blit(text_surface, pos)

    @staticmethod
    def invert(i: int):
        return abs(8 - i)

    def square_to_pos(self, square_pos: tuple[int, int]):
        row: int = square_pos[0]
        colum: int = square_pos[1]
        return self.top_left[0] + (self.__square_size[0] * row), self.top_left[1] + (self.__square_size[1] * colum)

    def pos_to_square(self, pos: tuple[int, int]) -> tuple[int, int]:
        coords_on_board = (pos[0] - self.top_left[0], pos[1] - self.top_left[1])
        row = int(coords_on_board[0] // self.__square_size[0]) + 1
        colum = int(coords_on_board[1] // self.__square_size[1]) + 1
        return row, colum

    def get_square_clicked(self) -> tuple[tuple[int, int], tuple[int, int]] | None:
        clicked: bool = pygame.mouse.get_pressed()[0]
        if clicked:
            pos = pygame.mouse.get_pos()
            if self.top_left[0] < pos[0] < self.top_left[0] + self.__size[0] and self.top_left[1] < pos[1] < \
                    self.top_left[1] + self.__size[1]:
                square = self.pos_to_square(pos)
                return (square[0] - 1, square[1] - 1), pos
            else:
                return None
        else:
            return None


if __name__ == "__main__":
    display = pygame.display.set_mode((1_000, 1_000))
    clock = pygame.time.Clock()
    gui = Board(display)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit")
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(gui.get_square_clicked())

        pygame.display.set_caption(f"fps: {int(clock.get_fps())}")

        display.fill("#000000")
        gui.draw_board()

        pygame.display.update()
        clock.tick()
