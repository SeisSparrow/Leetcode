class Solution {
  public boolean hasCycle(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;
    while (fast != null && slow != null) {
      fast = fast.next;
      slow = slow.next;
      if (fast != null) {
        fast = fast.next;
      }
      if (fast == slow) {
       break;
      }
    }
    
    if (fast != null && slow != null && (fast == slow)) {
      return true;
    } else {
      return false;
    }
  }
}
