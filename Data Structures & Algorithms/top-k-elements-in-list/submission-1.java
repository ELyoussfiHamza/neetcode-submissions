
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        
        // Count the frequency of each element
        for (Integer x : nums) {
            hm.put(x, hm.getOrDefault(x, 0) + 1);
        }
        
        int n = nums.length;
        
        // Create an array of ArrayLists to group elements by frequency
        List<Integer>[] arr = new List[n + 1];  // Use List instead of ArrayList for better flexibility
        
        // Initialize each element in the array
        for (int i = 0; i <= n; i++) {
            arr[i] = new ArrayList<>();
        }
        
        // Fill the array of lists with numbers according to their frequencies
        for (Map.Entry<Integer, Integer> entry : hm.entrySet()) {
            int frequency = entry.getValue();
            int num = entry.getKey();
            arr[frequency].add(num);
        }
        
        int index = 0;
        int[] res = new int[k];
        
        // Collect the top k frequent elements starting from the highest frequency
        for (int i = n; i >= 0; i--) {
            if (index == k) {
                break;
            }
            List<Integer> current = arr[i];
            if (!current.isEmpty()) {
                for (Integer ele : current) {
                    if (index == k) {
                        break;
                    }
                    res[index++] = ele;
                }
            }
        }
        
        return res;
    }
}
