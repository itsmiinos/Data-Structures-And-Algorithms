// Last updated: 8/13/2025, 8:22:13 PM
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
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> list = new ArrayList();
        traversal(root,list);
        return list;
    }

    public void traversal(TreeNode root, ArrayList list){
        if(root==null){
            return;
        }
        list.add(root.val);
        traversal(root.left,list);
        traversal(root.right,list);
    }
}