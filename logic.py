class ConnectFourGame:
    def __init__(self):
        # Initialize a 6x7 board with empty spaces and set the starting player to "X"
        self.rows = 6
        self.cols = 7
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = "X"

    def make_move(self, column):
        # Attempt to place a piece in the specified column and switch players
        for row in reversed(range(self.rows)):  # Start from bottom and go up
            if self.board[row][column] == " ":
                self.board[row][column] = self.current_player
                player = self.current_player
                self.switch_player()
                return row, player

        raise ValueError("This column is full.")

    def switch_player(self):
        # Switch the current player from "X" to "O" or "O" to "X"
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        # Check all directions for 4 in a row
        symbol = self.board[row][col]

        # Check horizontal (left and right)
        if self.count_in_direction(row, col, 0, 1, symbol) + self.count_in_direction(row, col, 0, -1, symbol) - 1 >= 4:
            return True

        # Check vertical (up and down)
        if self.count_in_direction(row, col, 1, 0, symbol) + self.count_in_direction(row, col, -1, 0, symbol) - 1 >= 4:
            return True

        # Check diagonal (top-left to bottom-right)
        if self.count_in_direction(row, col, 1, 1, symbol) + self.count_in_direction(row, col, -1, -1, symbol) - 1 >= 4:
            return True

        # Check diagonal (bottom-left to top-right)
        if self.count_in_direction(row, col, 1, -1, symbol) + self.count_in_direction(row, col, -1, 1, symbol) - 1 >= 4:
            return True

        return False

    def count_in_direction(self, row, col, row_step, col_step, symbol):
        # Count how many of the same symbol are connected in one direction
        count = 0
        while 0 <= row < self.rows and 0 <= col < self.cols and self.board[row][col] == symbol:
            count += 1
            row += row_step
            col += col_step
        return count

    def is_draw(self):
        # Return True if the board is full and there is no winner
        return all(self.board[0][col] != " " for col in range(self.cols))
