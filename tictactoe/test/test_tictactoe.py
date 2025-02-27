import unittest
from src.tictactoe import TicTacToe, CellState


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe(False, True)

    def test_make_move_valid(self):
        self.assertTrue(self.game.make_move(0, 0))
        self.assertEqual(self.game.board[0][0], CellState.X)

    def test_make_move_invalid(self):
        self.game.board[0][0] = CellState.X
        self.assertFalse(self.game.make_move(0, 0))

    def test_make_random_move(self):
        self.game.make_random_move()
        empty_cells = sum(row.count(CellState.EMPTY) for row in self.game.board)
        self.assertEqual(empty_cells, 8)

    def test_check_win(self):
        self.game.board = [
            [CellState.X, CellState.X, CellState.X],
            [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY],
            [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
        ]
        self.assertTrue(self.game.check_win())

    def test_is_draw(self):
        self.game.board = [
            [CellState.X, CellState.O, CellState.X],
            [CellState.X, CellState.X, CellState.O],
            [CellState.O, CellState.X, CellState.O]
        ]
        self.assertTrue(self.game.is_draw())

    def test_get_board(self):
        self.assertEqual(self.game.get_board(), self.game.board)

    def test_print_board(self):
        self.game.board = [
            [CellState.X, CellState.O, CellState.X],
            [CellState.X, CellState.X, CellState.O],
            [CellState.O, CellState.X, CellState.O]
        ]
        self.game.print_board()

    def test_is_first_player_turn(self):
        self.assertTrue(self.game.is_first_player_turn)

if __name__ == '__main__':
    unittest.main()