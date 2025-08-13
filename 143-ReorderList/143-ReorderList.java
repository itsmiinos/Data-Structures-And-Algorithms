// Last updated: 8/13/2025, 8:22:14 PM
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
    public void reorderList(ListNode head) {

        //finding the middle of the linkedlist
        ListNode slow = head;
        ListNode fast = head;
        while(fast.next!=null && fast.next.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode headSecond = slow.next;
        slow.next = null;

        //reversing the second part
        ListNode prev = null;
        ListNode curr = headSecond;
        while(curr!=null){
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        headSecond = prev;
        //slow.next= headSecond;

        //connecting the linked list
        ListNode headFirst = head;
        while(headSecond!=null){
            ListNode tempFirst = headFirst.next;
            ListNode tempSecond = headSecond.next;
            headFirst.next = headSecond;
            headSecond.next = tempFirst;
            headSecond = tempSecond;
            headFirst = tempFirst;
        }

        
    }
}