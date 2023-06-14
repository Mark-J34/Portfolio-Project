# Author: Mark Jensen
# GitHub username: Mark-J34
# Date: 06/01/2023
# Description: This program is an implementation of the Othello board game with player creation and game tracking.

class Player:
    """A class representing players in the Othello game."""
    def __init__(self, name, color):
        """Initialize a Player object with a name and color."""
        self._name = name
        self._color = color

    def get_name(self):
        """Return the name of the player."""
        return self._name

    def get_color(self):
        """Return the color of the player."""
        return self._color

class Othello:
    """This class represents an Othello game with player creation and game tracking."""

    def __init__(self):
        """Initialize an Othello game with an empty board and no players."""
        self._board = self.create_board()
        self._players = []

    def create_board(self):
        """Create an Othello game board."""
        edge = '*'
        x_piece = 'X'
        o_piece = 'O'
        empty_space = '.'
        board = []
        for x in range(10):
            row = []
            for y in range(10):
                if x == 0 or x == 9 or y == 0 or y == 9:
                    row.append(edge)
                elif (x == 4 and y == 4) or (x == 5 and y == 5):
                    row.append(o_piece)
                elif (x == 4 and y == 5) or (x == 5 and y == 4):
                    row.append(x_piece)
                else:
                    row.append(empty_space)
            board.append(row)

        return board

    def print_board(self):
        """Print the current state of the game board."""
        for row in self._board:
            print(' '.join(row))

    def create_player(self, player_name, color):
        """Create a new player with the given name and color and add them to the game."""
        player = Player(player_name, color)
        self._players.append(player)

    def return_winner(self):
        """Return the winner of the game or 'It's a tie' if there is no winner."""
        white_total = 0
        black_total = 0
        for i in self._board:
            for j in i:
                if j == "X":
                    black_total += 1
                elif j == "O":
                    white_total += 1

        if white_total > black_total:
            for player in self._players:
                if player.get_color() == "white":
                    return f"Winner is white player: {player.get_name()}"
        elif black_total > white_total:
            for player in self._players:
                if player.get_color() == "black":
                    return f"Winner is black player: {player.get_name()}"
        else:
            return "It's a tie"

    def return_available_positions(self, color):
        """Return a list of available positions for the given color."""
        if color == "black":
            opponent_piece = 'O'
            players_piece = "X"
        else:
            players_piece = "O"
            opponent_piece = "X"
        available_positions = []

        for i in range(1, 9):
            for j in range(1, 9):
                if self._board[i][j] == '.':
                    if self.check_direction(i, j, players_piece, opponent_piece, 0, -1):
                        available_positions.append((i, j)),
                    if self.check_direction(i, j, players_piece, opponent_piece, 0, 1):
                        available_positions.append((i, j))
                    if self.check_direction(i, j, players_piece, opponent_piece, 1, 0):
                        available_positions.append((i, j))
                    if self.check_direction(i, j, players_piece, opponent_piece, -1, 0):
                        available_positions.append((i, j))
                    if self.check_direction(i, j, players_piece, opponent_piece, -1, -1):
                        available_positions.append((i, j))
                    if self.check_direction(i, j, players_piece, opponent_piece, -1, 1):
                        available_positions.append((i, j))
                    if self.check_direction(i, j, players_piece, opponent_piece, 1, -1):
                        available_positions.append((i, j))
                    if self.check_direction(i, j, players_piece, opponent_piece, 1, 1):
                        available_positions.append((i, j))

        return available_positions

    def check_direction(self, i, j, players_piece, opponent_piece, row_dir, col_dir):
        """Check if a valid move is possible in the given direction."""
        i += row_dir
        j += col_dir
        in_between = False
        while 0 < i < 9 and 0 < j < 9 and self._board[i][j] == opponent_piece:
            i += row_dir
            j += col_dir
            in_between = True
        if self._board[i][j] == players_piece and in_between:
            in_between = False
            return True
        else:
            return False

    def make_move(self, color, coordinate):
        """Make a move with the given color at the specified coordinate."""
        if color == "black":
            piece = "X"
            opponent_piece = "O"
        else:
            piece = "O"
            opponent_piece = "X"
        positions = self.return_available_positions(color)
        if coordinate in positions:
            self._board[coordinate[0]][coordinate[1]] = piece
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            for direction in directions:
                i, j = coordinate
                i += direction[0]
                j += direction[1]
                while 0 < i < 9 and 0 < j < 9 and self._board[i][j] == opponent_piece:
                    i += direction[0]
                    j += direction[1]
                if self._board[i][j] == piece:
                    while True:
                        i -= direction[0]
                        j -= direction[1]
                        if (i, j) == coordinate:
                            break
                        self._board[i][j] = piece

            return self._board


    def play_game(self, player_color, piece_position):
        """Play a game with the given player color and piece position."""
        if piece_position not in self.return_available_positions(player_color):
            print(f"Here are the valid moves:, {self.return_available_positions(player_color)}")
            return "Invalid move"
        else:
            self.make_move(player_color, piece_position)
            white_total = 0
            black_total = 0
            for i in self._board:
                for j in i:
                    if j == "X":
                        black_total += 1
                    elif j == "O":
                        white_total += 1
            if self.return_available_positions("white") is None and self.return_available_positions("black") is None:
                print(f"Game is ended white piece: {white_total} black piece: {black_total}")
                return self.return_winner()
