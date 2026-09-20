class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        int n = nums.size();
        if (n == 1){

        }
        sort(nums.begin() , nums.end());

        int l = 0;
        int r = nums.back() - nums[0];
        int res = r;
        while (l<=r){
            int mid = (l + (r -l)/2);
            if (this->isValid(nums , mid , p ,n )){
                r = mid-1;
                res = mid;
            }else{
                l = mid + 1;
            }
        }
        
        return res;
        
    }

    bool isValid(const vector<int>& nums , int threeshold , int p , int size){
        
        int i = 0;
        int j = 1;

        while (j < size){
            if (abs(nums[i] - nums[j]) <= threeshold){
                p-=1;
                i+=2;
                j+=2;
            }else{
                i++;
                j++;
            }

            if (p == 0){
                return true;
            }
            
        }
        return false;

    }
};