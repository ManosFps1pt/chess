import os


def keyfromvalue(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]


class GlobalChess:
    def __init__(self, size, colors, topleft, outline, pieces_offset):
        print(f"object created: {self.__class__.__name__}")
        self.path = os.getcwd()
        self.boardsize = size
        self.colors = colors
        self.boardtopleft = topleft
        self.outline = outline
        self.rectsize = self.boardsize[0] // 8, self.boardsize[1] // 8
        self.piecessize = []
        self.offset = pieces_offset
        self.refresh = True

        self.pieces = {}
        self.letters = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7
        }

        self.lettersboard = []
        self.piecespos = [["br", "bh", "bb", "bq", "bk", "bb", "bh", "br"],
                          ["bp" for _ in range(8)],
                          [0 for _ in range(8)],
                          [0 for _ in range(8)],
                          [0, 0, 0, "br", 0, 0, 0],
                          [0 for _ in range(8)],
                          ["wp" for _ in range(8)],
                          ["wr", "wh", "wb", "wq", "wk", "wb", "wh", "wr"],
                          ]

    def shelltopos(self, shell, **kwargs) -> tuple:
        row = self.letters[shell[0].capitalize()]
        colum = int(shell[1])
        x = self.boardtopleft[0] + row * self.rectsize[0] + self.offset + kwargs.get("addx", 0)
        y = self.boardtopleft[1] + (colum - 1) * self.rectsize[1] + self.offset + kwargs.get("addy", 0)
        return x, y

    def __str__(self):
        return f"{self.path}"

    def __repr__(self):
        return self.__class__.__name__


if __name__ == "__main__":
    print("directory", os.getcwd(), sep=": ")
