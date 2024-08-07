# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # type: ignore
        res = ListNode(0, head) # type: ignore
        dummy = res

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return res.next 
    

    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/5418407/video-using-distance-between-two-pointers