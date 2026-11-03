import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class QuickSort {
    static Random random = new Random();

    static int partition(int[] a, int low, int high) {
        int pivot = a[high], i = low - 1;
        for (int j = low; j < high; j++) {
            if (a[j] <= pivot) {
                i++;
                int t = a[i]; a[i] = a[j]; a[j] = t;
            }
        }
        int t = a[i + 1]; a[i + 1] = a[high]; a[high] = t;
        return i + 1;
    }

    static void quickSort(int[] a, int low, int high, boolean randomized) {
        if (low >= high) return;
        if (randomized) {
            int p = low + random.nextInt(high - low + 1);
            int t = a[p]; a[p] = a[high]; a[high] = t;
        }
        int p = partition(a, low, high);
        quickSort(a, low, p - 1, randomized);
        quickSort(a, p + 1, high, randomized);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter integers separated by spaces: ");
        String line = sc.nextLine().trim();
        if (line.isEmpty()) { System.out.println("No numbers entered."); return; }
        String[] tokens = line.split("\\s+");
        int[] original = new int[tokens.length];
        for (int i = 0; i < tokens.length; i++) original[i] = Integer.parseInt(tokens[i]);
        int[] deterministic = original.clone(), randomized = original.clone();
        quickSort(deterministic, 0, deterministic.length - 1, false);
        quickSort(randomized, 0, randomized.length - 1, true);
        System.out.println("Deterministic: " + Arrays.toString(deterministic));
        System.out.println("Randomized:    " + Arrays.toString(randomized));
        System.out.println("Best/average O(n log n); worst O(n^2).");
    }
}
