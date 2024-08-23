import pygame

class GUI:
    def __init__(self, screen: pygame.display, size: tuple[int, int], colors: tuple[int | str, int | str], top_left: tuple[int, int], outline_color, outline_thickness, pieces_offset):
        self.screen:pygame.display = screen
        self.size: tuple[int, int] = size
        self.colors: tuple[int | str, int | str] = colors
        self.top_left: tuple[int, int] = top_left
        self.outline_color = outline_color
        self.outline_thickness = outline_thickness
        self.pieces_offset = pieces_offset
        self.rect_size: tuple[int, int] = self.size[0] // 8, self.size[1] // 8
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


    @staticmethod
    def key_from_value(dictionary: dict, value: str | int) :
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
                self.size[0] + self.outline_thickness * 2,
                self.size[1] + self.outline_thickness * 2
            )
        )

        # color a (white)
        pygame.draw.rect(
            self.screen, self.colors[0],
            pygame.Rect(
                self.top_left[0],
                self.top_left[1],
                self.size[0], self.size[1]
            )
        )

        # color b (black)
        for i in range(32):
            colum = i // 4
            row = (i % 4) * 2
            if colum % 2 == 0:
                row += 1
            x = (row * self.size[0]) + self.top_left[0]
            y = (colum * self.size[1]) + self.top_left[1]
            pygame.draw.rect(self.screen, self.colors[1], pygame.Rect(x, y, self.size[0], self.size[1]))

            """draw letters and numbers"""
        for i in range(8):
            letters_row = self.key_from_value(self.letters, i)
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = font.render(letters_row, False, "#ffffff")
            pos = self.shelltopos(f"{letters_row}1", addy=-self.rectsize[1])
            self.screen.blit(text_surface, pos)

        for i in range(8):
            font = pygame.font.SysFont("Comic Sans MS", 30)
            text_surface = font.render(str(abs(8 - i)), False, "#ffffff")
            pos = self.shelltopos(f"a{i}", addx=-self.rectsize[0], addy=self.rectsize[1])
            screen.blit(text_surface, pos)

