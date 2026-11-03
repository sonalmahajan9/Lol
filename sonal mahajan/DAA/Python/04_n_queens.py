"""Practical 4: N-Queens using backtracking; prints one solution."""

def solve_n_queens(n):
    if n < 1:
        return None
    board = [['.'] * n for _ in range(n)]
    columns, diag1, diag2 = set(), set(), set()

    def backtrack(row):
        if row == n:
            return True
        for col in range(n):
            d1, d2 = row - col, row + col
            if col in columns or d1 in diag1 or d2 in diag2:
                continue
            board[row][col] = 'Q'
            columns.add(col); diag1.add(d1); diag2.add(d2)
            if backtrack(row + 1):
                return True
            board[row][col] = '.'
            columns.remove(col); diag1.remove(d1); diag2.remove(d2)
        return False

    return board if backtrack(0) else None


def main():
    n = int(input("Enter N: "))
    solution = solve_n_queens(n)
    if solution is None:
        print("No solution exists for this N (or N is invalid).")
    else:
        for row in solution:
            print(' '.join(row))
    print("Backtracking places one queen in each row and rejects column/diagonal conflicts.")

if __name__ == '__main__':
    main()
