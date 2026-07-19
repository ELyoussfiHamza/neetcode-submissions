class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        // <otherValue,index>
        HashMap<Integer,Integer> seen = new  HashMap<>();
        for (int i = 0;i<n;i++){
            int OtherValue = target - nums[i];
            int index = seen.getOrDefault(OtherValue,-1);
            if (index!=-1){
                return new int[]{index,i};
            }
            seen.put(nums[i],i);
        }
        return new int[]{0,0};
    }
}
