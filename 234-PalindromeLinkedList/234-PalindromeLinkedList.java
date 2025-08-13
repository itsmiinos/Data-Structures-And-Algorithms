// Last updated: 8/13/2025, 8:20:57 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode first = head;
        ListNode second = head;
        Stack<ListNode> st = new Stack();

        while(first!=null){
            st.push(first);
            first = first.next;
        }

        while(st.size()>0){
            ListNode temp = st.pop();
            if(temp.val!=second.val){
                System.out.print(temp.val + " " + second.val);
                return false;
            }
            second = second.next;
        }

        return true;

    }
}