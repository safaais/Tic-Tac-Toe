class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, square, letter):
        row_ind = square // 3
        col_ind = square % 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        col = [self.board[col_ind + i*3] for i in range(3)]
        diag1 = [self.board[i] for i in [0, 4, 8]]
        diag2 = [self.board[i] for i in [2, 4, 6]]

        return (all(s == letter for s in row) or
                all(s == letter for s in col) or
                all(s == letter for s in diag1) or
                all(s == letter for s in diag2))

    def is_full(self):
        return ' ' not in self.board

    def get_state(self):
        return ''.join(self.board)
