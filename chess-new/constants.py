import pygame
from board.board import Board
from  chess import Chess

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

board = Board(screen)
chess = Chess(screen)
run: bool = True

big_piece_size = board.square_size
small_piece_size = (board.square_size[0] // 2, board.square_size[1] // 2)

# loading and scaling black pieces
black_q = pygame.image.load('assets/images/black queen.png')
black_q = pygame.transform.scale(black_q, big_piece_size)
black_q_small = pygame.transform.scale(black_q, small_piece_size)

black_k = pygame.image.load('assets/images/black king.png')
black_k = pygame.transform.scale(black_k, big_piece_size)
black_k_small = pygame.transform.scale(black_k, small_piece_size)

black_r = pygame.image.load('assets/images/black rook.png')
black_r = pygame.transform.scale(black_r, big_piece_size)
black_r_small = pygame.transform.scale(black_r, small_piece_size)

black_b = pygame.image.load('assets/images/black bishop.png')
black_b = pygame.transform.scale(black_b, big_piece_size)
black_b_small = pygame.transform.scale(black_b, small_piece_size)

black_kn = pygame.image.load('assets/images/black knight.png')
black_kn = pygame.transform.scale(black_kn, big_piece_size)
black_kn_small = pygame.transform.scale(black_kn, small_piece_size)

black_p = pygame.image.load('assets/images/black pawn.png')
black_p = pygame.transform.scale(black_p, big_piece_size)
black_p_small = pygame.transform.scale(black_p, small_piece_size)


# loading and scaling white pieces
white_q = pygame.image.load('assets/images/white queen.png')
white_q = pygame.transform.scale(white_q, big_piece_size)
white_q_small = pygame.transform.scale(white_q, small_piece_size)

white_k = pygame.image.load('assets/images/white king.png')
white_k = pygame.transform.scale(white_k, big_piece_size)
white_k_small = pygame.transform.scale(white_k, small_piece_size)

white_r = pygame.image.load('assets/images/white rook.png')
white_r = pygame.transform.scale(white_r, big_piece_size)
white_r_small = pygame.transform.scale(white_r, small_piece_size)

white_b = pygame.image.load('assets/images/white bishop.png')
white_b = pygame.transform.scale(white_b, big_piece_size)
white_b_small = pygame.transform.scale(white_b, small_piece_size)

white_kn = pygame.image.load('assets/images/white knight.png')
white_kn = pygame.transform.scale(white_kn, big_piece_size)
white_kn_small = pygame.transform.scale(white_kn, small_piece_size)

white_p = pygame.image.load('assets/images/white pawn.png')
white_p = pygame.transform.scale(white_p, big_piece_size)
white_p_small = pygame.transform.scale(white_p, small_piece_size)


# creating lists of pieces images
white_images = white_r, white_kn, white_b, white_q, white_k, white_p
black_images = black_r, black_kn, black_b, black_q, black_k, black_p
white_images_small = white_r_small, white_b_small, white_kn_small, white_q_small, white_k_small, white_p_small
black_images_small = black_r_small, black_b_small, black_kn_small, black_q_small, black_k_small, black_p_small

# creating list of pieces
pieces = "r", "kn", "b", "q", "k", "p"
