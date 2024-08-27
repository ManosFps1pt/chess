import pygame
from board.board import Board

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

board = Board(screen)
run: bool = True

big_piece_size = board.square_size
small_piece_size = (board.square_size[0] // 2, board.square_size[1] // 2)

black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, big_piece_size)
black_queen_small = pygame.transform.scale(black_queen, small_piece_size)

black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, big_piece_size)
black_king_small = pygame.transform.scale(black_king, small_piece_size)

black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, big_piece_size)
black_rook_small = pygame.transform.scale(black_rook, small_piece_size)

black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, big_piece_size)
black_bishop_small = pygame.transform.scale(black_bishop, small_piece_size)

black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, big_piece_size)
black_knight_small = pygame.transform.scale(black_knight, small_piece_size)

black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, big_piece_size)
black_pawn_small = pygame.transform.scale(black_pawn, small_piece_size)

white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, big_piece_size)
white_queen_small = pygame.transform.scale(white_queen, small_piece_size)

white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, big_piece_size)
white_king_small = pygame.transform.scale(white_king, small_piece_size)

white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, big_piece_size)
white_rook_small = pygame.transform.scale(white_rook, small_piece_size)

white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, big_piece_size)
white_bishop_small = pygame.transform.scale(white_bishop, small_piece_size)

white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, big_piece_size)
white_knight_small = pygame.transform.scale(white_knight, small_piece_size)

white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, big_piece_size)
white_pawn_small = pygame.transform.scale(white_pawn, small_piece_size)
