#N Queens
def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there's a queen in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check upper right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def solve(board, row):
        if row >= n:
            solutions.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(board, row + 1)
                board[row][col] = '.'

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return solutions


n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()
