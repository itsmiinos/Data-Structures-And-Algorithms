// Last updated: 8/13/2025, 8:22:18 PM
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        // if(head==null && head.next!=null){
        //     return -1;
        // }

        while(fast!=null && fast.next!=null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow==fast){
                break;
            }
        }

        if(fast==null || fast.next==null){
            return null;
        }

        fast = head;

        while(fast!=slow){
            fast = fast.next;
            slow = slow.next;
        }

        return slow;
    }
}