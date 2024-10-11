/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        return check(root) != -1;
    }

    public int check (TreeNode root){
        if (root == null){
            return 0;
        }

        int left_height = check (root.left);
        if (left_height == -1){
            return -1;
        }

        int right_height = check (root.right);
        if (right_height == -1){
            return -1;
        }

        if (Math.abs(left_height - right_height) > 1){
            return -1;
        }
        
        return 1 + Math.max(left_height, right_height);
    }
}
