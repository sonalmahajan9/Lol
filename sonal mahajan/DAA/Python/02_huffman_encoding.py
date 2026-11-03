"""Practical 2: Huffman Encoding using a greedy strategy."""
import heapq
from collections import Counter


def huffman_codes(text):
    if not text:
        return {}
    frequencies = Counter(text)
    heap = [[freq, [[char, ""]]] for char, freq in frequencies.items()]
    heapq.heapify(heap)
    if len(heap) == 1:
        return {heap[0][1][0][0]: "0"}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for item in left[1]:
            item[1] = "0" + item[1]
        for item in right[1]:
            item[1] = "1" + item[1]
        heapq.heappush(heap, [left[0] + right[0], left[1] + right[1]])

    return {char: code for char, code in heap[0][1]}


def main():
    text = input("Enter text: ")
    codes = huffman_codes(text)
    if not codes:
        print("No text entered.")
        return
    print("Huffman codes:")
    for char, code in sorted(codes.items()):
        print(repr(char), ":", code)
    print("Encoded text:", "".join(codes[char] for char in text))
    print("Time complexity with a priority queue: O(k log k), k = distinct characters.")

if __name__ == '__main__':
    main()
