class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector <vector<int>> ans;
        vector<int> top = {1};
        ans.push_back(top);
        if (numRows == 1){
            return ans;
        }
        
        for (int i=0 ; i < numRows-1 ; i++){
            int left = -1;
            int right = 0;
            vector<int> prev = ans.back();
            int prev_size = prev.size();
            vector<int> row;
            while (left <= prev_size){
                if (left == -1){
                    row.push_back(1);
                }else if (right == prev_size){
                    row.push_back(1);
                    break;
                }else{
                    row.push_back(prev[left] + prev[right]);
                }
                left++;
                right++;
            }
            ans.push_back(row);
        }

        return ans;

    }
};