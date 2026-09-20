class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string current;
        backtrack(ans ,n , n , current);
        return ans;
    }

    void backtrack(vector<string>& ans, int open , int close , string current){
        if (open == 0 && close == 0){ 
            ans.push_back(current);
            return;
        }
        if (open<=close){
            if (open>0){
                backtrack(ans , open-1 , close , current+'(');
            }
            if (close > 0){
                backtrack(ans , open , close - 1 , current + ')');
            }
        }
    }
};
