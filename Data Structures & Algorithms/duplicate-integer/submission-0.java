class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer , Boolean> showedUp =new HashMap<>();
        for (int x : nums){
            if (showedUp.getOrDefault(x,false)){
                return true;
            }
            showedUp.put(x,true);
        }
        return false;
    }
}
