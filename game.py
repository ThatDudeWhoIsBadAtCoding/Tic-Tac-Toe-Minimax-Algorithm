print("Welcome to TicTac Toe!")


class Game:
    def __init__(self, symbol_1: str, symbol_2: str) -> None:
        self.board: dict = {str(i): ' ' for i in range(1, 10)}
        assert len(symbol_1) == len(symbol_2) == 1
        self.player1: str = symbol_1
        self.player2: str = symbol_2

    def print_board(self) -> None:
        print("---------")
        for i in range(1, 10):
            print(f'{self.board[str(i)]}', end="")
            if i % 3 == 0:
                print()
                print("---------")
            else:
                print(" | ", end="")

    def play_turn(self, move: int, player: int):
        if self.board[str(move)] != " ":
            # print(self.board[str(move)], move)
            # self.print_board()
            raise ValueError("Square is already occupied")
        self.board[str(move)] = self.player1 if player else self.player2

    def undo_move(self, move: int) -> None:
        # board = self.board
        self.board[str(move)] = " "
        #  board != self.board

    def check_winner(self, player: int) -> int:
        # checking rows
        for i in [1, 4, 7]:
            if self.board[str(i)] == self.board[str(i + 1)] == self.board[str(i + 2)] and self.board[str(i)] != " ":
                return 1 if player else -1

        # checking columns
        for i in [1, 2, 3]:
            if self.board[str(i)] == self.board[str(i + 3)] == self.board[str(i + 6)] and self.board[str(i)] != " ":
                return 1 if player else -1

        # checking diagonals
        if self.board["1"] == self.board["5"] == self.board["9"] != " " or self.board["3"] == self.board["5"] == self.board["7"] != " ":
            return 1 if player else -1
        # checking for a draw
        if list(self.board.values()).count(" ") == 0:
            return 0
        return 69
