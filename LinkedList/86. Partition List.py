# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]: # type: ignore
        before, after = ListNode(0), ListNode(0) # type: ignore
        before_curr, after_curr = before, after
        
        while head:
            if head.val < x:
                before_curr.next, before_curr = head, head
            else:
                after_curr.next, after_curr = head, head
            head = head.next
        
        after_curr.next = None
        before_curr.next = after.next
        
        return before.next
    

    # https://leetcode.com/problems/partition-list/solutions/3910837/100-two-pointer-video-linked-list-visualization-optimal
    