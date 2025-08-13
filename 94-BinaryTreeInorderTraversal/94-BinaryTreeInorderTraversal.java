// Last updated: 8/13/2025, 8:23:00 PM
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
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> list = new ArrayList();
        traversal(root,list);
        return list;
    }

    public void traversal(TreeNode root, ArrayList list){
        if(root==null){
            return;
        }
        traversal(root.left,list);
        list.add(root.val);
        traversal(root.right,list);
    }
}