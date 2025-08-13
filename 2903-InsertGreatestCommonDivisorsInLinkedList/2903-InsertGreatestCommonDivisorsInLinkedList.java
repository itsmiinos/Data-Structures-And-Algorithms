// Last updated: 8/13/2025, 8:15:38 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode temp = head;
        if(head.next==null)return head;
        ListNode tempnext = head.next;
        while(tempnext!=null){
            ListNode newNode = gcdHelper(temp.val,tempnext.val);
            temp.next = newNode;
            newNode.next = tempnext;

            temp = tempnext;
            tempnext = tempnext.next;
        }
        return head;
    }

    public ListNode gcdHelper(int a , int b){
        int gcd=0;
         while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        gcd = a;
        ListNode node = new ListNode();
        node.val = gcd;
        node.next = null;
        return node;
    }
}