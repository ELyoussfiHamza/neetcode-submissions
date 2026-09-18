class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();
        set<int> s;

        for (int i = 0; i < n; i++){
            if (s.contains(nums[i])){
                return true;
            }
            s.insert(nums[i]);
        }

        return false;
    }
};