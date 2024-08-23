import os
import pygame
from chess.global_chess_class import GlobalChess

pygame.init()
pygame.init()
pygame.font.init()

directory = f"{os.getcwd()}\\chess_GUI\\pieces"
screen = pygame.display.set_mode((800, 800))


def keyFromValue(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]


class ChessLogic(GlobalChess):
    def availablePos(self, shellPiece) -> tuple:
        # H1
        colum = abs(int(shellPiece[1]) - 8)  # |1 - 8| = 7
        row = self.letters[shellPiece[0]]  # 7
        # print(f"row: {row}, colum: {colum}")
        piece = self.piecespos[colum][row][1]
        color = self.piecespos[colum][row][0]
        returning = []
        print(piece, color)
        if piece == 0:
            raise ValueError("not a piece")

        def vertical_horizontal(self, pieceShell):
            print("---------| up |----------------------------------------------------------------")
            i = [row, colum]
            o = 0
            print(self.piecespos[i[1]][i[0]][0], color)
            brk = False
            while i[1] > 0:
                if brk:
                    break
                o += 1
                i[1] -= 1
                checking = abs(i[1] - 8)
                # print("appending")
                if self.piecespos[i[1]][i[0]] != 0 and self.piecespos[i[1]][i[0]][0] == color:
                    break
                elif self.piecespos[i[1]][i[0]] != 0 and self.piecespos[i[1]][i[0]][0] != color:
                    brk = True
                returning.append(f"{keyFromValue(self.letters, i[0])}{checking}")
                print(f"color: {color}, piece: {self.piecespos[i[1]][i[0]]}")

            print("---------| down |----------------------------------------------------------------")
            i = [row, colum]
            brk = False
            while i[1] < 7:
                if brk:
                    break
                i[1] += 1
                print(self.piecespos[i[1]][i[0]])
                if self.piecespos[i[1]][i[0]] != 0 and self.piecespos[i[1]][i[0]][0] == color:
                    print("break", checking)
                    break
                elif self.piecespos[i[1]][i[0]] != 0 and self.piecespos[i[1]][i[0]][0] != color:
                    brk = True
                checking = abs(i[1] - 8)
                returning.append(f"{keyFromValue(self.letters, i[0])}{checking}")

            print("---------------| left |----------------------------------------------------------------")
            i = [row, colum]
            print("row {}, colum {}".format(row, colum))
            brk = False
            while i[0] > 0:
                if brk:
                    break
                i[0] -= 1
                print(f"i: {i[0]}, {i[1]}")
                print("self.piecepos[i[1]][i[0]]", self.piecespos[i[1]][i[0]])
                if self.piecespos[i[1]][i[0]] != 0 and self.piecespos[i[1]][i[0]][0] == color:
                    print("break", checking)
                    break
                elif self.piecespos[i[1]][i[0]] != 0 and self.piecespos[i[1]][i[0]][0] != color:
                    brk = True
                checking = i[0]  # abs(i[0] - 8)
                print(f"{keyFromValue(self.letters, i[0])}{checking}")
                returning.append(f"{keyFromValue(self.letters, i[0])}{checking}")

            print("-------------------| result |----------------------------------------------------------------")
            return returning

        if piece == "r":
            return vertical_horizontal(self, shellPiece)


"""---------| test and how it works |--------------------------------------------------------------------------------"""
if __name__ == "__main__":
    board = GlobalChess((500, 500), ("#cccccc", "#333333"), (100, 100), {"color": "#0000aa", "thickness": 10}, 5, directory)
    board.pieces_setup()
    print(board.availablepos("H1"))
    run = True
    while run:
        pygame.display.update()
        screen.fill("#666666")
        board.draw_board()
        board.draw_pieces()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
