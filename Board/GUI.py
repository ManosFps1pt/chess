import pygame


class GUI:
    def __init__(self, size: tuple[int, int], colors: tuple[int | str, int | str], topleft: tuple[int, int], outline, pieces_offset):
        self.size = size
