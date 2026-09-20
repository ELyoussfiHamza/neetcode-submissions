/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
unordered_map<TreeNode* ,int> seen;
public:
    int rob(TreeNode* root) {
       if (seen.contains(root)){
            return seen[root];
        }
        if (!root){
            return 0;
        }

        int robnow = 0;
        int dontrob= rob(root->left) + rob(root->right);;
        if (root->left and root->right){
            robnow = rob(root->left->left) + rob(root->left->right) + rob(root->right->left) + rob(root->right->right);
        }else if (root->left){
            robnow = rob(root->left->left) + rob(root->left->right);
        }else if (root->right){
        robnow =  rob(root->right->left) + rob(root->right->right);
        }
        seen[root] = max(root->val+ robnow , dontrob);
        return seen[root];
        }
        
    
};