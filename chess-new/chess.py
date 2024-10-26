from typing import List, Tuple
import pygame
from enum import Enum
from dataclasses import dataclass, field
from board.board import Board
import constants as c

pygame.init()


class Type(Enum):
    ROOK: str = "r"
    KNIGHT: str = "kn"
    BISHOP: str = "b"
    KING: str = "k"
    QUEEN: str = "q"
    PAWN: str = "p"

    WHITE: str = "w"
    BLACK: str = "b"


@dataclass(order=False)
class Piece:
    color: str
    type: str
    square_pos: tuple[int, int]
    pieces_size: tuple[tuple[int, int], tuple[int, int]] = field(init=True, repr=False)
    image: pygame.surface = field(init=False, repr=False)
    image_big: pygame.surface = field(init=False, repr=False)
    image_small: pygame.surface = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.image = pygame.image.load(f"assets/images/{self.color}_{self.type}.png").convert_alpha()
        self.image_big: pygame.surface = pygame.transform.scale(self.image, self.pieces_size[0])
        self.image_small: pygame.surface = pygame.transform.scale(self.image, self.pieces_size[1])


class Chess(Board, Piece):
    def __init__(self, screen: pygame.display):
        super().__init__(screen)
        self.pieces = \
            [
                "r", "kn", "b", "q", "k", "b", "kn", "r",
                "p", "p", "p", "p", "p", "p", "p", "p"
            ]

        self.white_pieces: list[Piece] = \
            [
                Piece(
                    color="w",
                    type=i,
                    square_pos=(
                        idx % 8,
                        idx // 8
                    ),
                    pieces_size=(
                        (
                            self.square_size[0] - 5,
                            self.square_size[1] - 5
                        ),

                        (
                            self.square_size[0] // 2,
                            self.square_size[1] // 2
                        )
                    )
                ) for idx, i in enumerate(self.pieces)
            ]

        self.black_pieces: list[Piece] = \
            [
                Piece(
                    color="b",
                    type=i,
                    square_pos=(
                        idx % 8,
                        self.invert(idx // 8)
                    ),
                    pieces_size=(
                        (
                            self.square_size[0] - 5,
                            self.square_size[1] - 5
                        ),
                        (
                            self.square_size[0] // 2,
                            self.square_size[1] // 2
                        )
                    )
                ) for idx, i in enumerate(self.pieces)
            ]

        self.white_squares_reachable: set[tuple[int, int]] = set()
        self.black_squares_reachable: set[tuple[int, int]] = set()
        self.selected_piece: Piece | None = None
        self.selected_piece_reachable: set[tuple[int, int]] = set()
        self.refresh = False
        self.white_playing: bool = True
        self.king_moved: bool = False

    def get_friendly_pieces_pos(self, is_white: bool) -> list[tuple[int, int]]:
        pos_list: list[tuple[int, int]] = []
        if is_white:
            for piece in self.white_pieces:
                pos_list.append(piece.square_pos)
        else:
            for piece in self.black_pieces:
                pos_list.append(piece.square_pos)
        return pos_list

    def get_enemy_pieces_pos(self, is_white: bool) -> list[tuple[int, int]]:
        return self.get_friendly_pieces_pos(not is_white)

    def get_squares_reachable(self, is_white: bool):
        if is_white:
            return self.white_squares_reachable
        else:
            return self.black_squares_reachable

    def draw_pieces(self):
        """
        Draws all pieces on the board.
        :return: None
        """
        for idx, i in enumerate(self.white_pieces):
            self.screen.blit(
                i.image_big,
                self.square_to_pos(
                    i.square_pos
                )
            )

        for idx, i in enumerate(self.black_pieces):
            self.screen.blit(
                i.image_big,
                self.square_to_pos(
                    i.square_pos
                )
            )

    def pawn_available(self, pos: tuple[int, int], is_white: bool) -> list[tuple[int, int]] | None:
        """
        Determines the available moves for a pawn at the given position.
        If the position in invalid, the function returns None.
        :param pos: The position of the pawn.
        :param is_white: Whether the pawn is white or black.
        :return: A list of available moves for the pawn.
        """
        if pos is None:
            return None
        moves_list = []
        if is_white:
            friendly_list = self.get_friendly_pieces_pos(is_white)
            enemy_list = self.get_enemy_pieces_pos(is_white)
            if (pos[0], pos[1] + 1) not in friendly_list and (pos[0], pos[1] + 1) not in enemy_list and pos[1] <= 6:
                moves_list.append((pos[0], pos[1] + 1))
                if (
                        (pos[0], pos[1] + 2) not in friendly_list
                        and (pos[0], pos[1] + 2) not in enemy_list
                        and pos[1] == 1
                ):
                    moves_list.append(
                        (
                            pos[0],
                            pos[1] + 2
                        )
                    )
            if (pos[0] + 1, pos[1] + 1) in enemy_list:
                moves_list.append(
                    (
                        pos[0] + 1,
                        pos[1] + 1
                    )
                )
            if (pos[0] - 1, pos[1] + 1) in enemy_list:
                moves_list.append(
                    (
                        pos[0] - 1,
                        pos[1] + 1
                    )
                )
        else:
            friendly_list = self.get_friendly_pieces_pos(is_white)
            enemy_list = self.get_enemy_pieces_pos(is_white)
            if (
                    (
                            pos[0], pos[1] - 1
                    ) not in friendly_list
                    and (
                    pos[0], pos[1] - 1
            ) not in enemy_list

                    and pos[1] >= 1
            ):
                moves_list.append(
                    (
                        pos[0],
                        pos[1] - 1
                    )
                )
                if (
                        (
                                pos[0], pos[1] - 2
                        ) not in friendly_list
                        and
                        (
                                pos[0], pos[1] - 2
                        ) not in enemy_list
                        and pos[1] == 6
                ):
                    moves_list.append((pos[0], pos[1] - 2))
            if (
                    (
                            pos[0] + 1, pos[1] - 1
                    ) in enemy_list
            ):
                moves_list.append((pos[0] + 1, pos[1] - 1))
            if (
                    (
                            pos[0] - 1, pos[1] - 1
                    ) in enemy_list
            ):
                moves_list.append((pos[0] - 1, pos[1] - 1))
        return moves_list

    def bishop_available(self, pos: tuple[int, int], is_white: bool) -> list[tuple[int, int]]:
        """
        Determines the available moves for a bishop at the given position.
        If the position in invalid, the function returns None.
        :param pos: The position of the bishop.
        :param is_white: Whether the bishop is white or black.
        :return:  A list of available moves for the bishop.
        """
        moves_list: list[tuple[int, int]] = []
        friendly_list = self.get_friendly_pieces_pos(is_white)
        enemy_list = self.get_enemy_pieces_pos(is_white)
        for i in range(4):
            match i:
                case 0:
                    direction: tuple[int, int] = 1, 1
                case 1:
                    direction: tuple[int, int] = 1, -1
                case 2:
                    direction: tuple[int, int] = -1, 1
                case 3:
                    direction: tuple[int, int] = -1, -1
                case _:
                    direction: tuple[int, int] = 0, 0  # not accessible

            chain: int = 1
            path = True
            while path:
                checking_square: tuple[int, int] = (
                    pos[0] + chain * direction[0],
                    pos[1] + chain * direction[1]
                )
                if (
                        checking_square not in friendly_list
                        and 0 <= checking_square[0] <= 7
                        and 0 <= checking_square[1] <= 7
                ):
                    moves_list.append(checking_square)
                    chain += 1
                    if checking_square in enemy_list:
                        path = False
                else:
                    path = False
        return moves_list

    def rook_available(self, pos: tuple[int, int], is_white: bool) -> list[tuple[int, int]]:
        """
        Determines the available moves for a rook at the given position.
        If the position in invalid, the function returns None.
        :param pos: The position of the rook.
        :param is_white: Whether the rook is white or black.
        :return:  A list of available moves for the rook.
        """
        moves_list: list[tuple[int, int]] = []
        friendly_list = self.get_friendly_pieces_pos(is_white)
        enemy_list = self.get_enemy_pieces_pos(is_white)
        for i in range(4):
            match i:
                case 0:
                    direction: tuple[int, int] = 0, -1
                case 1:
                    direction: tuple[int, int] = -1, 0
                case 2:
                    direction: tuple[int, int] = 0, 1
                case 3:
                    direction: tuple[int, int] = 1, 0
                case _:
                    direction: tuple[int, int] = 0, 0  # not accessible

            chain: int = 1
            path = True
            while path:
                checking_square: tuple[int, int] = pos[0] + (chain * direction[0]), pos[1] + (chain * direction[1])
                if (
                        checking_square not in friendly_list and
                        0 <= checking_square[0] <= 7
                        and 0 <= checking_square[1] <= 7
                ):
                    moves_list.append(checking_square)
                    chain += 1
                    if checking_square in enemy_list:
                        path = False
                else:
                    path = False
        return moves_list

    def queen_available(self, pos: tuple[int, int], is_white: bool):
        """
        Determines the available moves for a queen at the given position.
        If the position in invalid, the function returns None.
        :param pos: The position of the queen.
        :param is_white: Whether the queen is white or black.
        :return:  A list of available moves for the rook.
        """
        moves_list = [*self.rook_available(pos, is_white), *self.bishop_available(pos, is_white)]
        return moves_list

    def knight_available(self, pos: tuple[int, int], is_white: bool) -> list[tuple[int, int]]:
        """
        Determines the available moves for a knight at the given position.
        If the position in invalid, the function returns None.
        :param pos: The position of the knight.
        :param is_white: Whether the knight is white or black.
        :return:  A list of available moves for the knight.
        """

        moves_list: list[tuple[int, int]] = []
        moves: tuple = (
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1)
        )
        friendly_list = self.get_friendly_pieces_pos(is_white)

        for i in moves:
            pos_to_check = pos[0] + i[0], pos[1] + i[1]
            if 0 <= pos_to_check[0] <= 7 and 0 <= pos_to_check[1] <= 7 and pos_to_check not in friendly_list:
                moves_list.append(pos_to_check)

        return moves_list

    def king_available(self, pos: tuple[int, int], is_white: bool) -> list[tuple[int, int]]:
        """
        Determines the available moves for a king at the given position.
        If the position in invalid, the function returns None.
        :param pos: The position of the king.
        :param is_white: Whether the king is white or black.
        :return:  A list of available moves for the king.
        """

        moves_list: list[tuple[int, int]] = []
        moves: tuple = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        )
        unreachable_squares = self.get_squares_reachable(not is_white)

        friendly_list = self.get_friendly_pieces_pos(is_white)

        for i in moves:
            pos_to_check = pos[0] + i[0], pos[1] + i[1]
            if (
                    0 <= pos_to_check[0] <= 7
                    and 0 <= pos_to_check[1] <= 7
                    and pos_to_check not in friendly_list
                    and pos_to_check not in unreachable_squares
            ):
                moves_list.append(pos_to_check)

        return moves_list

    def valid_moves(self, piece: Piece) -> list[tuple[int, int]]:
        """
        Returns the valid moves for a given piece.
        """
        if piece.color == "w":
            is_white = True
        else:
            is_white = False

        match piece.type:
            case "p":
                return self.pawn_available(piece.square_pos, is_white)
            case "r":
                return self.rook_available(piece.square_pos, is_white)
            case "b":
                return self.bishop_available(piece.square_pos, is_white)
            case "q":
                return self.queen_available(piece.square_pos, is_white)
            case "k":
                return self.king_available(piece.square_pos, is_white)
            case "kn":
                return self.knight_available(piece.square_pos, is_white)
            case _:
                pass

    def move_piece(self, selected_piece: Piece, pos: tuple[int, int]) -> None:
        if selected_piece is None:
            return None
        if selected_piece.color == "b" and self.white_playing:
            return None
        elif selected_piece.color == "w" and not self.white_playing:
            return None
        piece_id = selected_piece.square_pos
        color = selected_piece.color
        piece: Piece | None = None
        for i in self.white_pieces:
            if piece is not None:
                break
            if i.square_pos == piece_id:
                piece = i

        for i in self.black_pieces:
            if piece is not None:
                break
            if i.square_pos == piece_id:
                piece = i

        if piece is None:
            return None

        if pos not in self.valid_moves(piece):
            return None

        if color == "w":
            for i in self.black_pieces:
                if i.square_pos == pos:
                    self.black_pieces.remove(i)
                    break
        else:
            for i in self.white_pieces:
                if i.square_pos == pos:
                    self.white_pieces.remove(i)
                    break

        piece.square_pos = pos
        self.white_playing ^= True

    def manage_click(self) -> None:
        """
        Handles the mouse click event to determine the clicked square and updates the game state accordingly.
        """
        mouse_clicked: bool = pygame.mouse.get_pressed()[0]
        new_click = pygame.mouse.get_just_pressed()[0]
        if not new_click:
            return None
        square_clicked = self.get_square_clicked()
        print(square_clicked)
        if square_clicked is None:
            self.selected_piece = None
            return None

        piece: Piece | None = None
        for idx, i in enumerate(self.white_pieces):
            if i.square_pos == square_clicked:
                piece = i

        for idx, i in enumerate(self.black_pieces):
            if i.square_pos == square_clicked:
                piece = i

        # if piece is None:
        #     return None
        if self.selected_piece is None:
            self.selected_piece = piece
            return None
        if square_clicked in self.valid_moves(self.selected_piece):
            self.move_piece(self.selected_piece, square_clicked)
            self.selected_piece = None
        else:
            self.selected_piece = None

        return None
        # if piece.color == "b":
        #     is_white: bool = False
        # else:
        #     is_white: bool = True

        # return self.valid_moves(piece)

    def playing(self):
        """
        The main game loop.
        """
        self.manage_click()
        # if click is None:
        #     return None
        if self.selected_piece is None:
            return None
        self.clear_marked_squares()
        self.mark_square(self.valid_moves(self.selected_piece))


def main():
    clock = pygame.time.Clock()
    run: bool = True
    chess = Chess(c.screen)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                square_clicked = chess.get_square_clicked()
            if event.type == pygame.KEYDOWN:
                print("keydown")
                if event.key == pygame.K_SPACE:
                    chess.flip_board()
        pygame.display.set_caption(f"fps: {int(clock.get_fps())}, {chess.selected_piece}, {chess.white_playing=}")

        c.screen.fill("#ff625f")
        chess.draw_board()
        chess.draw_pieces()
        chess.draw_letters()
        # chess.add_squares_to_mark(chess.manage_click())
        # chess.mark_squares()
        chess.playing()
        pygame.display.update()
        clock.tick()


if __name__ == '__main__':
    main()
