import java.util.*;

public class HuffmanEncoding {
    static class Node {
        char ch;
        int freq;
        Node left, right;
        Node(char ch, int freq) { this.ch = ch; this.freq = freq; }
        Node(Node left, Node right) {
            this.ch = '\0'; this.freq = left.freq + right.freq;
            this.left = left; this.right = right;
        }
        boolean isLeaf() { return left == null && right == null; }
    }

    static void printCodes(Node root, String code) {
        if (root == null) return;
        if (root.isLeaf()) {
            System.out.println("'" + root.ch + "' : " + (code.isEmpty() ? "0" : code));
            return;
        }
        printCodes(root.left, code + "0");
        printCodes(root.right, code + "1");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter text: ");
        String text = sc.nextLine();
        if (text.isEmpty()) { System.out.println("No text entered."); return; }
        Map<Character, Integer> frequencies = new HashMap<>();
        for (char ch : text.toCharArray()) frequencies.put(ch, frequencies.getOrDefault(ch, 0) + 1);
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.freq));
        for (Map.Entry<Character, Integer> entry : frequencies.entrySet())
            pq.add(new Node(entry.getKey(), entry.getValue()));
        while (pq.size() > 1) pq.add(new Node(pq.poll(), pq.poll()));
        Map<Character, String> codes = new HashMap<>();
        buildMap(pq.peek(), "", codes);
        System.out.println("Huffman codes:");
        for (Map.Entry<Character, String> e : codes.entrySet())
            System.out.println("'" + e.getKey() + "' : " + e.getValue());
        StringBuilder encoded = new StringBuilder();
        for (char ch : text.toCharArray()) encoded.append(codes.get(ch));
        System.out.println("Encoded text: " + encoded);
        System.out.println("Time complexity: O(k log k), where k is the number of distinct characters.");
    }

    static void buildMap(Node node, String code, Map<Character, String> codes) {
        if (node.isLeaf()) { codes.put(node.ch, code.isEmpty() ? "0" : code); return; }
        buildMap(node.left, code + "0", codes);
        buildMap(node.right, code + "1", codes);
    }
}
