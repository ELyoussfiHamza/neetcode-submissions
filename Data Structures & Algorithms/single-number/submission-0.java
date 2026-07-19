class Solution {
    public int singleNumber(int[] nums) {
        // x ^ 0 = x , x ^ x = 0 
        int res = 0;
        for (int x : nums){
            res = res ^ x;
        }
        return res;
    }
}
