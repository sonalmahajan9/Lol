import java.util.Scanner;

public class Fibonacci {
    static int fibRecursive(int n) {
        if (n <= 1) return n;
        return fibRecursive(n - 1) + fibRecursive(n - 2);
    }

    static long fibIterative(int n) {
        long a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            long next = a + b;
            a = b;
            b = next;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of terms (0 to 45 recommended): ");
        int n = sc.nextInt();
        if (n < 0) { System.out.println("Enter a non-negative number."); return; }
        System.out.print("Recursive: ");
        for (int i = 0; i < n; i++) System.out.print(fibRecursive(i) + " ");
        System.out.print("\nIterative: ");
        for (int i = 0; i < n; i++) System.out.print(fibIterative(i) + " ");
        System.out.println("\nRecursive time approx O(2^n), stack O(n); iterative time O(n) per sequence, O(1) auxiliary space.");
    }
}
