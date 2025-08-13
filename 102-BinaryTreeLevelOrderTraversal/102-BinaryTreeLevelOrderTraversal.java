// Last updated: 8/13/2025, 8:22:53 PM
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> q = new LinkedList();
        List<List<Integer>> list = new ArrayList();
        q.add(root);
        if(root == null) return list;
        while(q.size()>0){
            List<Integer> sublist = new ArrayList();
            int n = q.size();
            while(n>0){
                TreeNode temp = q.remove();
                sublist.add(temp.val);
                if(temp.left!=null){
                    q.add(temp.left);
                }
                if(temp.right!=null){
                    q.add(temp.right);
                }
                n--;
            }
            list.add(sublist);
        }
        return list;
    }
}