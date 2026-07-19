class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] output = new int[n];
        // let's count the number of zeros
        int zeros_count = 0;
        int prod = 1;
        for (int x : nums){
            if (x==0){
                zeros_count++;
            }else{
                prod = prod * x;
            }
        }
        if (zeros_count>1){
            return output;
        }

        for (int i = 0;i<n;i++){
            if (zeros_count==1){
                if (nums[i]==0){
                    output[i] = prod;
                }else{
                    output[i] = 0;
                }
            }else{
                output[i]  = prod/nums[i];
            }
        }
        return output;


    }
}  
