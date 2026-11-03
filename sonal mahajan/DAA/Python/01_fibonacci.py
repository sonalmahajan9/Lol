"""Practical 1: Recursive and iterative Fibonacci; time/space complexity."""

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def main():
    n = int(input("Enter number of terms: "))
    if n < 0:
        print("Please enter a non-negative number.")
        return
    recursive = [fib_recursive(i) for i in range(n)]
    iterative = fib_iterative(n)
    print("Recursive Fibonacci:", *recursive)
    print("Iterative Fibonacci:", *iterative)
    print("Recursive: exponential time approximately O(2^n), O(n) stack space.")
    print("Iterative: O(n) time for n terms, O(n) output storage; O(1) auxiliary space if not storing terms.")

if __name__ == '__main__':
    main()
