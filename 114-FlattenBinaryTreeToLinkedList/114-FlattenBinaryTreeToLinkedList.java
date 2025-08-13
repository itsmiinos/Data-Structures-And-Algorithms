// Last updated: 8/13/2025, 8:22:45 PM
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
    public void flatten(TreeNode root) {
        flattenHelper(root);
    }

    public TreeNode flattenHelper(TreeNode root){
        if(root==null){
            return root;
        }

        TreeNode leftLast = flattenHelper(root.left);
        TreeNode rightLast = flattenHelper(root.right);

        if(root.left==null && root.right==null){
            return root;
        }
        else if(root.left!=null && root.right==null){
            TreeNode leftChild = root.left;
            root.right = leftChild;
            root.left = null;
            return leftLast;
        }
        else if(root.left==null && root.right!=null){
            return rightLast;
        }
        else{
            TreeNode rightChild  = root.right;
            TreeNode leftChild = root.left;
            root.right = leftChild;
            leftLast.right = rightChild;
            root.left = null;
            return rightLast;
        }
    }
}