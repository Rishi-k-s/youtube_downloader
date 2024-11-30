import java.util.Scanner;

public class QuickSort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input array size
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();
        
        // Input array elements
        int[] array = new int[n];
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            array[i] = scanner.nextInt();
        }
        
        // Perform Quick Sort
        quickSort(array, 0, n - 1);
        
        // Output sorted array
        System.out.println("Sorted array:");
        for (int num : array) {
            System.out.print(num + " ");
        }
    }

    private static void quickSort(int[] array, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(array, low, high);
            quickSort(array, low, pivotIndex - 1);  // Sort left of pivot
            quickSort(array, pivotIndex + 1, high); // Sort right of pivot
        }
    }

    private static int partition(int[] array, int low, int high) {
        int pivot = array[low]; // First element as pivot
        int i = low + 1;
        int j = high;

        while (i <= j) {
            while (i <= high && array[i] <= pivot) {
                i++;
            }
            while (j >= low && array[j] > pivot) {
                j--;
            }
            if (i < j) {
                swap(array, i, j);
            }
        }

        // Swap pivot with element at j
        swap(array, low, j);
        return j; // Pivot's final position
    }

    private static void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
