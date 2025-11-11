# Write a program to implement Huffman Encoding using a greedy strategy.
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # This is needed so heapq can compare Node objects
    def __lt__(self, other):
        return self.freq < other.freq


def huffmanencoding(char_freq):
    # Step 1: Create a min-heap (priority queue)
    heap = [Node(ch, fr) for ch, fr in char_freq.items()]
    heapq.heapify(heap)

    # Step 2: Build Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    # Step 3: Generate Huffman Codes
    root = heap[0]
    codes = {}

    def generate_code(node, code=""):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code
            return
        generate_code(node.left, code + "0")
        generate_code(node.right, code + "1")

    generate_code(root)
    return codes


if __name__ == "__main__":
    char_freq = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
    codes = huffmanencoding(char_freq)

    print("Character | Huffman Code")
    for ch, code in codes.items():
        print(f"    {ch}     |     {code}")

