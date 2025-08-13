// Last updated: 8/13/2025, 8:21:53 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int length1 = 0;
        int length2 = 0;

        ListNode tempA= headA;
        ListNode tempB = headB;

        while(tempA!=null){
            tempA = tempA.next;
            length1++;
        }

        while(tempB!=null){
            tempB = tempB.next;
            length2++;
        }

        int diff = length2 - length1;

        if(diff<0){
            while(diff!=0){
                headA = headA.next;
                diff++;
            }
        }
        else{
            while(diff!=0){
                headB = headB.next;
                diff--;
            }
        }

        while(headA!=headB){
            headA = headA.next;
            headB = headB.next;
        }

        return headA;
    }
}