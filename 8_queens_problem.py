def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_8_queens_util(board, col):
    if col >= 8:
        return True
    for row in range(8):
        if is_safe(board, row, col):
            board[col] = row
            if solve_8_queens_util(board, col + 1):
                return True
            board[col] = -1
    return False

def solve_8_queens():
    board = [-1] * 8
    if not solve_8_queens_util(board, 0):
        print("Solution does not exist")
    print_board(board)


def print_board(board):
    for i in range(8):
        for j in range(8):
            if board[j] == i:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

solve_8_queens()
