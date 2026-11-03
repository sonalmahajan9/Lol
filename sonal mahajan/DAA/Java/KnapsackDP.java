import java.util.Scanner;

public class KnapsackDP {
    static int knapsack(int[] wt, int[] val, int capacity) {
        int n = wt.length;
        int[][] dp = new int[n + 1][capacity + 1];
        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                dp[i][w] = dp[i - 1][w];
                if (wt[i - 1] <= w)
                    dp[i][w] = Math.max(dp[i][w], val[i - 1] + dp[i - 1][w - wt[i - 1]]);
            }
        }
        return dp[n][capacity];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Number of items: ");
        int n = sc.nextInt();
        if (n <= 0) { System.out.println("Number of items must be positive."); return; }
        int[] wt = new int[n], val = new int[n];
        System.out.println("Enter " + n + " weights:");
        for (int i = 0; i < n; i++) wt[i] = sc.nextInt();
        System.out.println("Enter " + n + " values:");
        for (int i = 0; i < n; i++) val[i] = sc.nextInt();
        System.out.print("Capacity: ");
        int capacity = sc.nextInt();
        if (capacity < 0) { System.out.println("Capacity cannot be negative."); return; }
        System.out.println("Maximum value: " + knapsack(wt, val, capacity));
        System.out.println("Time and space: O(nW), where W is the capacity.");
    }
}
