import java.util.Arrays;
import java.util.Scanner;

public class NQueens {
    static int n;
    static char[][] board;
    static boolean[] columns, diag1, diag2;

    static boolean solve(int row) {
        if (row == n) return true;
        for (int col = 0; col < n; col++) {
            int d1 = row - col + n - 1, d2 = row + col;
            if (!columns[col] && !diag1[d1] && !diag2[d2]) {
                board[row][col] = 'Q';
                columns[col] = diag1[d1] = diag2[d2] = true;
                if (solve(row + 1)) return true;
                board[row][col] = '.';
                columns[col] = diag1[d1] = diag2[d2] = false;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N: ");
        n = sc.nextInt();
        if (n < 1) { System.out.println("N must be positive."); return; }
        board = new char[n][n];
        for (char[] row : board) Arrays.fill(row, '.');
        columns = new boolean[n]; diag1 = new boolean[2 * n - 1]; diag2 = new boolean[2 * n - 1];
        if (solve(0)) {
            for (char[] row : board) System.out.println(new String(row));
        } else System.out.println("No solution exists.");
        System.out.println("Backtracking checks column and diagonal conflicts; worst-case time is approximately O(N!).");
    }
}
