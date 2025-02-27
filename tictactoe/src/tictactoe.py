import random
from cellstate import CellState

class TicTacToe:
    def __init__(self, play_against_computer, player_goes_first):
        self.board = [[CellState.EMPTY for _ in range(3)] for _ in range(3)]
        self.is_first_player_turn = True
        self.is_player_vs_computer = play_against_computer
        self.is_player_first = player_goes_first

    def make_move(self, row, col):
        if row < 0 or row >= 3 or col < 0 or col >= 3 or self.board[row][col] != CellState.EMPTY:
            return False

        self.board[row][col] = CellState.X if self.is_first_player_turn else CellState.O
        self.is_first_player_turn = not self.is_first_player_turn

        if self.is_player_vs_computer and ((self.is_player_first and not self.is_first_player_turn) or (not self.is_player_first and self.is_first_player_turn)):
            self.make_computer_move()

        return True

    def make_computer_move(self):
        if self.find_winning_move():
            return
        if self.find_blocking_move():
            return
        self.make_random_move()

    def find_winning_move(self):
        computer_symbol = CellState.O if self.is_player_first else CellState.X
        return self.find_strategic_move(computer_symbol)

    def find_blocking_move(self):
        player_symbol = CellState.X if self.is_player_first else CellState.O
        return self.find_strategic_move(player_symbol)

    def find_strategic_move(self, symbol):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == CellState.EMPTY:
                    self.board[i][j] = symbol
                    if self.check_win():
                        self.board[i][j] = CellState.X if self.is_first_player_turn else CellState.O
                        self.is_first_player_turn = not self.is_first_player_turn
                        return True
                    self.board[i][j] = CellState.EMPTY
        return False

    def make_random_move(self):
        row, col = random.randint(0, 2), random.randint(0, 2)
        while self.board[row][col] != CellState.EMPTY:
            row, col = random.randint(0, 2), random.randint(0, 2)
        self.board[row][col] = CellState.X if self.is_first_player_turn else CellState.O
        self.is_first_player_turn = not self.is_first_player_turn

    def check_win(self):
        for i in range(3):
            if self.board[i][0] != CellState.EMPTY and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
        for j in range(3):
            if self.board[0][j] != CellState.EMPTY and self.board[0][j] == self.board[1][j] == self.board[2][j]:
                return True
        if self.board[0][0] != CellState.EMPTY and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != CellState.EMPTY and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False

    def is_draw(self):
        if self.check_win():
            return False
        for row in self.board:
            if CellState.EMPTY in row:
                return False
        return True

    def get_board(self):
        return self.board

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end="")
                if j < 2:
                    print("|", end="")
            print()
            if i < 2:
                print("-+-+-")
        print()

    def is_first_player_turn(self):
        return self.is_first_player_turn

if __name__ == "__main__":
    vs_computer = input("Play against computer? (y/n)").lower().startswith("y")
    player_first = True
    if vs_computer:
        player_first = input("Do you want to go first? (y/n)").lower().startswith("y")

    game = TicTacToe(vs_computer, player_first)

    while True:
        game.print_board()

        if game.check_win():
            print(f"{'Player O' if game.is_first_player_turn else 'Player X'} wins!")
            break

        if game.is_draw():
            print("It's a draw!")
            break

        print(f"Player {'X' if game.is_first_player_turn else 'O'}'s turn")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if not game.make_move(row, col):
            print("Invalid move! Try again.")