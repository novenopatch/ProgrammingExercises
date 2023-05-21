public class Main {
    public static void main(String[] args) {
        int[] nbrs = {10, 15, 7};
        int nbr = 17;
        
        boolean result = hasSumPair(nbrs, nbr);
        System.out.println(result);
    }
    
    public static boolean hasSumPair(int[] nbrs, int target) {
        for (int i : nbrs) {
            int complement = target - i;
            if (complement != 0 && contains(nbrs, complement)) {
                return true;
            }
        }
        return false;
    }
    
    public static boolean contains(int[] arr, int target) {
        for (int num : arr) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }
}
