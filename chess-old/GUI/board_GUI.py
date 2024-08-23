import pygame
import os
import sys
sys.path.append(os.getcwd())
from global_chess_class import Global_chess, keyfromvalue
pygame.init()
pygame.init()
pygame.font.init()

directory = f"{os.getcwd()}\\chess_GUI\\pieces"
screen = pygame.display.set_mode((800, 800))

#def keyfromvalue(dictionary, value):
#    return list(dictionary.keys())[list(dictionary.values()).index(value)]
print(Global_chess, type(Global_chess))
class Board(Global_chess):
    def pieces_setup(self) -> None:
        for file in os.scandir(self.path):
            if file.name.endswith("png"):
                image = pygame.image.load(f"{self.path}\\{file.name}")#.convert_alpha()
                #image = pygame.transform.scale(image, board.rectsize)
                #rect = pygame.Rect(image)
                width = image.get_width()
                height = image.get_height()
                rect_size_x = self.rectsize[0] - (2 * self.offset)
                rect_size_y = self.rectsize[1] - (2 * self.offset)
                if width > height:
                    scale_mult = rect_size_x / width
                    image = pygame.transform.scale(image, (self.rectsize[0] - 2 * self.offset, height * scale_mult))
                elif width <= height:
                    scale_mult = rect_size_y / height
                    image = pygame.transform.scale(image, (width * scale_mult, self.rectsize[1] - 2 * self.offset))

                self.pieces[file.name] = image
        print(self.pieces)


    def draw_board(self) -> None:
        """Draw the board"""
        # outline
        pygame.draw.rect(screen, self.outline["color"], pygame.Rect(self.boardtopleft[0] - self.outline["thickness"], self.boardtopleft[1] - self.outline["thickness"], self.boardsize[0] + self.outline["thickness"] * 2, self.boardsize[1] + self.outline["thickness"] * 2))
        
        # color a (white)
        pygame.draw.rect(screen, self.colors[0], pygame.Rect(self.boardtopleft[0], self.boardtopleft[1], self.boardsize[0], self.boardsize[1]))
        
        #color b (black)
        for i in range(32):
            colum = i // 4
            row = (i % 4) * 2
            if colum % 2 == 0:
                row += 1
            x = (row * self.rectsize[0]) + self.boardtopleft[0]
            y = (colum * self.rectsize[1]) + self.boardtopleft[1]
            pygame.draw.rect(screen, self.colors[1], pygame.Rect(x, y, self.rectsize[0], self.rectsize[1]))

            """draw letters and numbers"""
        for i in range(8):
            letters_row = keyfromvalue(self.letters, i)
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = font.render(letters_row, False, "#ffffff")
            pos = self.shelltopos(f"{letters_row}1", addy=-self.rectsize[1])
            screen.blit(text_surface, pos)

        for i in range(8):
            font = pygame.font.SysFont("Comic Sans MS", 30)
            text_surface = font.render(str(abs(8 - i)), False, "#ffffff")
            pos = self.shelltopos(f"a{i}", addx=-self.rectsize[0], addy=self.rectsize[1])
            screen.blit(text_surface, pos)
    

    

    def draw_pieces(self):
        for i in range(8):
            for idx, j in enumerate(self.piecespos[i]):
                if j != 0:
                    image = pygame.image.load(f"{directory}\\{j}.png").convert_alpha()
                    pos = self.shelltopos(f"{self.keyfromvalue(self.letters, idx)}{i + 1}")
                    screen.blit(self.pieces[f"{j}.png"], pos)
        
                
        


"""---------| test and how it works |----------------------------------------------------------------------------------"""
if __name__ == "__main__":
    board = Board((500, 500), ("#cccccc", "#333333"), (100, 100), {"color": "#0000aa", "thickness": 10}, 5)
    board.pieces_setup()
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