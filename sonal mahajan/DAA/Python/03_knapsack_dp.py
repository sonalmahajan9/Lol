"""Practical 3: 0/1 Knapsack using dynamic programming."""

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
    return dp[n][capacity]


def main():
    n = int(input("Number of items: "))
    weights = list(map(int, input("Enter weights separated by spaces: ").split()))
    values = list(map(int, input("Enter values separated by spaces: ").split()))
    capacity = int(input("Enter capacity: "))
    if n <= 0 or len(weights) != n or len(values) != n or capacity < 0:
        print("Invalid input. Make sure weights and values each contain n numbers.")
        return
    if any(w < 0 for w in weights):
        print("Weights must be non-negative.")
        return
    print("Maximum value:", knapsack(weights, values, capacity))
    print("Time: O(nW); space: O(nW), where W is the capacity.")

if __name__ == '__main__':
    main()
